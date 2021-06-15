class ConfigManager():
	json = '{}'		# store config file as json
	
	def __init__(self, file):
		# new IO manager (OR the one inherited from parent)
		# IOManager selects file
		# wait?
		print("Getting config...")
	
	def getConfig(propertyName):
		return json.find(propertyName).value
	
	def setConfig(propertyName, value):
		json.find(propertyName).value = value
		
		persist()
	
	def persist():
		# save file
		return
