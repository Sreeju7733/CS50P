# getting input from user
user_input = input("camelCase: ")
result = ""

for i in range(len(user_input)):
  if user_input[i].isupper():
    result = result + "_" + user_input[i].lower()
  else:
    result = result + user_input[i]

print(f"snake_case: {result}") 
