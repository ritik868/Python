grocery_price = {
    "Detergent": 300,
    "Shampoo": 100,
    "Hair oil":270,
    "Corn flakes":199,
    "Biscuit": 50,
    "Namkeen":120
}

grocery_quantity = {
    "Detergent": 2,
    "Shampoo": 10,
    "Hair oil":3,
    "Corn flakes":2,
    "Biscuit": 1,
    "Namkeen": 5
}

sum = 0
for x in grocery_price.keys():
        sum += (grocery_price[x]*grocery_quantity[x])

print("The sum of the items: ",sum)
