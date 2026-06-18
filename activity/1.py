x = int(input("input number: "))
sum = 0

while x > 0:
    num = x % 10
    if num % 2 == 0:
        sum += num
    x //= 10

print(f"ლუწი ციფრების ჯამი: {num}")