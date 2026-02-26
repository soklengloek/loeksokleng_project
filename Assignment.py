import pyodbc
db_path = r"DB_ASS\company.accdb"

conn = pyodbc.connect(
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=' + db_path + ';'
)
cursor = conn.cursor()
def add ():
    print ("===== 1.ADD NEW EMPLOYEE =====")
    name1 = input ("Enter Name : ")
    salary1 = float (input ("Enter Salary : "))
    dep  = input ("Enter Department : ")
    cursor.execute(
        "Insert into employee (Name, Salary, Department)values(?,?,?)",
        (name1, salary1, dep)
    )
    print ("Employee add successfully!")
    print ("="*25)
    conn.commit()
def view ():
    print ("===== 2.EMPLOYEE LIST =====")
    cursor.execute("Select * from employee")
    for row in cursor.fetchall():
        print (row)
        print ("="*25)
def search():
    print("===== 3.Search Employee =====")
    src = str (input ("Enter Employee name : "))
    cursor.execute(
        "Select * from employee WHERE name LIKE ?",
        ('%' + src + '%',)
    )
    record = cursor.fetchall()
    if record :
        for row in record :
            print (row)
            print ("Employee Found!")
            print ("="*25)
    else : 
         print ("Employee not found!")
         print ("="*25)
def menu():
    print ("Welcome to Menu")
    print ("1 to add employee")
    print ("2 to view")
    print("3 to search employee")
    print ("4 to exit")
def main ():
    while True :
        menu()
        ch = input (("Enter any number : "))
        if ch == '1': add()
        elif ch == '2': view()
        elif ch =='3': search()
        elif ch == '4': 
            print("Bye Bye! Have a good luck!")
            print ("-"*25)
            break
        else : print ("Wrong choice! Try again!")
main()