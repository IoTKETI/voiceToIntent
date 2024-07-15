import pygame
import speech_recognition as sr
from gtts import gTTS
import os
import playsound
import time
import json
from wit import Wit
from dataTransf import transform_data
from dataTransf_cc import transform_data_cc
from paho.mqtt import client as mqtt_client

# Wit.ai API access token
client_wit = Wit('2I6HTQYEDPTZ2QE7VFVX7H4H2WMEITPW')

# # MQTT broker settings
# broker = '192.168.0.2'
# port = 1883
# client = mqtt_client.Client()
# client.connect(broker, port)
# client.loop_start()

text =''
toggle_state = False

# Initialize Pygame and joystick module
pygame.init()
pygame.joystick.init()

# Create list to store connected joysticks
joysticks = []
for i in range(pygame.joystick.get_count()):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()
    joysticks.append(joystick)

# Function to speak text using gTTS
def speak(text):
    tts = gTTS(text=text, lang='ko')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

# Function to get audio input using speech_recognition
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio, language='ko-KR')
            print("You said:", said)
        except Exception as e:
            print("Exception:", str(e))

    return said

# Initial greeting
# playsound.playsound('voice_greeting.mp3')
speak("A 버튼을 누르고 KRM 에게 명령을 내리세요")

# Game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Check joystick button presses
        if event.type == pygame.JOYBUTTONDOWN:
            for joystick in joysticks:
                if event.joy == joystick.get_id():
                    if joystick.get_button(0):  # Adjust button index as needed
                        print("Button 0 pressed. Listening for audio...")
                        text = get_audio()
                        if not text:
                            continue  # If no text was recognized, skip the loop and wait for the next input

                        if "종료" in text: 
                            run = False
                            break

                        resp = client_wit.message(text)

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
                            # client.publish("/intent_created/KETI_GCS",intentResult_json)
                            continue
                        else:
                            # speak("KRM 명령어가 아닙니다. 다시 말씀해 주세요")
                            playsound.playsound('voice_case3.mp3')
        
# Quit Pygame
pygame.quit()
