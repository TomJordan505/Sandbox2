"""Thomas Jordan"""

password_length = 6


def main():
    password = get_password(password_length)
    print_stars(password)


def get_password(password_length):
    password = input("Please enter a {} character password: ".format(password_length))

    while len(password) < password_length:
        password = input("Please enter a {} character password: ".format(password_length))
    return password


def print_stars(sequence):
    print("*" * len(sequence))


main()
