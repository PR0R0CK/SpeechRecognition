import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()


# listening
def listening():
    with mic as source:
        print('Say something...')
        audio = r.listen(source)

    print(r.recognize_google(audio))


# listening with adjusting noises
def listening_with_noises():
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print('Say something...')
        audio = r.listen(source)
    print(r.recognize_google(audio))


def main():
    listening()
    # listening_with_noises()


if __name__ == '__main__':
    main()
