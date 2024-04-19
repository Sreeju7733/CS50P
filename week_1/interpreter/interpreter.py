# Getting input from the user and strip() and split by " "
user_input = input("Expression: ").strip().split(" ")

# assigning value to the x, y and z
x, y, z = int(user_input[0]), user_input[1], int(user_input[2])

if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z
else:
    result = x % z

print(float(result))
