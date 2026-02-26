import os
import csv
import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "course_register"
)
cursor = conn.cursor()
'''if conn.is_connected():
    print ("Connect Successful!")
cursor = conn.cursor()
cursor.execute(
    """Create table register (
    ID int auto_increment primary key,
    Student_name varchar(30),
    Course_ID varchar(5))"""
)
print ("Table Create Successful!")'''
def clear():
 os.system("cls" if os.name== 'nt' else 'clear')
def add_course ():
    print ("+++++ ADD NEW COURSE +++++")
    course_name = input ("Enter Course name : ")
    ins = input ("Enter Course Instructor : ")
    cre = int (input("Enter course Credits : "))
    sql = "INSERT INTO courses (Course_name, Instructor , Credits) values(%s, %s, %s)"
    data = (course_name,ins,cre)
    cursor.execute(sql, data)
    conn.commit()
    print("Course add success!")
    print("Thank You!")
    print("="*30)
    input ("Press Enter to go back...")
    clear()
def add_student():
   print("===== ADD NEW STUDENT =====")
   student_name = input ("Enter Student Name : ")
   course_id = input ("Enter Course ID : ")
   sql = "INSERT INTO register (Student_name, Course_ID) values (%s, %s)"
   data = (student_name,course_id)
   cursor.execute (sql, data)
   conn.commit()
   print ("Student Add Success!")
   print("="*30)
   input ("Press Enter to go back...")
   clear()
def view_reg():
    cursor.execute("select * from register")
    result = cursor.fetchall()
    if result :
        print("===== List of Students =====")
        for row in result :
            print (row)
            print()
            print ("="*30)
        print ("All of Students!")
    else :
        print ("No more Student!")
    input("\nPress Enter to go back.....")
    clear()
def view_course():
    cursor.execute("select * from courses")
    result = cursor.fetchall()
    if result :
        print("===== List of Course =====")
        for row in result :
            print (row)
            print ("="*30)
        print ("All of Course!")
    else :
        print ("No more Course!")
    input("\nPress Enter to go back.....")
    clear()
def search():
    print ("===== Welcome to Search Student =====")
    search_std = input ("Enter Student Name : ")
    sql = "select * from register WHERE Student_name LIKE %s"
    cursor.execute(sql, ("%" + search_std + "%",))
    record = cursor.fetchall()
    if record :
        for row in record :
            print (row)
            print ("Student Found!")
            print ("="*30)
            input ("\nPress Enter to go back..... ")
            clear()
    else :
         print ("Student not found!")
         print ("="*30)
         input ("\nPress Enter to go back..... ")
         clear()
def tran():
    print("===== Convert into CSV ( Excel ) =====")
    cursor.execute("select * from register")
    data = cursor.fetchall()
    with open ("Register.csv", "w", newline="") as file :
        write = csv.writer(file)
        write.writerow(["ID", "StudentName", "CourseID"])
        write.writerow(data)
    print("Successful Convert!")
    print("="*30)
    input ("Press Enter to go back.....")
    clear()
def menu():
    print("\tWelcome to Course Registration System")
    print("="*50)
    print("Press 1 to ADD new course.")
    print("Press 2 to Register new student.")
    print("Press 3 to View Register Student.")
    print("Press 4 to View course.")
    print("Press 5 to Search student.")
    print("Press 6 to Export Register to CSV (Excel).")
    print("Press 7 to Exit.")
    print("="*50)
def main():
    while True :
        menu()
        ch = input ("Enter your choice here : ")
        if ch == '1': add_course()
        elif ch == '2': add_student()
        elif ch == '3' : view_reg()
        elif ch == '4' : view_course()
        elif ch == '5' : search()
        elif ch == '6' : tran()
        elif ch == '7' :
            print ("Thanks for using our system!")
            break
        else : input ("Wrong Choice, Press Enter to Try Again!")
        clear()
main()