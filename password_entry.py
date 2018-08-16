"""Thomas Jordan"""
password_length = 6
password = input("Please enter a password: ")

while len(password) < password_length:
    password = input("Please enter a password: ")

print("*"*len(password))