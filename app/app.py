from flask import *
from .SpeechRecognizer import *
from nltk import *
from flask import jsonify
import requests
serverApp = Flask(__name__)
questions = ["what is your location?","which restaurant?","what you want to eat?"]
##questions = ["How "]
endPointURI = "http://172.16.120.165/swiggyHackathrone/db.php"
endPoints = ["?option=Locality&data=","?option=Restaurant&data=","?option=Food&data="]
serverApp.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
serverApp.debug = True
recognizer = SpeechRecognizer()
@serverApp.route('/test')
def test():
    print(__file__)
    return "test response"

@serverApp.route("/getTextFromSpeech/<filename>")
def getTextFromSpeech(filename):
    print(filename)
    return recognizer.recognize_file(filename)

@serverApp.route("/request-speech/<phoneno>")
def requestSpeechApi(phoneno):
    session[phoneno] = 0
    print(session[phoneno])
    print(len(questions))
    return "{0}".format(len(questions))

@serverApp.route("/processText/<int:i>/<text>")
def processText(i,text):
    # stopwords
    print(session.keys())
    stopwords = set(('location', 'locality', 'place', 'home', 'area', 'place','abode','street',
                              'restaurant','hotel','eatery','brewrey','bar','joint','food','order'))
    sentence = word_tokenize(text)
    tags = pos_tag(sentence)
    print(tags)
    dictionary = {"NN":[],"CD":[]}
    for tupple in tags:
        print(tupple[1])
        print(tupple[1][0:2])
        if (tupple[1][0:2] in dictionary) and (tupple[0] not in stopwords):
            dictionary[tupple[1][0:2]].append(tupple[0])
    print(dictionary)
    if len(dictionary['NN']) == 0:
        return "error"
    n = len(dictionary['NN'])-1
    token = " ".join(dictionary['NN'])
    new_end_point = '{0}{1}{2}'.format(endPointURI,endPoints[i],token)
    print(new_end_point)
    resp = requests.get(new_end_point)
    data = resp.json()
    print(data)
    return jsonify({"status":"success","data":data,"orig_text":token})

@serverApp.route("/fetchQuestion/<phoneno>/<index>")
def fetchQuestion(phoneno,index):
    if(int(index) < len(questions)):
        return questions[int(index)]
    return "placed your order"
