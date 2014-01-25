#!/usr/bin/env python

import os
import os.path
import time
import sys
from Xlib.display import Display
import subprocess
import glob
import random
import sys
import Tkinter as tk

if os.name == 'posix':
    import pyxhook as hooklib
elif os.name == 'nt':
    import pyHook as hooklib
    import pythoncom
else:
    print "OS is not recognised as windows or linux."
    exit()

class TypeWritter:
  
    def __init__(self):
	#if os.name == 'posix':
	#self.hashchecker = ControlKeyMonitor(self, self.ControlKeyHash)
	
	self.hm = hooklib.HookManager()
	self.hm.HookKeyboard()
	self.hm.KeyDown = self.OnKeyDownEvent
	self.disp = Display()
	
	self.RETURNFILE = os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0] + '/enter.wav'
	self.BACK = os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0] + '/backspace.wav'
	self.SPACE = os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0] + '/spacebar.wav'
	self.SHFT = os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0] + '/shift.wav'
	self.TABULATOR = os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0] + '/tab.wav'
	
	self.putanja = os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0] + "/sounds/"
	
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
	
    def spawn_event_threads(self):
	self.event_threads = {}
	self.queues = {}
	
    def start(self):
	if os.name == 'nt':
	    pythoncom.PumpMessages()
	if os.name == 'posix':
	    #self.hashchecker.start()
	    self.hm.start()

    def OnKeyDownEvent(self, event):
	#self.ControlKeyHash.update(event)
	
	self.keymap = self.disp.query_keymap()
	if self.keymap not in self.ignorelist:
	    self.x = random.choice(os.listdir(self.putanja))
	    self.zvuk = os.path.join(self.putanja, self.x)
	    self.KEYPRESSFILE = self.zvuk
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
	    subprocess.Popen(['aplay', self.filename], stderr=open('/dev/null', 'w'))
	    #print self.keymap #uncomment this line to print keycode for each key
	    
    def stop(self):
	if os.name == 'posix':
	    self.hm.cancel()
	    #self.hashchecker.cancel()
	    sys.exit()
	
if __name__== '__main__':
    tw = TypeWritter()
    tw.start()