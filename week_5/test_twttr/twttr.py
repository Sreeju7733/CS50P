def main():
    # getting input from user
    user_input = input("Input: ")
    print(shorten(user_input))


def shorten(word):
    for i in word:
        if i in "aeiouAEIOU":
            word = word.replace(i, "")

    return word


if __name__ == "__main__":
    main()
