import pyttsx3
engine = pyttsx3.init()
q = open("rick", 'r')
f = open("beemovie", 'r')
for word in q:
    engine.say(word)
engine.runAndWait()
for word in f:
    engine.say(word)
engine.runAndWait()
