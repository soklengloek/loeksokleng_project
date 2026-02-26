#Input
def input_fun() :
    print ("EDC Management System")
    print ("="*20)
    id = int(input("Customer ID : "))
    name = (input("Name : "))
    loc = (input("Location: "))
    old = int(input("OldKw : "))
    new = int(input("NewKw : "))
    return id , name , loc , old , new
#Process
def processing (total) :
    if total <= 10 :
        rate = 380
    elif total <= 50 :
        rate = 480
    elif total <= 200 :
        rate = 610
    else :
        rate = 730
    return rate
#Output
def output (id , name , loc , old , new ):
    print ("="*20)
    print ("\t\tReceipt")
    print ("Customer ID :" , id)
    print ("Name : " , name )
    print ("Location : " , loc)
    print ("OldKW : " , old , "KW" ," ","\nNewKW : " , new , "KW")
    print ("="*20)
    print ( total , "KW", "*" , rate , "Rate", "=" , pay , "Riel")
    print ("TotalKW : " , total , "KW")
    print ("Payment : " , pay , "Riel")
id, name, loc, old, new = input_fun()
total = new - old
rate = processing (total)
pay = (total * rate)
output(id,name,loc,new,old,)