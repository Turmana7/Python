users = {
    "giorgi": "12345",
    "ani": "password123",
    "luka": "qwerty"
}

username = input("Enter username: ").strip()
password = input("Enter password: ").strip()

if username in users and users[username] == password:
    print("Welcome! Login successful.")
else:
    print("Invalid username or password.")