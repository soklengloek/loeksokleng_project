import os
import csv
import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "attendance"
)
cursor = conn.cursor()
'''if conn.is_connected():
    print ("Connect Successful!")
cursor = conn.cursor()
cursor.execute(
    """Create table employee(
    ID int auto_increment primary key,
    Name varchar(30),
    Date int,
    Status varchar(20))"""
)
print ("Table Create Successful!")'''
def clear():
    os.system("cls" if os.name== 'nt' else 'clear')
def add_student():
    print ("++++ Add Student Name +++++")
    std = input ("Enter Student Name : ")
    dated = input("Date : ")
    mon = input ("Month : ")
    stat = input ("Enter Student Status : ")
    sql = "Insert into student (Name, Date, Month, Status) values(%s, %s, %s, %s)"
    data = (std, dated, mon, stat)
    cursor.execute(sql,data)
    conn.commit()
    print ("Student ADDED!")
    print ("="*30)
    input ("Press Enter to go back.....")
    clear()
def add_emp():
    print ("+++++ Add Employee Name +++++")
    std = input ("Enter Employee Name : ")
    dated = input("Date : ")
    mon = input ("Month : ")
    stat = input ("Enter Employee Status : ")
    sql = "Insert into employee (Name, Date, Month, Status) values(%s, %s, %s, %s)"
    data = (std, dated, mon, stat)
    cursor.execute(sql,data)
    conn.commit()
    print ("Employee ADDED!")
    print ("="*30)
    input ("Press Enter to go back.....")
    clear()
def add_menu():
    print ("===== Add Student or Employee =====")
    print("1 to Add student.")
    print("2 to Add Employee.")
    print("3 Go back")
    print ("="*30)
def add():
    while True:
        add_menu()
        choice = input("Enter your choice : ")
        clear()
        if choice == '1': add_student()
        elif choice == '2': add_emp()
        elif choice == '3':
            mark()
            break
        else: input ("Wrong choice! Press Enter to try again.")
        clear()
def view_student():
    print("----- View Student Attendance by Date -----")
    date = input ("Enter Date : ")
    sql = "select * from student WHERE Date LIKE %s"
    cursor.execute(sql, ("%" + date + "%",))
    result = cursor.fetchall()
    if result :
        print("===== List of Student =====")
        for row in result :
            print (row)
            print ("="*30)
        print ("All of Student!")
    else :
        print ("No Student!")
    input("\nPress Enter to go back.....")
    clear()
def view_emp():
    print("----- View Employee Attendance by Date -----")
    date = input ("Enter Date : ")
    sql = "select * from employee WHERE Date LIKE %s"
    cursor.execute(sql, ("%" + date + "%",))
    result = cursor.fetchall()
    if result :
        print("===== List of Employee =====")
        for row in result :
            print (row)
            print ("="*30)
        print ("All of Employee!")
    else :
        print ("No Employee!")
    input("\nPress Enter to go back.....")
    clear()
def view_menu():
    print ("===== View Attendance Student or Employee =====")
    print("1 View Attendance Student.")
    print("2 View Attendance Employee.")
    print("3 Go back")
    print ("="*30)
def view():
        while True:
            view_menu()
            choice = input("Enter your choice : ")
            clear()
            if choice == '1': view_student()
            elif choice == '2': view_emp()
            elif choice == '3':
                main()
                break
            else: input ("Wrong choice! Press Enter to try again.")
            clear()
def mark_student():
    print("***** Present/Absent for Student *****")
    name = input ("Enter Student Name : ")
    date = input ("Enter Date : ")
    stat = input ("Enter Status : ")
    sql = "Insert into student(Name, Date, Status) values(%s, %s, %s)"
    data = (name, date, stat)
    cursor.execute(sql, data)
    conn.commit()
    print ("Student Mark!")
    print ("="*30)
    input ("Press Enter to go back.....")
    clear()
def mark_emp():
    print("***** Present/Absent for Employee *****")
    name = input ("Enter Employee Name : ")
    date = input ("Enter Date : ")
    stat = input ("Enter Status : ")
    sql = "Insert into employee(Name, Date, Status) values(%s, %s, %s)"
    data = (name, date, stat)
    cursor.execute(sql, data)
    conn.commit()
    print ("Employee Mark!")
    print ("="*30)
    input ("Press Enter to go back.....")
    clear()
def mark_menu():
    print("+++++ Mark Present/Absent Student or employee +++++")
    print("="*45)
    print("1 Mark Present/Absent of Student.")
    print("2 Mark Present/Absent of Employee.")
    print("3 Add Student or Employee.")
    print("4 Back")
    print("="*45)
def mark():
    while True:
        mark_menu()
        ch = input ("Enter your choice : ")
        clear()
        if ch == '1' : mark_student()
        elif ch == '2' : mark_emp()
        elif ch == '3' : add()
        elif ch == '4' :
            main()
            break
        else: input ("Wrong Choice! Press Enter to try again!")
        clear()
def sea_stu():
    print ("===== Search Attendance by Student name =====")
    name = input ("Enter Student name : ")
    sql = "select * from student WHERE Name LIKE %s"
    cursor.execute(sql, ("%" + name + "%",))
    record = cursor.fetchall()
    if record :
        for row in record :
            print (row)
            print ("Student in List!")
            print ("="*30)
            input ("\nPress Enter to go back..... ")
            clear()
    else :
         print ("No Student Name!")
         print ("="*30)
         input ("\nPress Enter to go back..... ")
         clear()
def sea_emp():
    print ("===== Search Attendance by Employee name =====")
    name = input ("Enter Employee name : ")
    sql = "select * from employee WHERE Name LIKE %s"
    cursor.execute(sql, ("%" + name + "%",))
    record = cursor.fetchall()
    if record :
        for row in record :
            print (row)
            print ("Employee in List!")
            print ("="*30)
            input ("\nPress Enter to go back..... ")
            clear()
    else :
         print ("No Employee Name!")
         print ("="*30)
         input ("\nPress Enter to go back..... ")
         clear()
def sea_menu():
    print("***** Search Attendance by name of Student or Employee *****")
    print ("="*45)
    print ("1 Search Attendance Student name.")
    print ("2 Search Attendance Employee name.")
    print ("3 Back.")
    print ("="*45)
def search():
        while True:
            sea_menu()
            ch = input ("Enter your choice : ")
            clear()
            if ch == '1' : sea_stu()
            elif ch == '2' : sea_emp()
            elif ch == '3' : main()
            elif ch == '4' :
                main()
                break
            else: input ("Wrong Choice! Press Enter to try again!")
            clear()
def report_stu():
    print("----- Monthly Report Student Attendance -----")
    date = input ("Enter Month : ")
    sql = "select * from student WHERE Month LIKE %s"
    cursor.execute(sql, ("%" + date + "%",))
    result = cursor.fetchall()
    if result :
        print("===== List of Student =====")
        for row in result :
            print (row)
            print ("="*30)
        print ("All of Student!")
    else :
        print ("No Student!")
    input("\nPress Enter to go back.....")
    clear()
def report_emp():
    print("----- Monthly Report Employee Attendance -----")
    date = input ("Enter Month : ")
    sql = "select * from employee WHERE Month LIKE %s"
    cursor.execute(sql, ("%" + date + "%",))
    result = cursor.fetchall()
    if result :
        print("===== List of Employee =====")
        for row in result :
            print (row)
            print ("="*30)
        print ("All of Employee!")
    else :
        print ("No more Employee!")
    input("\nPress Enter to go back.....")
    clear()
def report_menu():
    print("***** Monthly Report Attendance of Student or Employee *****")
    print ("="*45)
    print ("1 Report for Attendance Student.")
    print ("2 Report for Attendance Employee.")
    print ("3 Back.")
    print ("="*45)
def report():
        while True:
            report_menu()
            ch = input ("Enter your choice : ")
            clear()
            if ch == '1' : report_stu()
            elif ch == '2' : report_emp()
            elif ch == '3' : main()
            elif ch == '4' :
                main()
                break
            else: input ("Wrong Choice! Press Enter to try again!")
            clear()
def tran_stu():
    print("===== Export Student Attendance into CSV ( Excel ) =====")
    cursor.execute("select * from student")
    data = cursor.fetchall()
    with open ("StudentAtt.csv", "w", newline="") as file :
        write = csv.writer(file)
        write.writerow(["ID", "Name", "Date", "Month", "Status"])
        write.writerow(data)
    print("Successful Convert!")
    print("="*30)
    input ("Press Enter to go back.....")
    clear()
def tran_emp():
    print("===== Export Employee Attendance into CSV ( Excel ) =====")
    cursor.execute("select * from employee")
    data = cursor.fetchall()
    with open ("EmployeeAtt.csv", "w", newline="") as file :
        write = csv.writer(file)
        write.writerow(["ID", "Name", "Date", "Month", "Status"])
        write.writerow(data)
    print("Successful Convert!")
    print("="*30)
    input ("Press Enter to go back.....")
    clear()
def tran_menu():
    print("===== Export Attendance into CSV (Excel) =====")
    print("-"*40)
    print("1 Export Student.")
    print("2 Export Employee.")
    print("3 Back.")
    print("-"*40)
def tran():
    while True:
        tran_menu()
        ch = input ("Enter your choice : ")
        clear()
        if ch == '1' : tran_stu()
        elif ch == '2' : tran_emp()
        elif ch == '3' :
            main()
            break
        else: input ("Wrong Choice! Press Enter to try again!")
        clear()
def menu():
    print("\tAttendance Management System")
    print("="*43)
    print("1 Mark Student or Employee.")
    print("2 View Attendance Student or Employee.")
    print("3 Search Attendance by name of Student or Employee.")
    print("4 Monthly attendance report.")
    print("5 Export attendance to CSV (Excel).")
    print("6 Exit.")
    print("="*43)
def main():
    while True :
        menu()
        ch = input("Enter your choice here : ")
        clear()
        if ch == '1' : mark()
        elif ch == '2' : view()
        elif ch == '3' : search()
        elif ch == '4' : report()
        elif ch == '5' : tran()
        elif ch == '6' :
            print("Thank you for using our system!")
            break
        else : input ("Wrong Choice, Try Again!!")
        clear()
main()