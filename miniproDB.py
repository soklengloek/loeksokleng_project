import os
import pyodbc
db_path = r"DBMINI\Student_Manange.accdb"
conn = pyodbc.connect(
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=' + db_path + ';'
)
cursor = conn.cursor()
def clear():
 os.system("cls" if os.name== 'nt' else 'clear')
def add():
    print ("===== Input Student Information =====")
    name1 = input ("Enter Name : ")
    age = input ("Enter age : ")
    course = input ("Enter Course : ")
    cursor.execute(
        "Insert into student (Name, Age, Course)values(?, ?, ?)",
        (name1, age, course)
    )
    conn.commit()
    print ("Student Added!")
    print ("="*25)
    input ("\nPress Enter To Go Back..... ")
    clear()
def view ():
        print ("===== Student List =====")
        cursor.execute("Select * from student")
        for row in cursor.fetchall():
            print (row)
            print ("="*25)
        print ("All of students list!")
        input ("\nPress Enter To Go Back..... ")
        clear()
def search():
    print("===== 3.Search Employee =====")
    sear = str (input ("Enter Student name : "))
    cursor.execute(
        "Select * from student WHERE name LIKE ?",
        ('%' + sear + '%',)
    )
    record = cursor.fetchall()
    if record :
        for row in record :
            print (row)
            print ("Student found!")
            print ("="*25)
            input ("\nPress Enter To Go Back..... ")
            clear()
    else :
         print ("Student not found!")
         print ("="*25)
         input ("\nPress Enter To Go Back..... ")
         clear()
def update():
    print ("===== Update Student Information =====")
    stuid = input ("Enter Student ID : ")
    un = input ("Enter Student new name : ")
    ua = input ("Enter Student new age : ")
    uc = input ("Enter Student new course : ")
    cursor.execute(
    "UPDATE student SET Name=?, Age=?, Course=? WHERE ID=?",
    (un, ua, uc, stuid)
    )
    conn.commit()
    print("Student update complete!")
    print ("="*35)
    input ("\nPress Enter To Go Back..... ")
    clear()
def delete():
    print("===== Delete Student =====")
    name_delete= input ("Enter student name : ")
    cursor.execute(
        "DELETE From student WHERE Name =?",
        (name_delete)
    )
    conn.commit()
    print ("Student Deleted!")
    print("="*25)
    input ("\nPress Enter To Go Back..... ")
    clear()
def menu():
    print ("Welcome to Student management system")
    print ("="*40)
    print ("1 to add new student.")
    print ("2 to view list student.")
    print ("3 to search student.")
    print ("4 to update student.")
    print ("5 to delete student.")
    print ("6 exit.")
    print("="*40)
def main():
    while True:
        menu()
        ch = input ("Enter number here : ")
        clear()
        if ch == '1' : add()
        elif ch == '2' : view()
        elif ch == '3' : search()
        elif ch == '4' : update()
        elif ch == '5' : delete()
        elif ch == '6' :
            print ("Good Luck! Bye Bye!")
            print ("-"*25)
            break
        else : print ("Choose again!")
main()