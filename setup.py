#!/bin/env python
# code by :IIT DEVELOPER

import os, sys
import configparser
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
def banner():
	os.system('clear')
	print(f"""
	{re}╦ ╦ ╔╦╗{cy}╔═╗ ┌─┐ ┬ ┬ ╔═╗ ║  ╔═╗ ┌─┐┌─┐┬─┐
        {re}║ ║  ║ {cy}║ ║ ├┤  │ │ ├┤  ║  ║ ║ ├─┘├┤ ├┬┘
        {re}╩ ╩  ╩ {cy}╚═╝ └─┘  ─  ╚═╝ ╚═ ╚═╝ ┴  └─┘┴└─
 
            version : 1.0
     {re} IIT {cy} DEVELOPER 
	{re}╔═╗{cy}┌─┐┌┬┐┬ ┬┌─┐
	{re}╚═╗{cy}├┤  │ │ │├─┘
	{re}╚═╝{cy}└─┘ ┴ └─┘┴
	""")
banner()
print(gr+"[+] Installing requierments ...")
os.system('python -m pip install telethon')
os.system('pip install telethon')
banner()
os.system("touch config.data")
cpass = configparser.RawConfigParser()
cpass.add_section('cred')
xid = input(gr+"[+] enter api ID : "+re)
cpass.set('cred', 'id', xid)
xhash = input(gr+"[+] enter hash ID : "+re)
cpass.set('cred', 'hash', xhash)
xphone = input(gr+"[+] enter phone number : "+re)
cpass.set('cred', 'phone', xphone)
setup = open('config.data', 'w')
cpass.write(setup)
setup.close()
print(gr+"[+] setup complete !")
