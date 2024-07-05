import speech_recognition as sr
from gtts import gTTS
import os
import playsound
import time
from wit import Wit
import json

client = Wit('2I6HTQYEDPTZ2QE7VFVX7H4H2WMEITPW')

def speak(text):
    tts=gTTS(text=text, lang='ko')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def get_audio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("지금 듣고 있어요: ")
        audio = r.listen(source)
        said = " "

        try:
            said = r.recognize_google(audio, language='ko-KR')
            print("말씀하신 내용입니다." , said)
        except Exception as e:
            pass
            print("exception: "+ str(e))
    return said

if os.path.isfile('memo.txt'):
    os.remove('memo.txt')

speak("안녕하세요, 안내방송입니다. ")

while True:
    text = get_audio()
    
    if "종료" in text:
        break

    resp = client.message(text)
    print(json.dumps(resp, indent=4, ensure_ascii=False))

    time.sleep(0.1)