import requests
from gtts import gTTS
import os
from speech_recognition import *
recognizer = Recognizer()
phno = 'xxab'
items = ['Restaurant','FoodItem','ItemId']
greets = ['Here are the top restaurants for you','Here is the menu']
order = {}
def start():
    r = requests.get('http://localhost:5000/request-speech/{0}'.format(phno))
    print(r.text)
    n =  int(r.text)
    startLoop(3)
def speak(text,file_name):
    tts = gTTS(text=text, lang='hi')
    tts.save(file_name)
    os.system("afplay {0}".format(file_name))
def startLoop(n):
    i = 0
    while i < n:
        r = requests.get('http://localhost:5000/fetchQuestion/{0}/{1}'.format(phno,i))
        text = r.text
        print(text)
        speak(text,"resp_{0}_{1}.mp3".format(phno,i))
        with Microphone() as source:
            audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(text)
            new_r = requests.get('http://localhost:5000/processText/{1}/{0}'.format(text,i))
            resp = new_r.json()
            print(resp)
            if resp["status"] == "success":
                print("success")
                if not(i == n-1):
                    speak('{0} in {1}'.format(greets[i],text),"greet_{0}.mp3".format(i))
                    for data in resp["data"]:
                        print(data[items[i]])
                        speak(data[items[i]],"{0}.mp3".format(data[items[i]].replace(' ','_')))
                i = i+1

        except:
            print("error")
    if i == n:
        r = requests.post('http://localhost:9000/postorder',data={"name":"order1","price":100})
        print(r.text)
    #print(type(json))
if __name__ == "__main__":
    start()
