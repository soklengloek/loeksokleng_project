def calculator():
    # Input
    a = float(input("Enter Number 1 : "))
    b = float(input("Enter Number 2 : "))
    print("Total Number 1 + Number 2 :", a + b)
    print("Total Number 1 - Number 2 :", a - b)
    print("Total Number 1 * Number 2 :", a * b)
    if b != 0:
        print("Total Number 1 / Number 2 :", a / b)
        print("Total Number 1 // Number 2 :", a // b)
        print("Total Number 1 % Number 2 :", a % b)
    else:
        print("Division, Floor Division, and Modulo: Not allowed (divide by zero)")
    print("Total Number 1 ** Number 2 :", a ** b)
calculator()

