import inflect

p = inflect.engine()
words = []

while True:
    try:
        # getting input from user
        user_input = input("Input: ")
        words.append(user_input)
    except EOFError:
        break

result = p.join(words)
print("Adieu, adieu, to", result)
