import crud as c1

while True:
    print("\n1.Add Food\n2.Display Food\n3.Search Food\n4.Sort Price\n5.Update Food\n6.Delete Food")
    choice = int(input("Enter The Choice:= "))
    if choice == 1:
        c1.add()
    elif choice == 2:
        c1.display()
    elif choice == 3:
        c1.search()
    elif choice == 4:
        c1.sort_price()
    elif choice == 5:
        c1.update_name()
    elif choice == 6:
        c1.delete()
    else:
        print("Invalid Choice:!")
        break