# ready untill speaking
# add exception process

import speech_recognition as sr
from gtts import gTTS
import os
import playsound
import time
from wit import Wit
import json
from dataTransf import transform_data

client = Wit('2I6HTQYEDPTZ2QE7VFVX7H4H2WMEITPW')

def speak(text):
    tts = gTTS(text=text, lang='ko')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("지금 듣고 있어요: ")
        audio = r.listen(source)  # No timeout or phrase_time_limit
        said = ""

        try:
            said = r.recognize_google(audio, language='ko-KR')
            print("말씀하신 내용입니다.", said)
        except Exception as e:
            print("exception: 대기" + str(e))
    return said

speak("KRM 에게 명령을 내리세요.")

while True:
    text = get_audio()
    
    if not text:
        continue  # If no text was recognized, skip the loop and wait for the next input

    if "종료" in text:
        break

    resp = client.message(text)
    
    # 예외처리
    # intent 추출 실패 시 
    if resp["intents"] ==[]: # intent 추출 실패 시 
        continue
    # intent 가 stand, standby, sit 중 하나가 아닐 경우
    elif resp["intents"][0]["name"] != "stand" or resp["intents"][0]["name"] != "standby" or resp["intents"][0]["name"] != "sit": 
        continue

    intentResult=transform_data(resp)
    
    print(json.dumps(intentResult, indent=4, ensure_ascii=False))

    time.sleep(0.1)
