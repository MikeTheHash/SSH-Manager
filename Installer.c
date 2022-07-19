#include <stdio.h>
#include <string.h>

int main(){
	printf("Installing SSH service...");
	system("sudo apt-get install openssh-server");
	printf("Installing figlet...");
	system("sudo apt-get install figlet");
	printf("Installing python...");
	system("sudo apt-get install python3");
	system("sudo apt-get install python3-pip");
	system("sudo apt-get install pip"); 
	printf("Installing libraries...");
	system("pip install os");
	system("pip install colorama");
}
