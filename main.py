# Christian Medel (Elbullazul) 6/6/2021
# The background service of the Pudu desktop environment
# License: GPL v3

# see if imports can be reduced/reimplemented
import os

from objects.Constants import Constants
from managers.AppIndexManager import AppIndexManager

# TODO: think of a better class name...
class root_process():
	keybindManager = None
	appIndexManager = None

	def __init__(self):
		appIndexManager = AppIndexManager(self)

	def launch(self):
		# launch each sub-process and have them share the resources via this class
		# 
		print(f"{Constants.appname} is starting...")

	# instantiate child processes
		# panel (does menu count as taskbar???)
			# secondary panel
		# menu
		# launcher (necessary?)
		
	# bind itself as parent for children apps
	# launch background service

# when children require some "centralized" functionality, call the object from parent instead of re-creating a copy/relaunching a service

# TODO: move to an appropriate object/manager file once finished
root_process = root_process()
root_process.launch()
