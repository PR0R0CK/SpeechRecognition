import speech_recognition as sr

# print(sr.__version__)
r = sr.Recognizer()
harvard = sr.AudioFile('harvard.wav')
speech_and_hammer = sr.AudioFile('jackhammer.wav')


# capturing data from file
def capture_data():
    with harvard as source:
        print('Listens...')
        audio = r.record(source)
    print(r.recognize_google(audio))


# capturing data from file with duration
def capture_data_with_duration():
    with harvard as source:
        print('Listens...')
        audio1 = r.record(source, duration=4)
        audio2 = r.record(source, duration=4)
    print(r.recognize_google(audio1))
    print(r.recognize_google(audio2))


# capturing data from file with duration and offset
# 4 means 4th second
def capture_data_with_duration_and_offset():
    with harvard as source:
        print('Listens...')
        audio = r.record(source, duration=4, offset=4)
    print(r.recognize_google(audio))


# effect of noise
def noise():
    with speech_and_hammer as source:
        print('Listens...')
        audio = r.record(source)
    print(r.recognize_google(audio))
# wrong translating "the snail smelly old gear vendors"


# dealing with noise
def noise_adjusted():
    with speech_and_hammer as source:
        r.adjust_for_ambient_noise(source)
        print('Listens...')
        audio = r.record(source)
    print(r.recognize_google(audio))
# closer to the original - "the" is missing


# dealing with noise with lowering duration from 1 (default) to 0.5
def noise_adjusted_with_more_samples():
    with speech_and_hammer as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print('Listens...')
        audio = r.record(source)
    # showing many possible transcriptions
    print(r.recognize_google(audio, show_all=True))


def main():
    capture_data()
    # capture_data_with_duration()
    # capture_data_with_duration_and_offset()
    # noise()
    # noise_adjusted_with_more_samples()


if __name__ == '__main__':
    main()
