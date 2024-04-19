from validator_collection import validators

email = input("What's your email address? ")
try:
    is_valid = validators.email(email)
    if is_valid:
        print("Valid")
    else:
        print("Invalid")
except:
    print("Invalid")
