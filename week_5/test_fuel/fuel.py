def main():
    user_input = input("Fraction: ")
    converted_percentage = convert(user_input)
    gauge_result = gauge(converted_percentage)
    print(gauge_result)


def convert(fraction):
    fraction = fraction.split("/")
    x = int(fraction[0])
    y = int(fraction[1])

    if x > y:
        raise ValueError
    elif y == 0:
        raise ZeroDivisionError

    return round((x / y) * 100)

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
