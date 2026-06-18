number = int(input("input num: "))
search_num = int(input("input search num: "))
count = 0

while number > 0:
    if number % 10 == search_num:
        count += 1
    number //= 10

print(f"ციფრი გვხვდება {count}-ჯერ.")