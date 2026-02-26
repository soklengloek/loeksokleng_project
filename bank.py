import os
import csv
import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "bank"
)
cursor = conn.cursor()
'''if conn.is_connected():
    print ("Connect Successful!")
cursor = conn.cursor()
cursor.execute(
    """Create table transactions (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    AccountID INT,
    Type VARCHAR(20),
    Amount FLOAT,
    Date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (AccountID) REFERENCES accounts(ID))"""
)
print ("Table Create Successful!")'''
def clear():
    os.system("cls" if os.name== 'nt' else 'clear')
def create_acc():
    print("\tCreate Account Currency")
    print ("="*38)
    print("\tMake sure you put your name right!")
    name = input ("Enter Your Name : ")
    bla = input ("Input your Balance : ")
    cur = input ("Currency USD $ or Riel ៛​ : ")
    sql = "Insert into accounts(Name, Currency, Balance) values(%s, %s, %s)"
    data = (name, cur, bla)
    cursor.execute(sql,data)
    conn.commit()
    print ("="*50)
    print("\t\tAccount Create Success!")
    input ("Press Enter to go back...")
    clear()
def view():
    print("----- View Account -----")
    name = input ("Enter Your Name : ")
    sql = "select * from accounts WHERE Name LIKE %s"
    cursor.execute(sql, ("%" + name + "%",))
    result = cursor.fetchall()
    if result :
        print ("="*30)
        print ("|","\tYour name found","     |")
        print ("="*30)
        print("======== Your Account ========")
        for row in result :
            print (row)
            print ("="*30)
    else :
        print ("="*30)
        print ("\tNo name found!!")
        print ("="*30)
    input("\nPress Enter to go back.....")
    clear()
def create_menu():
    print("======= Welcome to Create Your Account =======")
    print ("="*40)
    print("1.Create New Account.")
    print("2.View Your Account.")
    print ("3.Back")
    print ("="*40)
def create():
    while True:
        create_menu()
        ch = input ("Enter your choice here : ")
        clear()
        if ch == '1' : create_acc()
        elif ch == '2' : view()
        elif ch == '3' :
            main()
            break
        else : input("\nWrong Choice. Press Enter to try again!")
        clear()
def deposit():
        print ("="*38)
        print ("|","\t\tDeposit\t\t","    |")
        print ("="*38)
        acc_id = input ("Enter Your Account ID : ")
        amount = input ("Enter Amount : ")
        cursor.execute("UPDATE accounts SET balance = balance + %s WHERE id = %s", (amount, acc_id))
        cursor.execute(
        "INSERT INTO transactions (AccountID, Type, Amount) VALUES (%s, %s, %s)",
        (acc_id, "Deposit", amount)
        )
        conn.commit()
        print ("="*38)
        print("\t\tDeposit Success!")
        input ("Press Enter to go back...")
        clear()
def withdraw():
        print ("="*38)
        print ("|","\t\tWithdraw\t","    |")
        print ("="*38)
        acc_id = input ("Enter Your Account ID : ")
        amount = input ("Enter Amount : ")
        cursor.execute("UPDATE accounts SET balance = balance - %s WHERE id = %s", (amount, acc_id))
        cursor.execute(
        "INSERT INTO transactions (AccountID, Type, Amount) VALUES (%s, %s, %s)",
        (acc_id, "Deposit", amount)
        )
        conn.commit()
        print ("="*38)
        print("\t\tWithdraw Success!")
        input ("Press Enter to go back...")
        clear()
def balance ():
    print("----- View Account Balance -----")
    acc_id = int(input("Enter account ID: "))
    cursor.execute("SELECT name, balance ,currency FROM accounts WHERE id = %s", (acc_id,))
    result = cursor.fetchone()
    if result:
        print(f"Name : {result[0]}")
        print(f"Balance : {result[1]}")
        print(f"Currency : {result[2]}")
    else:
        print("Account not found!")
    input("\nPress Enter to go back.....")
    clear()
def export():
    print ("="*50)
    print ("|","\t\tExport transactions to CSV\t","|")
    print ("="*50)
    cursor.execute("""
        SELECT accounts.ID, accounts.Name, transactions.Type, transactions.Amount, transactions.Date
        FROM transactions
        JOIN accounts ON transactions.AccountID = accounts.ID
    """)
    records = cursor.fetchall()
    with open("Transactions.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["AccountID", "Name", "Type", "Amount", "Date"])
        writer.writerows(records)
    print("Transactions Export Complete!")
    input("\nPress Enter to go back.....")
    clear()
def menu():
    print ("="*50)
    print ("|","\tWelcome to our simple banking system\t","|")
    print ("="*50)
    print("1-Create Account.")
    print("2-Deposit.")
    print("3-Withdraw.")
    print("4-View Balance")
    print("5-Export Transaction to CSV (Excel).")
    print("6-Exit.")
def main():
    while True :
        menu()
        ch = input ("Enter your choice : ")
        clear()
        if ch == '1' : create()
        elif ch == '2' : deposit()
        elif ch == '3' : withdraw()
        elif ch == '4' : balance()
        elif ch == '5' : export()
        elif ch == '6' :
            print("Goodbye! Have a nice day!")
            break
        else : input("\nWrong Choice. Press Enter to try again!")
        clear()
main()