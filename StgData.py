from pystyle import Colors , Colorate
import PIL.Image
from PIL.ExifTags import TAGS
import io
from pathlib import Path
from six.moves import input
import os , sys
from stegano import lsb
from time import sleep





class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'


def banner():
    os.system("clear")
    print(Colorate.Horizontal(Colors.green_to_red,'+[+[+[ STgData v1.0 ]+]+]+'))
    print(Colorate.Horizontal(Colors.green_to_red,'+[+[+[ made By Tarek DHK ]+]+]+\n\n'))
    os.system("\nfiglet -f Bloody StgData | lolcat")
    os.system("echo '\t\t\t+++ Coded_By_Tarek_Dhokkar +++' | lolcat ")
    print(Colorate.Horizontal(Colors.green_to_red,''' 
                                                                                                                         
 ***************************************       
 + 1 + Hide Image Into another         *       
 + 2 + Export Hidden Image             *       
 + 3 + Hide Any File In Image          *       
 + 4 + Export Hidden File From Image   *      
 + 5 + Hide Message in Image           *       
 + 6 + Export Hidden message           *
 + 7 + Show META_Data From Images      *       
 ***************************************       
                      + Fb   : Tarek Dhk                                        
                      + Insta: tarek_dgh                                                          
 '''))




banner()
while True:
    ch=int(input(Colorate.Horizontal(Colors.yellow_to_green,"++ Chose One Of This Options >>> ")))
    if ch<=8:
        break


#Condition1 Hide Photo Into another 
if ch==int(1):
    os.system("clear")
    os.system("\nfiglet -f Whimsy HidePhoto | lolcat")
    os.system("echo '\t\t\t+++ Coded_By_Tarek_Dhokkar +++\n\n\n' | lolcat ")
    Current_img = input(Colorate.Horizontal(Colors.green_to_blue,"++ Enter the output Photo <3 >>> "))
    Insert_img = input(Colorate.Horizontal(Colors.green_to_blue,"++ Enter Photo you want to hide It! >>> "))
    if (Current_img!="")and(Insert_img!=""):
    	img = PIL.Image.open(Insert_img)
    	byte_arr = io.BytesIO()
    	img.save(byte_arr, format='PNG')
    	with open(Current_img, 'ab') as f:
        	f.write(byte_arr.getvalue())
    	sleep(1)
    	print(Colorate.Horizontal(Colors.yellow_to_red,"Done !!  Photo injected Successfully"))
    else:
    	print(Colorate.Horizontal(Colors.red_to_green,"\n\n>>> Put The right Path !! ya wldi yhdik -__- !!"))	
    sleep(3)
    os.system("python3 StgData.py")
    
#Condition 2 Unhide steg photo   
elif ch==int(2):
    os.system("clear")
    os.system("\nfiglet -f Whimsy EXTPhoto | lolcat")
    os.system("echo '\t\t\t+++ Coded_By_Tarek_Dhokkar +++\n\n\n' | lolcat ")
    image_int = input(Colorate.Horizontal(Colors.green_to_blue,"++ Enter The current image  "))
    Name_OutImg = input(Colorate.Horizontal(Colors.green_to_blue,"++ Enter New Image Name >> "))
    if (image_int!="")and(Name_OutImg!=""):
    	with open(image_int, 'rb') as f:
        	content = f.read()
        	offset = content.index(bytes.fromhex('FFD9'))
        	

        	f.seek(offset + 2)
        	new_img = PIL.Image.open(io.BytesIO(f.read()))

        	new_filename = Path(Name_OutImg).stem + ".png"
        	new_img.save(new_filename)
    	sleep(1)
    	print(Colorate.Horizontal(Colors.yellow_to_red,"Done !!  Check Tool Folder <3 "))
    else:
    	print(Colorate.Horizontal(Colors.red_to_green,"\n\n>>> Put The right Path !! ya wldi yhdik -__- !!"))
    sleep(3)
    os.system("python3 StgData.py")

#Condition 3 Hide any file into photo
elif ch==int(3):
    os.system("clear")
    os.system("\nfiglet -f Whimsy HideFiles | lolcat")
    os.system("echo '\t\t\t+++ Coded_By_Tarek_Dhokkar +++\n\n\n' | lolcat ")
    exe_prog = input(Colorate.Horizontal(Colors.green_to_blue,"++ Enter the executable file >>  "))
    Current_Img = input(Colorate.Horizontal(Colors.green_to_blue,"++ Enter The Current Image To export it >> "))
    with open(Current_Img, "ab") as g, open(exe_prog, "rb") as e:
        g.write(e.read())
    sleep(1)
    print(Colorate.Horizontal(Colors.yellow_to_red,"Done !! The File injected Successfully <3 "))
    sleep(2)
    os.system("python3 StgData.py")

#Condition 4 Unhide the file
elif ch==int(4):
    os.system("clear")
    os.system("\nfiglet -f Whimsy EXTFiles | lolcat")
    os.system("echo '\t\t\t+++ Coded_By_Tarek_Dhokkar +++\n\n\n' | lolcat ")
    Current_IMg = input(Colorate.Horizontal(Colors.green_to_blue,"++ Enter The Current Image To export it >> "))
    newfile=input(Colorate.Horizontal(Colors.green_to_blue,"++ Enter the Output .exe File >> "))
    with open(Current_IMg, "rb") as g:
        cont = g.read()
        off = cont.index(bytes.fromhex('FFD9'))

        g.seek(off + 2)
        with open(newfile, "wb") as n:
            n.write(g.read())
    sleep(1)
    print(Colorate.Horizontal(Colors.yellow_to_red,"Done !!  Check Tool Folder <3 "))
    sleep(2)
    os.system("python3 StgData.py")
    
#Condition 5 Msg hide 
elif ch==int(5):
    os.system("clear")
    os.system("\nfiglet -f Whimsy HideMsg | lolcat")
    os.system("echo '\t\t\t+++ Coded_By_Tarek_Dhokkar +++\n\n\n' | lolcat ")
    msg = input(Colorate.Horizontal(Colors.green_to_blue,"++ Enter A message  >>  "))
    image = input(Colorate.Horizontal(Colors.green_to_blue,"++ Enter The Picture Path or name >> "))
    new_imgss=input(Colorate.Horizontal(Colors.green_to_blue,"++ Enter the New Picture Name >> "))
    
    lsb.hide(image,message=msg).save(new_imgss)
    sleep(1)
    print(Colorate.Horizontal(Colors.yellow_to_red,"Done !! Msg Injected Successfuly Check Tool Folder <3 "))
    sleep(2)
    os.system("python3 StgData.py")

#Condition 6 Unhide Msg
elif ch==int(6):
    os.system("clear")
    os.system("\nfiglet -f Whimsy EXTMsg | lolcat")
    os.system("echo '\t\t\t+++ Coded_By_Tarek_Dhokkar +++\n\n\n' | lolcat ")
    new_imgss=input(Colorate.Horizontal(Colors.green_to_blue,"++ Enter the New image to export the message >> "))
    reveal_img= lsb.reveal(new_imgss)
    with open("newtext.txt", "w")as f:
        f.write(reveal_img)
    sleep(1)
    print(Colorate.Horizontal(Colors.yellow_to_red,"The Message : ",reveal_img))
    print(Colorate.Horizontal(Colors.yellow_to_red,"Also the message in (newtext.txt) check the tool folder <3"))
    sleep(3)
    os.system("python3 StgData.py")
#Condition 7 Show the EXIF meta Data From any Photo 
elif ch==int(7):
    os.system("clear")
    os.system("figlet -f Whimsy EXIFData | lolcat")
    os.system("echo '\t\t+++ Coded_By_Tarek_Dhokkar +++\n\n\n' | lolcat ")
    print(Colorate.Horizontal(Colors.yellow_to_red,"Dude! The photos From FB or Insta etc.. \nThey Don't Have meta Data (auto removed)"))
    sleep(0)
    ino=input(Colorate.Horizontal(Colors.green_to_blue,"\n\n++ Enter The image Path To Export EXIFData >> "))
    image= PIL.Image.open(ino)
    exifdata = image.getexif()
    i=0
    for tid in exifdata:
    	tagname = TAGS.get(tid)
    	value = exifdata.get(tid)
    	print("{} : {}".format(tagname,value))
    	i+=1
    if i==0:
    	print(Colorate.Horizontal(Colors.green_to_red,"\n\nSorry!! Dude -_- \nThere's no EXIF MetaData In This Image "))
    sleep(3)
    os.system("python3 StgData.py")
