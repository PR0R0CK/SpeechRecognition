import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# write audio to a RAW file
with open("record.raw", "wb") as f:
    f.write(audio.get_raw_data())

# write audio to a WAV file
with open("record.wav", "wb") as f:
    f.write(audio.get_wav_data())

# write audio to an AIFF file
with open("record.aiff", "wb") as f:
    f.write(audio.get_aiff_data())

# write audio to a FLAC file
with open("record.flac", "wb") as f:
    f.write(audio.get_flac_data())