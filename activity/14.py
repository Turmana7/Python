def is_palindrome(text):

    clean_text = text.lower().replace(" ", "")

    reversed_text = clean_text[::-1]
    
    return clean_text == reversed_text

user_text = input("input txt: ")

if is_palindrome(user_text):
    print("this txt is palindrome!")
else:
    print("this txt is not palindrome.")