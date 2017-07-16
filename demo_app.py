import requests
from gtts import gTTS
import os
import difflib
from speech_recognition import *
recognizer = Recognizer()
phno = 'xxab'
items = ['Restaurant','FoodItem','ItemId']
greets = ['Here are the top restaurants for you','Here is the list of trending food items']
orderItems = ['Restaurant_id','ItemId']
valItems = ['Restaurant_id','item_id']
prevItemDictionary = {}
orderDictionary = {}
orderJSONItems = ["place","restaurant","food_item","cost"]
orderJSON = {}
def start():
    r = requests.get('http://localhost:5000/request-speech/{0}'.format(phno))
    print(r.text)
    n =  int(r.text)
    startLoop(n)
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
            prev_menus = prevItemDictionary.keys()
            if len(prev_menus) > 0:
                matches = difflib.get_close_matches(text,prev_menus)
                if len(matches) == 1:
                    text = matches[0]
            new_r = requests.get('http://localhost:5000/processText/{1}/{0}'.format(text,i))
            resp = new_r.json()
            print(resp)
            if resp["status"] == "success":
                key_text = text
                for key in prevItemDictionary.keys():
                    if key.replace(' ','').lower() in key_text.replace(' ','').lower():
                        key_text = key
                        print('key text is {0}'.format(key_text))

                if key_text in prevItemDictionary:
                    orderDictionary[valItems[i-1]] = prevItemDictionary[key_text]

                print("success")
                orderJSON[orderJSONItems[i]] = resp["orig_text"]
                if not(i == n-1):
                    speak('{0} in {1}'.format(greets[i],resp["orig_text"]),"greet_{0}.mp3".format(i))
                    for data in resp["data"]:
                        print(data[items[i]])
                        speak(data[items[i]],"{0}.mp3".format(data[items[i]].replace(' ','_')))
                        prevItemDictionary[data[items[i]]] = data[orderItems[i]]

                else:
                    print(orderDictionary)
                    cost = float(resp["data"])
                    orderJSON[orderJSONItems[i+1]] = cost
                i = i+1

        except Exception as e:
            print(e)
            print("error")
    if i == n:
        print(orderJSON)
        post_order = requests.post('http://172.16.120.165/swiggyHackathrone/db.php?option=ConfirmOrder',data=orderDictionary)
        post_order_text = (post_order.text)
        res = requests.post('http://localhost:9000/postorder',data=orderJSON)
        print(res.text)
    #print(type(json))
if __name__ == "__main__":
    start()
