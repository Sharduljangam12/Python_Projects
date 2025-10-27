# Task 1: Build a simple CLI script to convert user input text to speech
import pyttsx3

'''
input("Enter the Text you want to hear:- ")
#pyttsx3.speak("I will speak this text")
engine = pyttsx3.init()
#engine.say('Sally sells seashells by the seashore.')
engine.say(input())
#engine.say('The quick brown fox jumped over the lazy dog.')

engine.runAndWait()'''
def main():
    engine = pyttsx3.init()
    print("Welcome to Tell-Me application")
    print("This Application will read all the books/Articles/Notes or Anything else you want to read it can read it for you")
    text = input("Enter the text you want to hear: ")
    engine.say(text)
    engine.runAndWait()

    print("Thank you for Using Tell Me")

if __name__ == "__main__":
    main()

