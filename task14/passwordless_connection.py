import json
import paramiko
import sys


def configure_passwordless_conection(hosts, username, password):
    for host in hosts:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=username, password=password)
        stdin, stdout, stderr = client.exec_command("cat ~/.ssh/id_rsa.pub")
        key = stdout.read()
        for host_ in hosts:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(host_, username=username, password=password)
            client.exec_command('echo "%s" >> ~/.ssh/authorized_keys' % key)
            client.close()
        client.close()


with open(sys.argv[1], 'r') as config_file:
    hosts_data = json.load(config_file)
username_ = hosts_data["username"]
password_ = hosts_data["password"]
hosts_ = hosts_data["ips"]

configure_passwordless_conection(hosts_, username_, password_)
