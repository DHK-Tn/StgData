from pystyle import Colors , Colorate
from time import sleep
import os
os.system("clear")
os.system("unzip figlet.zip")
os.system("sudo gem install lolcat")
sleep(1)
os.system("clear")
while True:
	print(Colorate.Horizontal(Colors.green_to_blue,"I will automate Remove Your Figlet Folder and move My Figlet Folder Y/N "))
	n=str(input(Colorate.Horizontal(Colors.green_to_red,"\n     >>>  ")))
	if (n.upper()=="Y")or(n.upper()=="N"):
		break
if n.upper()=="Y":
	os.system("rm -rf /usr/share/figlet")
	os.system("cp -r figlet /usr/share/")
	print(Colorate.Horizontal(Colors.green_to_blue,"\nDone! Have Fun Using The Tool"))
	sleep(2)
	os.system("python3 StgData.py")
else:
	os.system("clear")
	print(Colorate.Horizontal(Colors.green_to_red,"Per-Attention !!!!"))
	print(Colorate.Horizontal(Colors.green_to_blue,"\nPls! Copy All Files In Figlet tool Folder  to Your Figlet Folder \nIn Path (/usr/share/figlet/)"))
	print(Colorate.Horizontal(Colors.red_to_blue,"\nBras lmyma Copihom fy el figlet directory <3"))
	print(Colorate.Horizontal(Colors.green_to_red,"\nBye!!  Have Fun <3"))
