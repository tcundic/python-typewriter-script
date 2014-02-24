#!/usr/bin/env python 

import wx
import os.path
import sys

TRAY_TOOLTIP = 'Typewriter application'
TRAY_ICON = os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0] + '/icon.gif'

class TaskBarIcon(wx.TaskBarIcon):
	def __init__(self, frame):
		wx.TaskBarIcon.__init__(self)

		self.frame = frame
		self.SetIcon(wx.IconFromBitmap(wx.Bitmap(TRAY_ICON)), TRAY_TOOLTIP)
		self.Bind(wx.EVT_MENU, self.OnTaskBarMute, id=1)
		self.Bind(wx.EVT_MENU, self.OnTaskBarUnmute, id=2)
		self.Bind(wx.EVT_MENU, self.OnTaskBarClose, id=3)
		self.Mute = False
		text_file = open(os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0] + "/mute.dat", "w")
		text_file.write("False")
		text_file.close()

	def CreatePopupMenu(self):
		menu = wx.Menu()
		menu.Append(1, 'Mute')
		menu.Append(2, 'Unmute')
		menu.Append(3, 'Exit')
		return menu

	def OnTaskBarClose(self, event):
		self.frame.Close()

	def OnTaskBarMute(self, event):
		self.mute = True
		text_file = open(os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0] + "/mute.dat", "w")
		text_file.write("True")
		text_file.close()

	def OnTaskBarUnmute(self, event):
		self.mute = False
		text_file = open(os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0] + "/mute.dat", "w")
		text_file.write("False")
		text_file.close()

class TypewriterTray(wx.Frame):
	def __init__(self, parent, id, title):
		wx.Frame.__init__(self, parent, id, title, (-1, -1), (290, 280))

		self.tray = TaskBarIcon(self)
		self.Centre()
		self.Bind(wx.EVT_CLOSE, self.OnClose)

	def OnClose(self, event):
		text_file = open(os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0] + "/mute.dat", "w")
		text_file.write("Exit")
		text_file.close()
		self.tray.Destroy()
		self.Destroy()

class Tray(wx.App):
	def OnInit(self):
		frame = TypewriterTray(None, -1, 'Typewriter')
		frame.Show(False)
		self.SetTopWindow(frame)
		return True

app = Tray(0)
app.MainLoop()