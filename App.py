import speech_recognition as sr

print(sr.__version__)
r = sr.Recognizer()
# r.recognize_google();


harvard = sr.AudioFile('harvard.wav')
## capturing data from file
# with harvard as source:
#     audio = r.record(source)
# type(audio)
# print(r.recognize_google(audio))

## capturing data from file with duration
# with harvard as source:
#     audio1 = r.record(source, duration=4)
#     audio2 = r.record(source, duration=4)
# print(r.recognize_google(audio1))
# print(r.recognize_google(audio2))

## capturing data from file with duration and offset
# with harvard as source:
#     audio = r.record(source, duration=4, offset=4)
# print(r.recognize_google(audio))

jackhammer = sr.AudioFile('jackhammer.wav')
## effect of noise
# with jackhammer as source:
#     audio = r.record(source)
# print(r.recognize_google(audio))
## wrong translating "the snail smelly old gear vendors"

## dealing with noise
# with jackhammer as source:
#     r.adjust_for_ambient_noise(source)
#     audio = r.record(source)
# print(r.recognize_google(audio))
## closer to the original - "the" is missing

## dealing with noise with lowering duration from 1 (default) to 0.5
# with jackhammer as source:
#     r.adjust_for_ambient_noise(source, duration=0.5)
#     audio = r.record(source)
# ## showing many possible transcriptions
# print(r.recognize_google(audio,show_all=True))