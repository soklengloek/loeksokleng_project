import pyodbc
db_path = r"DB-ASS\company.accdb"

conn = pyodbc.connect(
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=' + db_path + ';'
)
cursor = conn.cursor()
def add ():
    print ("===== ADD NEW EMPLOYEE =====")
    name1 = input ("Enter Name : ")
    salary1 = float (input ("Enter Salary : "))
    dep  = input ("Enter Department : ")
    cursor.execute(
        "Insert into emp (Name, Salary, Department)values(?,?,?)",
        (name1, salary1, dep)
    )
    print ("Employee add successfully!")
    print ("="*25)
    conn.commit()
def view ():
    print ("===== EMPLOYEE LIST =====")
    cursor.execute("Select * from employee")
    for row in cursor.fetchall():
        print (row)
def menu():
    print ("Welcome to Menu")
    print ("1 to add Employee")
    print ("2 to view")
    print ("5 to exit")
def main ():
    while True :
        menu()
        ch = input (("Enter any number : "))
        if ch == '1': add()
        elif ch == '2': view()
        elif ch == '5': break
        else : print ("Wrong choice! Try again!")
main()