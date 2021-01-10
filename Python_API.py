import paramiko
import getpass

host = input('Enter host IP: ')
port = 22
username = input("Enter your remote account: ")
password = getpass.getpass()

command = "ls"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command(command)
for l in stdout.readlines():
	print(l)
