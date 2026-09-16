import random
import time

def eightball():
    try: 
        s = input('=== 8Ball Machine - Credits to @JustPixel\nWhat do you wish to do?\n1) Play the 8Ball game\n2) Exit\n> ')
        if s == "1":
            n = input('What do you wish your username to be?\n> ')
            try:
                while True:
                    g = input(f'{n} > ')
                    if g == "exit":
                        print("\nBye!")
                        exit()
                    responses = [
                        "Yes",
                        "YEAHHH",
                        "FOR SURE",
                        "YESSIRRR",
                        "YEAHHHH * yeah",
                        "SURE",
                        "f5",
                        "fs",
                        "yeah lowk yeah",
                        "No",
                        "NOPE",
                        "hell nah",
                        "HELL NAHH BROTHA",
                        "no",
                        "nah gng",
                        "nah man",
                        "nuh uh",
                        "yeah, no",
                        "idk gng",
                        "idfk go ask sm1 else",
                        "i aint AI bruh"
                    ]
                    if g == "exit":
                        exit()
                    result = random.choice(responses)
                    print(f'question: {g}\nanswer: {result}')
            except Exception as e:
                print(f"error: {e}")
                return
        elif s == "2":
            l = input('are you sure? (y/n)\n> ')
            time.sleep(1)
            if l == "y":
                print("\nbye!")
                exit()
        else:
            print("invalid input")
            return
    except KeyboardInterrupt:
        print("Bye!")
        exit()
        

eightball()
