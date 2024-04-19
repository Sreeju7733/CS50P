def main():
    user_input = input("What time is it? ")
    user_time = convert(user_input)

    if 7 <= user_time <= 8:
        print("breakfast time")
    elif 12 <= user_time <= 13:
        print("lunch time")
    elif 18 <= user_time <= 19:
        print("dinner time")


def convert(user_input):
    hr, mint = user_input.split(":")
    hr, mint = int(hr), int(mint) / 60

    return float(hr + mint)


if __name__ == "__main__":
    main()
