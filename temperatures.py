"""

CP1404/CP5632 - Practical

Pseudocode for temperature conversion

"""

MENU = """C - Convert Celsius to Fahrenheit

F - Convert Fahrenheit to Celsius

Q - Quit"""


def main():
    print(MENU)


choice = input(">>> ").upper()

while choice != "Q":

    if choice == "C":

        celsius = float(input("Celsius: "))

        fahrenheit = fahrenheit_conversion(celsius)

        print("Result: {:.2f} F".format(fahrenheit))

    elif choice == "F":

        fahrenheit = float(input("Fahrenheit: "))

        celsius = celsius_conversion(fahrenheit)

        print("Result: {:.2f} F".format(celsius))



    else:

        print("Invalid option")

    print(MENU)

    choice = input(">>> ").upper()

print("Thank you.")


def celsius_conversion(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)


def fahrenheit_conversion(celsius):
    return celsius * 9.0 / 5 + 32


main()
