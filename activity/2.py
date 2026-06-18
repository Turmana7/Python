x = int(input("შეიყვანეთ რიცხვი: "))
reversed = 0

while x > 0:
    num = x % 10
    reversed = reversed * 10 + num
    x //= 10

print(f"შებრუნებული რიცხვი: {reversed}")