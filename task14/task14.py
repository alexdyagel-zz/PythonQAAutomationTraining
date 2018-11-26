import paramiko
import json
import os


def generate_ssh_key(ip, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, username=username, password=password)
    except paramiko.SSHException:
        print("Connection Failed")
        quit()
    stdin, stdout, stderr = ssh.exec_command("ssh-keygen")
    stdin.write("\n")
    stdin.write("\n")
    stdin.write("\n")
    stdin.channel.shutdown_write()
    for line in stdout.readlines():
        print(line.strip())
    ssh.close()


def share_public_key_with_hosts(ip, ips, username, password):
    ips.remove(ip)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for ip_of_other_host in ips:
        try:
            ssh.connect(ip, username=username, password=password)
        except paramiko.SSHException:
            print("Connection Failed")
            quit()
        stdin, stdout, stderr = ssh.exec_command("ssh-copy-id {}@{}".format(username, ip_of_other_host))
        stdin.write("{}\n".format(password))
        stdin.channel.shutdown_write()
        for line in stdout.readlines():
            print(line.strip())
        ssh.close()


file_path = '/home/alex_dyagel/python_projects/config.json'
with open(file_path) as hosts_info:
    hosts_data = json.load(hosts_info)
ips_ = hosts_data["ips"]
username_ = hosts_data["username"]
password_ = hosts_data["password"]

for ip_ in ips_:
    generate_ssh_key(ip_, username_, password_)
