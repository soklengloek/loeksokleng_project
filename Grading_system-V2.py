def student_grade():

    name = input("Name : ")
    id = input("ID : ")
    att = float(input("Attendance 0-10 : "))
    quiz = float(input("Quiz 0-15 : "))
    mid = float(input("Midterm 0-15 : "))
    pro = float(input("Project 0-25 : "))
    fin = float(input("Final 0-35 : "))
    total = att + quiz + mid + pro + fin
    avg = total // 5
    # Find grade
    if total >= 90:
        grade = "A"
    elif total >= 80:
        grade = "B"
    elif total >= 70:
        grade = "C"
    elif total >= 60:
        grade = "D"
    elif total >= 50:
        grade = "E"
    else:
        grade = "F"
    print("ID :", id)
    print("Name :", name)
    print("Total :", total)
    print("Average :", avg)
    print("Grade :", grade)
student_grade()
