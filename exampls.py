# Shoe stores keeping track of inventory

Black_shoes = {42: 2, 41: 3, 40: 4, 39: 1, 38: 0}
print(Black_shoes)
while True:
    purchase_size = int(input("What size of shoe would you like to buy? \n"))
    if purchase_size < 0:
        break
    if Black_shoes[purchase_size] > 0:
        Black_shoes[purchase_size] -= 1
    else:
        print("Sorry we are out of stock")
    print(Black_shoes)

