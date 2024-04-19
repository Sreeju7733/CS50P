items = {}

while True:
  try:
    # getting input from the user
    user_input = input()
    if user_input in items:
      items[user_input] = items[user_input] + 1
    else:
      items[user_input] = 1
  except EOFError:
    break

# items.item will make list of tuples with key value pairs
# sorted() will sort the list of tuples
# dict will convert the list of tuples to dictionary
acc_items = dict(sorted(items.items()))
for item in acc_items:
  print(items[item], item.upper())
