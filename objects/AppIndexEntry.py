# Christian Medel (Elbullazul) 6/6/2021
# Models
# License: GPL v3

class AppIndexEntry():
		appIcon = ''
		appName = ''	# Don't forget to use translations manager!
		appCommand = ''
		appDescription = ''
		
		iconIdx = 0
		nameIdx = 1
		descIdx = 2
		cmdIdx = 3
		
		def __init__(self, icon, name, command, description):
			self.appIcon = icon
			self.appName = name
			self.appCommand = command
			self.appDescription = description
