def main():
    # getting input from user
    user_input = input("Greeting: ")
    print(f"${value(user_input)}")

def value(greeting):
    greeting = greeting.lower()
    if greeting.startswith("hello"):
      dollars = 0
    elif greeting.startswith("h"):
      dollars = 20
    else:
      dollars = 100

    return dollars

if __name__ == "__main__":
    main()
