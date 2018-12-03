#!/usr/bin/python

import paramiko
import sys
import json
import os
import logging
import argparse
import subprocess
from abc import abstractmethod, ABCMeta

logger = logging.getLogger(__name__)
logfile = "script_log.log"

formatter = logging.Formatter('%(asctime)s - %(name)s : %(message)s')

screen_handler = logging.StreamHandler(sys.stdout)
screen_handler.setLevel(logging.DEBUG)
screen_handler.setFormatter(formatter)

file_handler = logging.FileHandler(logfile)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

logger.addHandler(screen_handler)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


class Response(object):
    def __init__(self, out="", error="", exitcode=-1, failure_reason=None):
        self.out = out
        self.error = error
        self.exitcode = exitcode
        self.failure_reason = failure_reason

    @property
    def is_success(self):
        return self.exitcode == 0


class Host(object):
    __metaclass__ = ABCMeta
    EMPTY_PASSPHRASE_BY_DEFAULT = "\"\""

    def __init__(self, ip, user_name, password, file_with_private_key, file_with_public_key,
                 file_with_authorized_keys):
        self.ip = ip
        self.user_name = user_name
        self.password = password
        self.file_with_private_key = file_with_private_key
        self.file_with_public_key = file_with_public_key
        self.file_with_authorized_keys = file_with_authorized_keys

    @abstractmethod
    def run_cmd(self, cmd):
        pass

    def remove_file(self, file_path):
        self.run_cmd("rm {}".format(file_path))

    def create_file(self, file_path):
        self.run_cmd("touch {}".format(file_path))

    def add_info_to_file(self, info, file_path):
        self.run_cmd('echo "{}" >> {}'.format(info, file_path))

    @abstractmethod
    def get_file_content(self, file_path):
        pass

    def remove_ssh_keys(self):
        self.remove_file(self.file_with_private_key)
        self.remove_file(self.file_with_public_key)
        self.remove_file(self.file_with_authorized_keys)

    def generate_ssh_keys(self, passphrase=EMPTY_PASSPHRASE_BY_DEFAULT):
        self.run_cmd("ssh-keygen -f {} -q -N {}".format(self.file_with_private_key, passphrase))

    def configure_passwordless_connection_with_(self, another_host):
        key = self.get_file_content(self.file_with_public_key)
        another_host.add_info_to_file(key, self.file_with_authorized_keys)


class RemoteHost(Host):
    def __init__(self, ip, user_name, password, file_with_private_key,
                 file_with_public_key, file_with_authorized_keys):
        super(RemoteHost, self).__init__(ip, user_name, password, file_with_private_key,
                                         file_with_public_key, file_with_authorized_keys)
        self.ssh_connection = paramiko.SSHClient()
        self.ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.connect()

    def connect(self):
        try:
            logger.info("Connecting to host {}".format(self.ip))
            self.ssh_connection.connect(self.ip, username=self.user_name, password=self.password)
            logger.info("Connected to host {}".format(self.ip))
            return Response(exitcode=0)
        except paramiko.SSHException as exc:
            logger.error("Connection to host {} failed".format(self.ip))
            return Response(exitcode=-1, failure_reason=exc)

    def run_cmd(self, cmd):
        if not self.ssh_connection.get_transport().is_active():
            self.connect()
        try:
            stdin, stdout, stderr = self.ssh_connection.exec_command(cmd)
            logger.info("Executed command \"{}\" on host {}".format(cmd, self.ip))
            exit_code = stdout.channel.recv_exit_status()
            return Response(stdout, stderr, exit_code)
        except Exception as exc:
            return Response(exitcode=-1, failure_reason=exc)

    def get_file_content(self, file_path):
        sftp_client = self.ssh_connection.open_sftp()
        remote_file = sftp_client.open(os.path.expanduser(file_path))
        return remote_file.read()


class LocalHost(Host):
    def run_cmd(self, cmd):
        try:
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, shell=True)
            logger.info("Executed command \"{}\" on host {}".format(cmd, self.ip))
            out, err = proc.communicate()
            exit_code = proc.returncode
            return Response(out.decode("cp866"), err, exit_code)
        except Exception as exc:
            return Response(exitcode=-1, failure_reason=exc)

    def get_file_content(self, file_path):
        with open(file_path) as file_to_read:
            return file_to_read.read()


class HostPool(object):
    def __init__(self):
        self._hosts = []

    def add_host(self, host):
        if not isinstance(host, Host):
            raise TypeError("In pool of hosts you can add only Host objects. Except got type: {}".format(type(host)))
        self._hosts.append(host)

    def add_hosts(self, *hosts):
        for host in hosts:
            self.add_host(host)

    def remove_host(self, host):
        try:
            self._hosts.remove(host)
        except ValueError:
            print("ValueError: host is not in pool".format(host))

    def remove_hosts(self, *hosts):
        for host in hosts:
            self.remove_host(host)

    def contains(self, host):
        return host in self._hosts

    def configure_passwordless_connection_between_hosts(self):
        for host in self._hosts:
            for host_to_connect_with in self._hosts:
                if host_to_connect_with is host:
                    continue
                host.configure_passwordless_connection_with_(host_to_connect_with)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('config_file', type=argparse.FileType('r'))
    args = parser.parse_args()
    config = json.load(args.config_file)

    ips_ = config["ips"]
    username_ = config["username"]
    password_ = config["password"]
    file_with_private_key_ = config["file_with_private_key"]
    file_with_public_key_ = config["file_with_public_key"]
    file_with_authorized_keys_ = config["file_with_authorized_keys"]

    hosts_ = [
        RemoteHost(ip_, username_, password_, file_with_private_key_, file_with_public_key_, file_with_authorized_keys_)
        if ips_[ip_] == "remote"
        else LocalHost(ip_, username_, password_, file_with_private_key_, file_with_public_key_,
                       file_with_authorized_keys_)
        for ip_ in ips_]

    network = HostPool()

    for host_ in hosts_:
        host_.remove_ssh_keys()
        host_.generate_ssh_keys()
        network.add_host(host_)

    network.configure_passwordless_connection_between_hosts()
