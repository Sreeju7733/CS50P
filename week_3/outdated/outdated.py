months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    # getting input from the user
    user_input = input("Date: ")
    try:
        if "/" in user_input:
            mm, dd, yyyy = user_input.split("/")
        elif "," in user_input:
            mmdd, yyyy = user_input.split(", ")
            mm, dd = mmdd.split(" ")

            mm = (months.index(mm)) + 1
        if int(mm) > 12 or int(dd) > 31:
            raise ValueError
    except (AttributeError, ValueError, NameError, KeyError):
        pass
    else:
        print(f"{int(yyyy)}-{int(mm):02}-{int(dd):02}")
        break
