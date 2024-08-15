import pyttsx3

if __name__ == '__main__':
    while True:
        x = input("Enter a string:")
        if x == 'q':
            break
            
        engine = pyttsx3.init()
        engine.say(x)
        engine.runAndWait()
