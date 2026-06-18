x = int(input("input 5digit num: "))

first = x // 10000
last = x % 10
sum = first + last

print(f"პირველი და ბოლო ციფრის ჯამი: {sum}")