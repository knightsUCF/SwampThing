import pyttsx, time

class Talkamaton():
   
    def __init__(self):
        self.talkamaton = pyttsx.init()
    
    def Say(self, text):
        self.talkamaton.say(text)
        self.talkamaton.runAndWait()
