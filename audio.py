# import sounddevice as sd
# import wavio
# import speech_recognition as sr
import streamlit as st
# def record_voice():
#     st.sidebar.write("Recording...")
#     st.sidebar.write("Please speak your Username")
    # duration = 3  # seconds
    # fs = 48000
    # sd.default.samplerate = fs
    # sd.default.channels = 1
    # myrecording = sd.rec(int(duration * fs))
    # sd.wait(duration)
    # print("Saving sample as myvoice.mp3")
    # path_myrecording = "./sample/myvoice.mp3"
    # wavio.write(path_myrecording, myrecording, fs, sampwidth=2)
#     print(myrecording)
    # sd.play(myrecording, fs)


# record_voice()
# r = sr.Recognizer()

# audio_file = sr.AudioFile("./sample/myvoice.mp3")

# with audio_file as source:
#     audio = r.record(source)
#     text = r.recognize_google(audio)

import azure.cognitiveservices.speech as speechsdk
import os
SPEECH_KEY='61c1cb532a1048939af075b5b98b44d1'
SPEECH_REGION ='eastus'


def tesp(text):
    speech_config1 = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION )
    audio_config1 = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    speech_config1.speech_synthesis_voice_name='en-IN-NeerjaNeural'
    speech_synthesizer1 = speechsdk.SpeechSynthesizer(speech_config=speech_config1, audio_config=audio_config1)
    speech_synthesis_result = speech_synthesizer1.speak_text_async(text).get()



def sptex():
    speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    result = speech_recognizer.recognize_once()
    return result.text


task = st.sidebar.selectbox("Menu",["Login"])
if task == "Login":
	st.write("recording...")
	# st.write(sptex())
	username = st.text_input(value = sptex(),label ="User Name")
	password = st.text_input("Password",type='password')
	
