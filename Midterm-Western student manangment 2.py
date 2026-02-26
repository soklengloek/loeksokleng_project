print("----- Add Student Information -----")
students = {}
def my_input():
    id = input("Enter ID : ")
    name = input("Enter Name : ")
    att = float(input("Enter attendance (0-10) : "))
    q = float(input("Enter quiz (0-15) : "))
    ass = float(input("Enter assignment (0-25) : "))
    mid = float(input("Enter midterm (0-20) : "))
    fin = float(input("Enter final (0-30) : "))
    print ("Student added successfully!")
    return id, name, att, q, ass, mid, fin
def grade_find(total):
    if total >= 90:
        grade = 'A'
    elif total >= 80:
        grade = 'B'
    elif total >= 70:
        grade = 'C'
    elif total >= 60:
        grade = 'D'
    elif total >= 50:
        grade = 'E'
    else:
        grade = 'F'
    return grade
def output(id, name, att, q, ass, mid, fin, total, grade):
    print("\n======= Student Result =====")
    print("ID:", id)
    print("Name:", name)
    print("Attendance:", att)
    print("Quiz:", q)
    print("Assignment:", ass)
    print("Midterm:", mid)
    print("Final:", fin)
    print("Total Score:", total)
    print("Grade:", grade)
def store (id, name, att, q, ass, mid, fin, total, grade) :
    students [id] = {
        "Name :" : name,"Attendance : " : att,"Quiz : " : q,"Assignment : " : ass,"Midterm : " : mid,"Final : " : fin,"Total :" : total, "Grade : " : grade
    }
    return
def add_student():
    print("\n--- Add Student Information ---")
    id = input("Enter ID: ")
    name = input("Enter Name: ")
    att = float(input("Enter Attendance (0-10): "))
    q = float(input("Enter Quiz (0-15): "))
    ass = float(input("Enter Assignment (0-25): "))
    mid = float(input("Enter Midterm (0-20): "))
    fin = float(input("Enter Final Exam (0-30): "))
    total = att + q + ass + mid + fi
    grade = grade_find(total)
    store(id, name, att, q, ass, mid, fin, total, grade)
    print("Student added successfully!")
def view_all():
    print("\n--- All Students Information ---")
    if not students:
        print("No student yet!")
    else:
        for id, info in students.items():
            print("ID:", id, "Info:", info)
def search(id):
    if id in students:
        print("\n--- Student Found ---")
        print(students[id])
    else:
        print("Student not found.")
def update(id):
    if id in students:
        print("\n--- Update Student Information ---")
        name = input("Enter Name: ")
        att = float(input("Enter Attendance (0-10): "))
        q = float(input("Enter Quiz (0-15): "))
        ass = float(input("Enter Assignment (0-25): "))
        mid = float(input("Enter Midterm (0-20): "))
        fin = float(input("Enter Final Exam (0-30): "))
        total = att + q + ass + mid + fin
        grade = grade_find(total)
        store(id, name, att, q, ass, mid, fin, total, grade)
        print("Update Successful!")
    else:
        print("Student not found.")
def delete(id):
    if id in students:
        del students[id]
        print("Student deleted successfully.")
    else:
        print("Student not found.")
def menu():
    while True:
        print("\n========= WU STUDENT MANAGEMENT MENU =========")
        print("1. Add Student Information")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Update Student by ID")
        print("5. Delete Student by ID")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_all()
        elif choice == "3":
            id = input("Enter ID to Search: ")
            search(id)
        elif choice == "4":
            id = input("Enter ID to Update: ")
            update(id)
        elif choice == "5":
            id = input("Enter ID to Delete: ")
            delete(id)
        elif choice == "6":
            print("Exit Program. Goodbye!")
            break
        else:
            print("Wrong Option!")
menu()
id, name, att, q, ass, mid, fin = my_input()
total = att + q + ass + mid + fin
grade = grade_find(total)
output(id, name, att, q, ass, mid, fin, total, grade)
