import sys
import pyttsx3 as ttx
import speech_recognition as sr
import pywhatkit
import datetime
import random
import pyaudio

listener = sr.Recognizer()
engine = ttx.init()
voice = engine.getProperty('voices')
engine.setProperty('voice','french')

#fonction qui permet a l'assisstant de parler (transformer les textes en parole)
def talk(text):
 engine.say(text)
 engine.runAndWait()

#permet de saluer en fonction de l'heur actuelle
def greetme():
    current_hour = int(datetime.datetime.now().hour)
    if 0 <= current_hour < 12:
       talk("bonjour alpha")
    if 12 <= current_hour<18:
       talk("bonapré midi alpha")
    if current_hour >= 18 and current_hour != 0:
       talk("bonsoir alpha")

#set french male voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
greetme()
ouvertur_jarvis = ["en quoi je peux t'aider?", "t'as besoin de moi ?", "que puije faire pour toi ?",]
engine.say(random.choice(ouvertur_jarvis))
engine.runAndWait()

#consiste a passer la commande vocale a jarvis
def jarvis_command():
  with sr.Microphone()as source:
    print("parlez maintenant...")
    listener.pause_threshold = 5
    voice = listener.listen(source)
    command = listener.recognize_google(voice, language="fr-FR")
    command = command.lower()
    print(command)
    if 'jarvis' in command:
      command = command.replace('jarvis', '')
      print (command)
  return command

def run_jarvis():
  command = jarvis_command()
  if 'musique' in command:
    song = command.replace('musique', '')
    talk("musique en cours de recherche...")
    pywhatkit.playonyt(song)
  elif "comment tu t'appelle" in command:
      talk("je m'appelle jarvis")
  elif 'ton nom' in command:
      talk("mon nom est jarvis")
  elif 'heure' in command:
    time = datetime.datetime.now().strftime('%H"heure":%M')
    print(time)
    talk("il é actuelement:"+time)
  elif "aujourd'hui" in command:
    day = datetime.datetime.today().weekday()+1
    day_dict = {1:'lundi', 2:'mardi', 3:'mercredi', 4:'jeudi', 5:'vendredi', 6:'samedi', 7:'dimanche'}
    jours=day_dict[day]
    print(jours)
    talk("aujourd'hui c'est:"+jours)
  elif 'sortir avec moi' in command:
    talk("non je suis deja en couple")
  elif 'tu sors avec qui' in command:
    talk("je sort avec siri de apeul")
  elif 'créé' in command:
    tfq = ["mon créateur est alpha kays", " jé été créé par alpha kays","alpha kays", "c'est alpha kays qui m'a creer"]
    talk(random.choice(tfq))
  elif 'désactive toi' in command:
      talk("bye et a plus tard")
      sys.exit()
  else:
    talk("j'ai pas bien capter,tu peux repeté?")

while True:
 run_jarvis()
