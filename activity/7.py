n = int(input("input num: "))

fqt = 1
for i in range(2, n + 1):
    fqt *= i

sum = 0
temp = fqt
while temp > 0:
    sum += temp % 10
    temp //= 10

print(f"{n}! = {fqt}, მისი ციფრების ჯამი = {sum}")