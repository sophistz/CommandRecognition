import json

content = None
f = open('simDict.py')
content = f.read()

content = content.replace("'", '"')
data = json.loads(content)

f.close()
