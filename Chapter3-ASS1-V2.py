def age():
    age = int(input("Enter Age : "))

    if age <= 13:
        print("Child")
    elif age <= 19:
        print("Teenager")
    else:
        print("Adult")
age()