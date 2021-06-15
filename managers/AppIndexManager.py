# Christian Medel (Elbullazul) 6/6/2021
# A class to keep an up-to-date index of available desktop apps in a system
# License: GPL v3

# see if imports can be reduced/reimplemented
import os, gi

# Global variables
from objects.Constants import Constants
from objects.AppIndexEntry import AppIndexEntry


# Import PyGTK
gi.require_version('Gtk', '3.0')
from gi.repository import Gio

class AppIndexManager():
	parentDaemon = None
	appListener = None		# GDK app directory listener (for software changes)
	index = []
	
	def __init__(self, process):
		parentProcess = process
		appListener = Gio.File.new_for_path(Constants.appdir)
			
	# TODO: There has to be a better way to get installed app info
	def parseAppFile(self, file):
		appInfo = []
		icon = name = desc = cmd = ''
		
		buffer = open(Constants.appdir + '/' + file, "r")
		
		# Is it OK to load info here? Maybe it's better in the AppIndexEntry class...
		for line in buffer:
			if line.startswith("Icon="):
				icon = line[5:].rstrip()
			if line.startswith("Name="):
				name = line[5:].rstrip()
			if line.startswith("Comment="):
				desc = line[8:].rstrip()
			if line.startswith("Exec="):
				cmd = line[5:].rstrip().lower()
				cmd = cmd.replace("%u","")
				cmd = cmd.replace("%f","")

		appInfo.append(icon)
		appInfo.append(name)
		appInfo.append(desc)
		appInfo.append(cmd)		
		
		return appInfo
	
	# TODO: check if command exists instead of check 'false'
	def validateEntry(self, appInfo):
		isValid = True
		
		appCmd = appInfo[AppIndexEntry.cmdIdx]
		appName = appInfo[AppIndexEntry.nameIdx]
		
		# Filter unlaunchable entries
		if 'false' in appCmd:
			isValid = False
		elif appName == "":
			isValid = False
		
		return isValid
		
	# NOTE: Maybe we can package info better? Also, implement categories in the future
	def buildIndexEntry(self, index, appInfo):
		entry = AppIndexEntry(
			appInfo[AppIndexEntry.iconIdx],
			appInfo[AppIndexEntry.nameIdx],
			appInfo[AppIndexEntry.cmdIdx],
			appInfo[AppIndexEntry.descIdx]
		)
		index.append(entry)

	# TODO: redo the app import method in a more standard way
	def buildIndex(self):
		appFiles = os.listdir(Constants.appdir)
		
		for appFile in appFiles:
			if os.path.isfile(os.path.join(Constants.appdir, appFile)):
				appInfo = self.parseAppFile(appFile)
				
				if self.validateEntry(appInfo):
					self.buildIndexEntry(self.index, appInfo)
	
	# TODO: rebuild index without flushing it?
	def updateIndex(self):
		# flush the current index for now
		index = []
		
		# rebuild it
		self.buildIndex()
	
	# TODO: can we see what exactly changed and just scan/purge those files?
	def appDirChanged(self):
		print("Dir has changed!")
	
	# EZ!
	def searchIndex(self, query):
		results = []
		
		for appEntry in index:
			if query in appEntry.name or query in appEntry.cmd:
				results.append(appEntry)
		
		return results
