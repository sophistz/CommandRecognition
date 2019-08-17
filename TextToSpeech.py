import pyttsx3
engine = pyttsx3.init()
print(engine.getProperty('voice'))
engine.setProperty('rate', 140)
