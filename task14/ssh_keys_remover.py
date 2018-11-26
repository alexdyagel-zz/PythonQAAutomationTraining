import paramiko
import json
import sys


def remove_ssh_key(ip, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, username=username, password=password)
    except paramiko.SSHException:
        print("Connection Failed")
        quit()
    ssh.exec_command("rm ~/.ssh/authorized_keys")
    ssh.exec_command("rm ~/.ssh/id_rsa")
    ssh.exec_command("rm ~/.ssh/id_rsa.pub")
    ssh.close()


with open(sys.argv[1], 'r') as config_file:
    hosts_data = json.load(config_file)
ips_ = hosts_data["ips"]
username_ = hosts_data["username"]
password_ = hosts_data["password"]

for ip_ in ips_:
    remove_ssh_key(ip_, username_, password_)
