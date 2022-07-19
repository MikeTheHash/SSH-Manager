import os
from colorama import Back, Fore, Style

def main():
	os.system("figlet SSH-Manager")
	print("1: Start SSH server \n2: Status of SSH server \n3: Stop SSH server \n4: Connect to an SSH server \n5: Clear \n6: Exit")
	iusr = input("Select an option >")
	if iusr == "1":
		os.system("service ssh start")
		print("SSH server started!")

	if iusr == "2":
		os.system("service ssh status")

	if iusr == "3":
		os.system("service ssh stop")
		print("SSH server stopped")

	if iusr == "4":
		iusr2 = input("Type the login-username >")
		iusr3 = input("Type the IP-Adress >")
		os.system(f"ssh {iusr2}@{iusr3}")

	if iusr == "5":
		os.system("clear")
		os.system("figlet SSH-Manager-v1.0")
		print("1: Start SSH server \n2: Status of SSH server \n3: Stop SSH server \n4: Connect to an SSH server \n5: Clear \n6: Exit")
	if iusr == "6":
		exit()
while(True):
	main()
