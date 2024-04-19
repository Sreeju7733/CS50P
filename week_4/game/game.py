import random

while True:
    try:
        #getting input fromu user
        level = int(input("Level: "))
        x = random.randint(1, level)

        while True:
            # getting input from user
            guess = int(input("Guess: "))
            if guess > x:
                print("Too large!")
            elif guess < x:
                print("Too small!")
            elif guess == x:
                print("Just right!")
                raise EOFError

    except ValueError:
        pass
    except EOFError:
        break
