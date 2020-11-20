import speech_recognition as sr

import random
import time

# print(sr.__version__)
r = sr.Recognizer()


def recognize_speech_from_mic(recognizer, microphone):
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjusting the recognizer sensivity to ambient noise from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # trying to recognize the speech from the microphone
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # when API doesn't respond
        response["success"] = False
        response["error"] = "API doesn't respond!"
    except sr.UnknownValueError:
        # when speech was unintelligible
        response["error"] = "Cannot recognize the speech!"
    return response


def main():
    # list of words, max. nmbr of guesses, prompt limit
    WORDS = ["apple", "banana", "grape", "orange", "mango", "lemon"]
    NUM_GUESSES = 3
    PROMPT_LIMIT = 5

    # create recognizer and and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # getting a random word from the list
    word = random.choice(WORDS)


    # format the instructions string
    instructions = (
        "I'm thinking of one of these words:\n"
        "{words}\n"
        "You have {n} tries to guess which one.\n"
    ).format(words=', '.join(WORDS), n=NUM_GUESSES)

    # show instructions and wait 3 seconds before starting the game
    print(instructions)
    time.sleep(3)

    for i in range(NUM_GUESSES):
        # get the guess from the user
        # if a transcription is returned, break out of the loop and
        #     continue
        # if no transcription returned and API request failed, break
        #     loop and continue
        # if API request succeeded but no transcription was returned,
        #     re-prompt the user to say their guess again. Do this up
        #     to PROMPT_LIMIT times
        for j in range(PROMPT_LIMIT):
            print("Guess {}. Speak now!".format(i+1))
            guess = recognize_speech_from_mic(recognizer, microphone)
            print("You said: ", guess["transcription"])
            if guess["transcription"]:
                break
            if not guess["success"]:
                break
            print("I didn't catch that. What did you say?\n")
            # if there was an error - stop the game
        if guess["error"]:
            print("ERROR: {}".format(guess["transcription"]))
            # determine if guess is correct and if any attempts remain
        guess_is_correct = guess["transcription"].lower() == word.lower()
        user_has_more_attempts = i < NUM_GUESSES - 1

        # determine if the user has won the game
        # if not, repeat the loop if user has more attempts
        # if no attempts left, the user loses the game
        if guess_is_correct:
            print("Correct! You won!".format(word))
            break
        elif user_has_more_attempts:
            print("Incorrect! Try again.\n")
        else:
            print("Sorry, you lose.\nI was thinking of '{}'.".format(word))
            break


if __name__ == '__main__':
    main()
