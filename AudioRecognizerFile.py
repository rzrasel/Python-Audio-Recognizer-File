import speech_recognition as sr

r = sr.Recognizer()

audio = 'English.wav'
# audio = 'Bangla.wav'

with sr.AudioFile(audio) as source:
    audio = r.record(source)
    print ('Done!')

try:
    # text = r.recognize_google(audio)
    # text = r.recognize_google(audio, language="bn-BN")
    text = r.recognize_google(audio, language="en-EN")
    print (text)

except Exception as e:
    print (e)
