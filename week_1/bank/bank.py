# getting input from user and covert to lowercase
user_input = input("Greeting: ").lower().strip()

 # validating
if user_input.startswith("hello"):
  dollars = 0
elif user_input.startswith("h"):
  dollars = 20
else:
  dollars = 100

print(f"${dollars}")
