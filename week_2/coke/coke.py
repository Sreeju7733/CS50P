priceofcoke = 50


while priceofcoke > 0:
    print(f"Amount Due: {priceofcoke}")
    # getting input from user
    user_input = int(input("Insert Coin: "))


    if user_input in [25, 10, 5] and priceofcoke != 0:
        priceofcoke = priceofcoke - user_input

        if priceofcoke > 0:
            print(f"Amount Due: {priceofcoke}")

print(f"Change Owed: {abs(priceofcoke)}")
