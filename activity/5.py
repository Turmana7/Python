x = int(input("input 3digit num: "))
orginal = x
sum = 0

while x > 0:
    cifri = x % 10
    sum += cifri ** 3
    x //= 10

if sum == orginal:
    print("ეს არის არმსტრონგის რიცხვი")
else:
    print("არ არის არმსტრონგის რიცხვი")