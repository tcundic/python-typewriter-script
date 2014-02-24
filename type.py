#!/usr/bin/env python

import subprocess
import time
import sys
import os
import os.path
from Xlib.display import Display
import random
import Tkinter as tk
import pyxhook as hooklib

class TypeWritter:
  
    def __init__(self):
	
	self.hm = hooklib.HookManager()
	self.hm.HookKeyboard()
	self.hm.KeyDown = self.OnKeyDownEvent
	self.disp = Display()
	
	self.RETURNFILE = os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0] + '/enter.wav'
	self.BACK = os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0] + '/backspace.wav'
	self.SPACE = os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0] + '/spacebar.wav'
	self.SHFT = os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0] + '/shift.wav'
	self.TABULATOR = os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0] + '/tab.wav'
	
	self.path = os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0] + "/sounds/"
	
	self.ZERO, self.SHIFT, self.ALT, self.CTL, self.BACKSPACE, self.SPACEBAR, self.TAB, self.SHIFT2=[],[],[],[], [], [], [], []
	self.ENTER = [0, 0, 0, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	for i in range(0,32):
	    self.ZERO.append(0)
	    if i==6:
		self.SHIFT.append(4)
	    else:
		self.SHIFT.append(0)
	    if i==7:
		self.SHIFT2.append(64)
	    else:
		self.SHIFT2.append(0)
	    if i==4:
		self.CTL.append(32)
	    else:
		self.CTL.append(0)
	    if i==8:
		self.ALT.append(1)
	    else:
		self.ALT.append(0)
	    if i==2:
		self.BACKSPACE.append(64)
	    else:
		self.BACKSPACE.append(0)
	    if i==8:
		self.SPACEBAR.append(2)
	    else:
		self.SPACEBAR.append(0)
	    if i==2:
		self.TAB.append(128)
	    else:
		self.TAB.append(0)

	self.ignorelist=[self.ZERO,self.ALT,self.CTL]
	
    def start(self):
	self.hm.start()

    def OnKeyDownEvent(self, event):
	self.mute = open(os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0] + "/mute.dat", "r").read()
	self.keymap = self.disp.query_keymap()
	if self.keymap not in self.ignorelist:
	    self.x = random.choice(os.listdir(self.path))
	    self.wav = os.path.join(self.path, self.x)
	    self.KEYPRESSFILE = self.wav
	if self.keymap == self.ENTER:
		self.filename = self.RETURNFILE
	elif self.keymap == self.BACKSPACE:
		self.filename = self.BACK
	elif self.keymap == self.SPACEBAR:
		self.filename = self.SPACE
	elif self.keymap == self.SHIFT or self.keymap == self.SHIFT2:
		self.filename = self.SHFT
	elif self.keymap == self.TAB:
		self.filename = self.TABULATOR
	else:
		self.filename = self.KEYPRESSFILE
	if self.mute == "False":
			subprocess.Popen(['aplay', self.filename], stderr=open('/dev/null', 'w'))

	if self.mute == "Exit":
		self.stop()
	#uncomment this line to print keycode for each key
	#print self.keymap 
	    
    def stop(self):
	self.hm.cancel()
	sys.exit()
	
if __name__== '__main__':
    tw = TypeWritter()
    tw.start()
