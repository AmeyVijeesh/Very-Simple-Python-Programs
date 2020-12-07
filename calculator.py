print("""This is the calculator program made by Amey 
You have four operators and you can get your result within seconds!""")


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("""List of operations:
Add (A)
Subtract (S)
Multiply (M)
Divide (D)""")


while True:

    choice = input("Choose an operation(A/S/M/D): ").upper()
    if choice in ('A', 'S', 'M', 'D'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == 'A':
            print(num1, "added to", num2, "is", add(num1, num2))

        elif choice == 'S':
            print(num1, "subtracted by", num2, "is", subtract(num1, num2))

        elif choice == 'M':
            print(num1, "multiplied by ", num2, "is", multiply(num1, num2))

        elif choice == 'D':
            print(num1, "divided by", num2, "is", divide(num1, num2))
        break
    else:
        print("Invalid Input")
print("Thank you!")
