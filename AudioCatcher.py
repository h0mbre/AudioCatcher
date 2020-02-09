#!/usr/bin/env python3

import sys
import os
from playsound import playsound
import threading
import time

def check():
	if len(sys.argv) < 3:
		print("usage: example.py -lvp 443\n")
		sys.exit(1)	

def play():
	playsound('~/AudioCatcher/headshot.wav')

def netcat():
	command = ("nc {0} {1}".format(sys.argv[1],sys.argv[2]) + " 2>&1 | tee 1rwN2S.txt")
	os.system(command)
	os.system("rm 1rwN2S.txt")

def file_check():
	while True:
		try:
			f = open("1rwN2S.txt", "r")
			content = f.read()
			if 'connect' in content:
				play()
				break
		except:
			sys.exit(1)
			
def main():
	check()
	netcat()

m = threading.Thread(target=main)
fc = threading.Thread(target=file_check)

m.start()
time.sleep(.1)
fc.start()
