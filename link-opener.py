import webbrowser

text = open(r"path\to\your'file", "r")
text.read()

for link in text:
	web  = webbrowser.open("link")
