from flask import *
from .SpeechRecognizer import *
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
    print(text)
    return "success"

@serverApp.route("/fetchQuestion/<phoneno>/<index>")
def fetchQuestion(phoneno,index):
    if(int(index) < len(questions)):
        return questions[int(index)]
    return "placed your order"
