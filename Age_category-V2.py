def age_category():
    age = int(input("Enter Age : "))

    if age < 13:
        print("Child")
    elif 13 <= age <= 19:
        print("Teenager")
    elif 20 <= age <= 59:
        print("Adult")
    else:
        print("Senior Citizen")
age_category()
