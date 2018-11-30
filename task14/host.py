#!/usr/bin/python

import paramiko
import sys
import json
import os
import logging
import argparse

logger = logging.getLogger(__name__)
logfile = "script_log.log"

formatter = logging.Formatter('%(asctime)s - %(name)s : %(message)s')
screen_handler = logging.StreamHandler(sys.stdout)
screen_handler.setLevel(logging.INFO)
screen_handler.setFormatter(formatter)

file_handler = logging.FileHandler(logfile)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(screen_handler)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


class Response(object):
    A_OK = 0x0
    BAD_APP = 0x1
    INSUFFICIENT_PERMISSIONS = 0x2

    def __init__(self, out, error, exitcode):
        self.out = out
        self.error = error
        self.exitcode = exitcode
        self._failure_reason = self.A_OK
        self._process_error_set_reason()

    def _process_error_set_reason(self):
        if self.error and "is not recognized" in self.out:
            self._failure_reason = self.BAD_APP

    @property
    def is_success(self):
        return self.exitcode == 0

    @property
    def failure_reason(self):
        return self._failure_reason


class DummyResponse(Response):
    def __init__(self, failure_reason):
        super(DummyResponse, self).__init__("", "", -1)
        self._failure_reason = failure_reason

    @property
    def failure_reason(self):
        return self._failure_reason


class Host(object):
    def __init__(self, ip, user_name, password):
        self.ip = ip
        self.user_name = user_name
        self.password = password
        self.ssh_connection = paramiko.SSHClient()
        self.connect()

    def connect(self):
        self.ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            self.ssh_connection.connect(self.ip, username=self.user_name, password=self.password)
        except paramiko.SSHException:
            logger.info("Connection to host {} failed".format(self.ip))
        logger.info("Connected to host {}".format(self.ip))

    def run_cmd(self, cmd, *user_inputs):
        if not self.ssh_connection.get_transport().is_active():
            self.connect()
        try:
            stdin, stdout, stderr = self.ssh_connection.exec_command(cmd)
            logger.info("Executed command {} on host {}".format(cmd, self.ip))
            for user_input in user_inputs:
                stdin.write(user_input)
            stdin.channel.shutdown_write()
            exit_code = stdout.channel.recv_exit_status()
            return Response(stdout, stderr, exit_code)
        except Exception as e:
            return DummyResponse(failure_reason=e)


class Checker(object):
    @staticmethod
    def check_response(response):
        logger.debug(response.out)
        if not response.is_success:
            logger.debug(response.failure_reason)
            logger.debug(response.error)


class SSHConfiguration(object):
    NEWLINE_FOR_SAVING_FILE_TO_DEFAULT_PATH = "\n"
    EMPTY_PASSPHRASE = "\n"

    @staticmethod
    def remove_ssh_keys(host):
        response = host.run_cmd("rm ~/.ssh/authorized_keys")
        Checker.check_response(response)
        response = host.run_cmd("rm ~/.ssh/id_rsa")
        Checker.check_response(response)
        response = host.run_cmd("rm ~/.ssh/id_rsa.pub")
        Checker.check_response(response)

    @staticmethod
    def generate_ssh_keys(host, file_to_save_key=NEWLINE_FOR_SAVING_FILE_TO_DEFAULT_PATH, passphrase=EMPTY_PASSPHRASE):
        response = host.run_cmd("ssh-keygen", file_to_save_key, passphrase, passphrase)
        Checker.check_response(response)

    @staticmethod
    def configure_passwordless_connection(hosts):
        for host in hosts:
            sftp_client = host.ssh_connection.open_sftp()
            remote_file = sftp_client.open(os.path.expanduser(".ssh/id_rsa.pub"))
            key = remote_file.read()
            for host__ in hosts:
                response = host__.run_cmd('echo "%s" >> ~/.ssh/authorized_keys' % key)
                Checker.check_response(response)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('config_file', type=argparse.FileType('r'))
    args = parser.parse_args()
    config = json.load(args.config_file)

    ips_ = config["ips"]
    username_ = config["username"]
    password_ = config["password"]

    host1 = Host(ips_[0], username_, password_)
    host2 = Host(ips_[1], username_, password_)
    host3 = Host(ips_[2], username_, password_)
    hosts_ = [host1, host2, host3]

    for host_ in hosts_:
        SSHConfiguration.remove_ssh_keys(host_)
        SSHConfiguration.generate_ssh_keys(host_)

    SSHConfiguration.configure_passwordless_connection(hosts_)
