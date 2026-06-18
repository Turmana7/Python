products = {
    "პური": 1.50,
    "ყველი": 12.00,
    "რძე": 4.00
}

for item in products:
    products[item] = round(products[item] * 0.90, 2)

print(products)