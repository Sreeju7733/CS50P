# getting input from the user, removing space and converting to lowercase
user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

# checking whether input contain any of the item
if user_input in ["42", "forty-two", "forty two"]:
    print("Yes")
else:
    print("No")
