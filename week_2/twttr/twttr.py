# getting input from user
user_input = input("Input: ")

for i in user_input:
    if i in "aeiouAEIOU":
        user_input = user_input.replace(i, "")

print(f"Output: {user_input}")
