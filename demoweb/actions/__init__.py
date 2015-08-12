

urls = []

def add_action(urlStr,actionName):
	actionName = "actions." + actionName + ".main"
	urls.extend([urlStr,actionName])

add_action('/','index')
add_action('/login','login')
add_action('/livelong','livelong')
