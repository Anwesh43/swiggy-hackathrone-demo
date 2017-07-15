from speech_recognition import *
from os import path
class SpeechRecognizer:
    def __init__(self):
        self.r = Recognizer()
    def recognize_file(self,filename):
        AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)),"sound/{0}".format(filename))
        print(AUDIO_FILE)
        with AudioFile(AUDIO_FILE) as source:
            audio = self.r.record(source)
        try:
            text = self.r.recognize_google(audio,langauge = "en-IN")
            print(text)
            return text
        except:
            print("error")
            return "error"
