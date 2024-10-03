import os,platform,subprocess,requests,time
#_____________________[SIM NAME CODE]____________________________#
orange = "\x1b[38;5;196m";yellow = "\x1b[38;5;208m";black="\033[1;30m";rad="\x1b[38;5;160m";green="\x1b[38;5;46m";yelloww="\033[1;33m";blue="\033[38;5;6m";purple="\033[1;35m";cyan="\033[1;36m";white="\033[1;37m";faltu = "\033[1;47m";pvt = "\033[1;0m";gren = "\x1b[38;5;154m";gas = "\033[1;32m";W = "\033[1;37m";G = "\033[38;5;46m";G1 = "\033[38;5;47m";G2 = "\033[38;5;48m";G3 = "\033[38;5;49m";G4 = "\033[38;5;50m";R = "\033[38;5;196m";R3 = "\033[38;5;1m";R1 = "\033[38;5;202m";R2 = "\033[38;5;203m";C = "\033[38;5;4m";K="\033[38;5;15m";A="\033[38;5;248m";LG="\033[38;5;195m";A1="\033[38;5;250m";A2="\033[38;5;251m";A3="\033[38;5;252m";A4="\033[38;5;253m";A5="\033[38;5;254m";B="\033[38;5;153m";logo = '\x1b[38;5;154m';logo1 = '\x1b[38;5;155m';logo2 = '\x1b[38;5;156m';logo3 = '\x1b[38;5;157m';logo4 = '\x1b[38;5;158m';z = f'{W}[{G}✗{W}] ';age = f'{W}[{G}';pore = f'{W}] '
try:
    output = subprocess.check_output('getprop gsm.operator.alpha', shell=True).decode('utf-8')
    ahydra = output.replace(',', '|').replace('\n', '')
except Exception as e:pass;ahydra = None
bit = platform.architecture()[0]
os.system('clear')
os.system('xdg-open https://chat.whatsapp.com/IIFAd4VrnBk2XJZrGs2oxw');time.sleep(2)
os.system('xdg-open https://www.facebook.com/ARAFAT19847000');time.sleep(2)
os.system('git pull')
#__________________[ TOOL VERSION ]__________________#
try:
    version = requests.get("htt"+"ps://r"+"aw.git"+"hubus"+"erc"+"onten"+"t.com/AR"+"AFAT-"+"X-MI"+"TUL/AC"+"CE"+"SS/ma"+"in/vers"+"ion.txt").text
except:
    print('No Internet Connection');exit()
version = version.strip()
line = (f'{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
"""-------------------------(LOGO BOX)-------------------------"""
logo = (f"""\n {logo} █████  ██   ██ ███    ███ {W}┃ \n {logo}██   ██  ██ ██  ████  ████ {W}┃     \n {logo}███████   ███   ██ ████ ██ {W}┃ SIM {R}× {G}{ahydra}\n {logo}██   ██  ██ ██  ██  ██  ██ {W}┃ DEVICE {R}× {G}{bit}\n {logo}██   ██ ██   ██ ██      ██ {W}┃ VERSION {R}× {G}PAID {R}× {G}{version}\n{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━\n          {R}× {G}AXM AGAIN BACK WITH NEW LOOK {R}×\n{line}\n{z}{W}AUTHOR  : {G}MOHAMMAD ARAFAT\n{z}{W}GITHUB  : {G}GITHUB.COM/AXM \n{z}{W}TOOL    : {G}FILE {R}× {G}RANDOM \n{z}{W}TYPE    : {G}FREE TOOLS\n{line}""")
def linex():
    print(f'{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
#-------------------------------[MAIN MENU]------------------------------#
def clear():os.system('clear');print(logo)
#---------------------------| MENU BOX |---------------------------#
def _____menu_____():
        clear()
        print(f'{age}1{pore}GRAPH SYSTEM');print(f'{age}2{pore}HOST SYSTEM');linex();option=input(f'{z}CHOICE : ')
        if option in ["1"]:os.system("./RANDOMM")
        if option in ["2"]:os.system("./RANDOM")
        else:_____menu_____()
_____menu_____()
