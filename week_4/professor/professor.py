import random


def main():
    questions = 10
    score = 0
    chances = 3
    level = get_level()
    while questions != 0:
        if chances == 3:
            x, y = generate_integer(level)
        try:
            user_answer = int(input(f"{x} + {y} = "))
            answer = x + y
            if user_answer == answer:
                questions = questions - 1
                score = score + 1
                chances = 3
                continue
            else:
                raise ValueError
        except (ValueError, NameError):
            print("EEE")
            chances = chances - 1
            pass
        if chances == 0:
            print((f"{x} + {y} = {answer}"))
            chances = 3
            questions = questions - 1
            continue
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            # getting input from user
            user_input = int(input("Level: "))
            if 1 <= user_input <= 3:
                return user_input
        except:
            pass


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y


if __name__ == "__main__":
    main()
