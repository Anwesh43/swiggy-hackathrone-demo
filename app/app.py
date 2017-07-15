from flask import *
from .SpeechRecognizer import *
from nltk import *
serverApp = Flask(__name__)
questions = ["what is your location","which restaurant?","what you want to eat?"]
serverApp.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

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
    print(len(questions))
    return "{0}".format(len(questions))

@serverApp.route("/processText/<text>")
def processText(text):
    # stopwords 
    stopwords = set(('location', 'locality', 'place', 'home', 'area', 'place','abode','street',
                              'restaurant','hotel','eatery','brewrey','bar','joint','food','order'))
    sentence = word_tokenize(text)
    tags = pos_tag(sentence)
    keywords = []
    for tupple in tags:
        if "NN" in tupple[1] and tupple[0] not in stopwords:
            keywords.append(tupple[0])
        if "CD" in tupple[1]:
            keywords.append(tupple[0])
    print(keywords)
    return "success"

@serverApp.route("/fetchQuestion/<phoneno>/<index>")
def fetchQuestion(phoneno,index):
    if(int(index) < len(questions)):
        return questions[int(index)]
    return "placed your order"
