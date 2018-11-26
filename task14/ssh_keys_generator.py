import paramiko
import json
import sys


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


with open(sys.argv[1], 'r') as config_file:
    hosts_data = json.load(config_file)
ips_ = hosts_data["ips"]
username_ = hosts_data["username"]
password_ = hosts_data["password"]

for ip_ in ips_:
    generate_ssh_key(ip_, username_, password_)
