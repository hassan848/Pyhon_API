import paramiko
import getpass
from datetime import datetime

filename = str(input("Please Enter a Shell Filename: "))
print(filename)

f = open(f"{filename}", "r")
rf = f.read()

port = 22

def getWorkerInfo():
	host = input('Enter host IP: ')
	username = input('Enter your remote account: ')
	password = getpass.getpass()
	return {'host': host, 'name': username, 'password': password}


command = [f"sh {filename}"]

def ssh_connection(host, username, password):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(host, port, username, password)
	#now we need to transfer the entire shell file
	sftp_client=ssh.open_sftp()

	sftp_client.put(f"{filename}", f"{filename}")
	print()
	startTime = datetime.now()

	stdin, stdout, stderr = ssh.exec_command(command[0])
	#endTime = (datetime.now() - startTime)

	for l in stdout.readlines():
		print(l.strip()) #strip() will print the result without any line breaks
	endTime = (datetime.now() - startTime)

	sftp_client.close()
	ssh.close()
	print(f"The time to execute this task was: {endTime}")
	print()

print()
worker1 = getWorkerInfo()
print()
worker2 = getWorkerInfo()

ssh_connection(worker1['host'], worker1['name'],worker1['password'])
ssh_connection(worker2['host'], worker2['name'],worker2['password'])
