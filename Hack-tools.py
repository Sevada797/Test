#This is a comment
#You can install a list of things from here and use
import os
import sys
import subprocess
import time
os.system('clear') 
print ("\033[1;32;40m installing some usefull things")
print ("\033[1;32;40m Installing PHP")
time.sleep(2)
subprocess.call('pkg install php', shell=True)
print ("\033[1;32;40m Installing nano(for editing files).")
time.sleep(3)
subprocess.call('pkg install nano', shell=True)
os.system('clear')
logo = """
 ____                      _      _____ ___ _____
/ ___|  _____   ____ _  __| | __ |___  / _ \___  |
\___ \ / _ \ \ / / _` |/ _` |/ _` | / / (_) | / /
 ___) |  __/\ V / (_| | (_| | (_| |/ / \__, |/ /
|____/ \___| \_/ \__,_|\__,_|\__,_/_/    /_//_/  \n """
print ("\033[1;32;40m" + logo)
print ("\033[1;31;40m Some hacking programs for you to install \n")
print ("\033[1;32;40m Press 1 for Phishing")
print ("\033[1;32;40m Press 2 for Fb brute-force")
print ("\033[1;32;40m Press 3 for Fb friends info gather")
print ("\033[1;32;40m Press 4 for Insta brute-force")
print ("\033[1;32;40m Press 5 for SMS bombing")
print ("\033[1;32;40m Press 6 for Fakemailer \n")
print ("\033[1;31;40m Program is not working good now. Building is in progress.")
def menu():
    quest = "\033[1;33;40m Enter a number: "
    x = " "
    a = float(input(7*x + quest))
    if a == 1:
      os.system('clear')
      print ("You can also visit")
      print ("shadowave.info & z-shadow.co")
      time.sleep(4)
      subprocess.call('git clone https://github.com/xHak9x/SocialPhish', shell=True)
      subprocess.call('cd SocialPhish')
      subprocess.call('chmod +x socialphish.sh')
      subprocess.call('./socialphish.sh')
    elif a == 2:
        os.system('clear')
        print ("\033[1;31;40m This is not working now!")
    elif a == 3:
        os.system('clear')
        print ("\033[1;31;40m This is not working now!")
    elif a == 4:
        os.system('clear')
        print ("\033[1;31;40m This is not working now!")
    elif a == 5:
        os.system('clear')
        print ("\033[1;31;40m This is not working now!")
    elif a == 6:
        os.system('clear')
        print ("\033[1;31;40m This is not working now!")
    else:
        print ("\033[1;31;40m Please input valid number")
        return menu()

menu()
