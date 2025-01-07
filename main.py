
import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.AudioFile('converted_audio.wav') as source:
    audio = recognizer.record(source)
print(recognizer.recognize_google(audio, language="pt-BR"))
