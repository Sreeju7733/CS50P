# convert function
def convert(str):
    str = str.replace(":)", "🙂").replace(":(", "🙁")
    return str

# main function
def main():
    user_input = input("Enter text: ")
    print(convert(user_input))

# Call main function
if __name__ == "__main__":
    main()
