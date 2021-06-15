# Christian Medel (Elbullazul) 6/6/2021
# A class to keep useful global variables to avoid re-declaring them everywhere
# License: GPL v3

import os

class Constants():
	# Program globals
	appname = 'pudu'	# might change in the future, use var for dir and other 'changeable' references
	appversion = '0.0.1'  # very alpha

	# Path globals
	# TODO: find a way to persist the environment
	#homedir = os.getenv("HOME") + '/'
	homedir = '/home/elbullazul/'
	
	appdir = '/usr/share/applications/.'

	# File globals
	configfile = homedir + f".config/{appname}/{appname}.config"
	lockfile = homedir + f".config/{appname}/{appname}.lock"
	logfile = homedir + f".config/{appname}/{appname}.log"
