import requests
from gtts import gTTS
import os
from speech_recognition import *
recognizer = Recognizer()
phno = 'xxab'
def start():
    r = requests.get('http://localhost:5000/request-speech/{0}'.format(phno))
    print(r.text)
    n =  int(r.text)
    startLoop(3)
def startLoop(n):
    i = 0
    while i < n:
        r = requests.get('http://localhost:5000/fetchQuestion/{0}/{1}'.format(phno,i))
        text = r.text
        print(text)
        tts = gTTS(text=text, lang='en')
        tts.save("resp.mp3")
        os.system("afplay resp.mp3")
        with Microphone() as source:
            audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(text)
            new_r = requests.get('http://localhost:5000/processText/{0}'.format(text))
            status = new_r.text
            if status == "success":
                i = i+1
        except:
            print("error")
    #print(type(json))
if __name__ == "__main__":
    start()
