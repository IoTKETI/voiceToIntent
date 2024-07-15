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
from dataTransf_cc import transform_data_cc
from paho.mqtt import client as mqtt_client

client_wit = Wit('2I6HTQYEDPTZ2QE7VFVX7H4H2WMEITPW')

# mqtt setting
broker = '192.168.0.2'
port = 1883
client = mqtt_client.Client()
client.connect(broker, port)
client.loop_start()

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

# speak("KRM 에게 명령을 내리세요.")
playsound.playsound('voice_greeting.mp3')

while True:
    text = get_audio()
    
    if not text:
        continue  # If no text was recognized, skip the loop and wait for the next input

    if "종료" in text:
        break

    resp = client_wit.message(text)
    # print(resp["intents"][0]["name"])
    
    # 예외처리
    # intent 추출 실패 시 
    if resp["intents"] ==[]: # intent 추출 실패 시
        # speak("추출실패, 다시 말씀해 주세요")
        playsound.playsound('voice_case1.mp3')
        continue
    # intent 가 stand, standby, sit 중 하나 일 경우
    elif resp["intents"][0]["name"] == "stand" or resp["intents"][0]["name"] == "ready" or resp["intents"][0]["name"] == "sit": 
        # speak("메세지 전송 성공")
        playsound.playsound('voice_case2.mp3')
        intentResult=transform_data(resp)
        intentResult_json=json.dumps(intentResult, indent=4, ensure_ascii=False)
        print(intentResult_json)
        # intentCC=transform_data_cc(intentResult)
        # intentCC_json=json.dumps(intentCC, indent=4, ensure_ascii=False)
        # print(intentCC_json)

        # client.publish("/INTENT_CREATED/KETI_GCS",intentResult_json)
        client.publish("/intent_created/KETI_GCS",intentResult_json)
        # time.sleep(1)
        # client.publish("/RAW_INTENT_CREATED/KETI_GCS",intentCC_json)
        
        continue
    else:
        # speak("KRM 명령어가 아닙니다. 다시 말씀해 주세요")
        playsound.playsound('voice_case3.mp3')

    # intentResult=transform_data(resp)
    # print(json.dumps(intentResult, indent=4, ensure_ascii=False))

    time.sleep(0.1)
