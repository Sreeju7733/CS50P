while True:
    try:
        # getting input from the user
        user_input = input("Fraction: ").split("/")
        x = int(user_input[0])
        y = int(user_input[1])
        if x > y:
            user_input = input("Fraction: ").split("/")
            x = int(user_input[0])
            y = int(user_input[1])
        result = x / y
        break
    except (ValueError, ZeroDivisionError):
        pass

percentage = int(round(result * 100))

if percentage >= 99:
    print("F")
elif percentage <= 1:
    print("E")
else:
    print(f"{percentage}%")
