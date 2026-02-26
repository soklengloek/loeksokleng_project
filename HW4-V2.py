def grading_system():
    name = input("Enter Name : ")
    id = int(input("Enter ID : "))
    att = int(input("Enter Attendance (0-10) : "))
    q = int(input("Enter Quiz (0-10) : "))
    mid = int(input("Enter Midterm (0-15) : "))
    fin = int(input("Enter Final (0-60) : "))
    total = att + q + mid + fin
    avg = total / 4
    print("=" * 80)
    print("Name   ID   Attendance   Quiz   Midterm   Final   Average")
    print("=" * 80)
    print(name, id, att, q, mid, fin, avg)
grading_system()
