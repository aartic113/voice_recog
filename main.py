import pyttsx3 as p
import speech_recognition as sr 
import datetime
import randfacts


from selenium_web import * 
from yt_audio import *
from news import *
from jokes import *
from weather import *


engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
# print(voices)


def speak(text):
	engine.say(text)
	engine.runAndWait()


def wishme():
	hour = int(datetime.datetime.now().hour)
	if hour > 0 and hour < 12:
		return("morning")
	elif hour >= 12 and hour < 16:
		return("afternoon")
	else:
		return("evening")


today_date = datetime.datetime.now()
r = sr.Recognizer()


speak("hello mam," + "good " + wishme() + " i am your voice assistant.")
speak("today is " + today_date.strftime("%d") + " of " + today_date.strftime("%B") + ", And its currently " + (today_date.strftime("%I")) + (today_date.strftime("%M")) + (today_date.strftime("%p")))
speak("Temperature in London is " + str(temp()) + "degree celcius" + " and with " + str(des()))
speak("what can i do for you?")


# with sr.Microphone() as source:
# 	r.energy_threshold  = 10000
# 	r.adjust_for_ambient_noise(source,1.2)
# 	print("listening")
# 	audio = r.listen(source)
# 	text=r.recognize_google(audio)
# 	print(text)

# if "what" and "about" and "you" in text:
# 	speak("i am also having a good day mam")
# 	speak("what can i do for you?")


with sr.Microphone() as source:
	r.energy_threshold  = 10000
	r.adjust_for_ambient_noise(source,1.2)
	print("listening...")
	audio = r.listen(source)
	text2=r.recognize_google(audio)
	print(text2)

if "information" in text2:
	speak("you need information related to which topics?")


	with sr.Microphone() as source:
		r.energy_threshold  = 10000
		r.adjust_for_ambient_noise(source,1.2)
		print("listening...")
		audio = r.listen(source)
		infor=r.recognize_google(audio)

	speak("searching {} in wikipedia".format(infor))
	print("searching {} in wikipedia".format(infor))
	assist = infow()
	assist.get_info(infor)


elif "video" in text2:
	speak("you want me to play which video?")

	with sr.Microphone() as source:
		r.energy_threshold  = 10000
		r.adjust_for_ambient_noise(source,1.2)
		print("listening...")
		audio = r.listen(source)
		vid=r.recognize_google(audio)
		speak("Playing {} on youtube".format(vid))
		print("Playing {} on youtube".format(vid))
		assist = music()
		assist.play(vid)


elif "news" in text2:
	speak("Sure mam, Now I will read the news for you.")
	arr = news()
	for i in range(len(arr)):
		print(arr[i])
		speak(arr[i])


elif "joke" in text2:
	speak("Sure mam, get ready for some chuckles")
	jokes = joke()
	print(jokes[0])
	speak(jokes[0])
	print(jokes[1])
	speak(jokes[1])



elif "fact" in text2:
	speak("Sure mam")
	x = randfacts.get_fact()
	# print(x)
	speak("Did you know that, " + x)

