import speech_recognition as sr

print(sr.__version__)
r = sr.Recognizer()
# r.recognize_google();


harvard = sr.AudioFile('harvard.wav')
with harvard as source:
    audio = r.record(source)
    type(audio)
r.recognize_google(audio)
