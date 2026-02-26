def student_management():
    id = input("ID : ")
    name = input("Name : ")
    sex = input("Sex : ")
    year = input("Year : ")
    sem = input("Semester : ")
    dis = float(input("Discount (%): "))
    pay = float(input("Pay : "))
    net = pay * (1 - dis / 100)
    print("=" * 90)
    print(f"{'ID':<6}{'Name':<15}{'Sex':<6}{'Year':<8}{'Semester':<10}"
          f"{'Discount':<10}{'Pay':<10}{'NetPay':<10}")
    print("=" * 90)
    print(f"{id:<6}{name:<15}{sex:<6}{year:<8}{sem:<10}"
          f"{dis:<10.2f}{pay:<10.2f}{net:<10.2f}")
student_management()
