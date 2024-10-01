import os, sys, platform,time
 
bit = platform.architecture()[0]
os.system('git pull')
if bit == '64bit':
    os.system('clear')
    os.system('git pull')
    os.system('xdg-open https://chat.whatsapp.com/IIFAd4VrnBk2XJZrGs2oxw');time.sleep(2)
    os.system('xdg-open https://www.facebook.com/ARAFAT19847000');time.sleep(2)
    os.system('git pull')
    print("TOOLS IS OFF");time.sleep(4)
   # os.system('chmod 777 RANDOM')
    #os.system('./RANDOM')
    
elif bit == '32bit':
    os.system("clear")
    os.system('xdg-open https://www.facebook.com/ARAFAT19847000');time.sleep(2)
    print("SORRY 32 BIT IS NOT UPLOADED")
 
