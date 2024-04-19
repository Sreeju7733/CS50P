# getting input from user and covert to lowercase
user_input = input("Greeting: ").lower().strip()

# spliting input using "."
split_input = user_input.split(".")


# validating
if split_input[-1] in ["jpeg", "jpg"]:
    print("image/jpeg")

elif split_input[-1] in ["png", "gif"]:
  print(f"image/{split_input[-1]}")

elif split_input[-1] in ["zip", "pdf"]:
    print(f"application/{split_input[-1]}")

elif split_input[-1] in ["txt"]:
    print("text/plain")

else:
    print("application/octet-stream")
