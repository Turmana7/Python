def count_xmovani(text):
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

input = input("Enter some text: ")

result = count_xmovani(input)
print(f"The number of vowels is: {result}")
