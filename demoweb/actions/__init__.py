

urls = []

def add_action(urlStr,actionName):
	urls.append(urlStr)
	urls.append("actions." + actionName + ".main")

add_action('/','index')
add_action('/login','login')
