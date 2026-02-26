import os
import csv
import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "inventory"
)
cursor = conn.cursor()
'''if conn.is_connected():
    print ("Connect Successful!")
cursor = conn.cursor()
cursor.execute(
    """Create table products(
    ID int auto_increment primary key,
    Name varchar(30),
    Quantity int,
    Price float,
    Supplier varchar(20))"""
)
print ("Table Create Successful!")'''
def clear():
    os.system("cls" if os.name== 'nt' else 'clear')
def add_pro():
    print("----- Add Products -----")
    name_pro = input ("Input Product Name : ")
    qty = input ("Input Product Quantity : ")
    pri = input ("Input Product Price : $")
    sup = input ("Input Supplier Name : ")
    sql = "Insert into products(Name, Quantity, Price, Supplier) values (%s, %s, %s, %s)"
    data = (name_pro, qty, pri, sup)
    cursor.execute(sql,data)
    conn.commit()
    print("Product add success!")
    print("Thank You!")
    print("="*30)
    input ("Press Enter to go back...")
    clear()
def update ():
    print("===== Update Stock Quantity =====")
    name_product = input("Enter Product name : ")
    new_qty = input ("Enter New Quantity : ")
    sql = "update products set Quantity=%s where Name =%s"
    data = (new_qty, name_product)
    cursor.execute(sql,data)
    conn.commit()
    print("Quantity Update!")
    print("="*30)
    input ("Press Enter to go back.....")
    clear()
def view():
    low = int (input ("Enter Low stock from : "))
    sql = "select * from products where Quantity <= %s"
    cursor.execute(sql, (low,))
    result = cursor.fetchall()
    if result :
        print("===== List of Products =====")
        for row in result :
            print (row)
            print()
            print ("="*30)
        print ("All of Low-Stock Product!")
    else :
        print ("No Low-Stock Product!")
    input("\nPress Enter to go back.....")
    clear()
def delete():
    print("===== Delete Products by ID =====")
    idpro = input ("Enter Product ID : ")
    sql = "Delete from products where id=%s"
    cursor.execute(sql, (idpro,))
    conn.commit
    print ("Product Deleted!")
    print("="*30)
    input ("Press Enter to go back.....")
    clear()
def tran():
    print("===== Convert into CSV ( Excel ) =====")
    cursor.execute("select * from products")
    data = cursor.fetchall()
    with open ("Products.csv", "w", newline="") as file :
        write = csv.writer(file)
        write.writerow(["ID", "ProductName", "QTY", "Price", "Supplier"])
        write.writerow(data)
    print("Successful Convert!")
    print("="*30)
    input ("Press Enter to go back.....")
    clear()
def menu():
    print("Inventory Management System")
    print("="*30)
    print ("Enter 1 to Add Products.")
    print ("Enter 2 to Update Product Quantity.")
    print ("Enter 3 to View Low-Stock Products.")
    print ("Enter 4 to Delete Products.")
    print ("Enter 5 to Export to CSV (Excel).")
    print ("Enter 6 to Exit.")
    print("="*30)
def main():
    while True:
        menu()
        ch = input ("Enter Your Choice Here : ")
        if ch == '1': add_pro()
        elif ch == '2': update()
        elif ch == '3': view()
        elif ch == '4' : delete()
        elif ch == '5' :tran()
        elif ch == '6' :
            print ("Exit! Thank You!")
            break
        else : input ("Wrong Choice, Try Again!!")
        clear()
main()
