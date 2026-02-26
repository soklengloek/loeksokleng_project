import os
import csv
import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "librarypro"
)
cursor = conn.cursor()
'''if conn.is_connected():
    print ("Connect Successful!")
cursor = conn.cursor()
cursor.execute(
    """Create table books (
    ID int auto_increment primary key,
    Title varchar(30),
    Author varchar(25),
    Category varchar (25),
    Status varchar (20))"""
)'''
print ("Table Create Successful!")
def clear():
 os.system("cls" if os.name== 'nt' else 'clear')
def add():
    print ("===== Welcome to Add new book =====")
    titlebook = input ("Enter book Title : ")
    authorb = input ("Enter Author of a book : ")
    cate = input ("Enter book Category : ")
    statusb = input ("Enter book Status : ")
    sql = "INSERT INTO books(Title, Author, Category, Status) values(%s, %s, %s, %s)"
    data = (titlebook, authorb, cate, statusb)
    cursor.execute(sql, data)
    conn.commit()
    print("Book add! Thank you!")
    print("="*30)
    input ("Press Enter to go back.....")
    clear()
def view():
    cursor.execute("select * from books")
    result = cursor.fetchall()
    if result :
        print("===== List of book =====")
        for row in result :
            print (row)
            print ("="*30)
        print ("All of List!")
    else :
        print ("No more book!")
    input("\nPress Enter to go back.....")
    clear()
def search():
    print ("===== Welcome to Search your book =====")
    searchbook = input ("Enter Book title : ")
    sql = "select * from books WHERE Title LIKE %s"
    cursor.execute(sql, ("%" + searchbook + "%",))
    record = cursor.fetchall()
    if record :
        for row in record :
            print (row)
            print ("Found your book!")
            print ("="*30)
            input ("\nPress Enter to go back..... ")
            clear()
    else :
         print ("Your book not found!")
         print ("="*30)
         input ("\nPress Enter to go back..... ")
         clear()
def update ():
    print("===== Update book =====")
    id = int (input("Enter Book ID : "))
    new_title = input ("Enter New title : ")
    new_author = input ("Enter New Author name : ")
    new_category = input ("Enter new Category : ")
    new_status = input ("Enter new Status : ")
    sql = "update books set Title=%s, Author=%s, Category=%s, Status=%s where id=%s"
    data = (new_title, new_author, new_category, new_status, id)
    cursor.execute(sql,data)
    conn.commit()
    print("Book Update!")
    print("="*30)
    input ("Press Enter to go back.....")
    clear()
def tran():
    print("===== Convert into CSV ( Excel ) =====")
    cursor.execute("select * from books")
    data = cursor.fetchall()
    with open ("Library.csv", "w", newline=" ") as file :
        write = csv.writer(file)
        write.writerow(["ID", "Title", "Author", "Category", "Status"])
        write.writerow(data)
    print("Successful Convert!")
    print("="*30)
    input ("Press Enter to go back.....")
    clear()
def menu():
    print ("Welcome to Library")
    print ("1 Add new book")
    print ("2 View list book")
    print ("3 Search book")
    print ("4 Update book")
    print ("5 Export book to CSV")
    print("6 to Exit")
    print ("="*30)
def main():
    while True :
        menu()
        ch = input ("Enter your choice here : ")
        clear()
        if ch == '1' : add()
        elif ch == '2' : view()
        elif ch == '3' : search()
        elif ch == '4' : update()
        elif ch == '5': tran()
        elif ch == '6':
            print("Thanks you! Have a nice day!")
            print ("-"*30)
            break
        else : input ("Wrong Choice, Press Enter to Try Again!")
        clear()
main()