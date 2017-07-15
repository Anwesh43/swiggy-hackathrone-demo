from flask import *
from .SpeechRecognizer import *
serverApp = Flask(__name__)
recognizer = SpeechRecognizer()
@serverApp.route('/test')
def test():
    print(__file__)
    return "test response"

@serverApp.route("/getTextFromSpeech/<filename>")
def getTextFromSpeech(filename):
    print(filename)
    return recognizer.recognize_file(filename)
