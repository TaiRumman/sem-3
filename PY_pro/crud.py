l1 = []

def add():
    pid = int(input("Enter The Food Id: "))
    pname = input("Enter The Food Name: ")
    half_price = int(input("Enter The Food Half Price: "))
    full_price = int(input("Enter The Food Full Price: "))
    mfg_date = input("Enter Food MFG Date (DD-MM-YYYY): ")
    exp_date = input("Enter Food Expire Date (DD-MM-YYYY): ")
    
    d1 = {
        "Pid": pid,
        "Pname": pname,
        "HalfPrice": half_price,
        "FullPrice": full_price,
        "MfgDate": mfg_date,
        "ExpDate": exp_date
    }
    l1.append(d1)

def display():
    print("==================================================================================================")
    print("Food Id | Food Name | Half Price | Full Price | MFG Date    | Expire Date")
    print("==================================================================================================")
    for d1 in l1:
        print(d1["Pid"], "     |", d1["Pname"], "    |", d1["HalfPrice"], "       |", d1["FullPrice"], "       |", d1["MfgDate"], " |", d1["ExpDate"])

def search():
    found = 0
    id = int(input("Enter The ID For Searching:- "))
    for d1 in l1:
        if d1["Pid"] == id:
            found = 1
            break
    if found == 1:
        print("Food item is found:")
        print("==================================================================================================")
        print("Food Id | Food Name | Half Price | Full Price | MFG Date    | Expire Date")
        print("==================================================================================================")
        print(d1["Pid"], "     |", d1["Pname"], "    |", d1["HalfPrice"], "       |", d1["FullPrice"], "       |", d1["MfgDate"], " |", d1["ExpDate"])
    else:
        print("Data Not Found.!")

def sort_price():
    if not l1:
        print("No Food Available For Sort")
        return
    l1.sort(key=lambda x: x["FullPrice"])
    print("Food Items Successfully Sorted By Full Price")
    display()

def update_name():
    found = 0
    id = int(input("Enter The ID For Searching:- "))
    for d1 in l1:
        if d1["Pid"] == id:
            found = 1
            break
    if found == 1:
        print("Food item is found:")
        print(d1["Pid"], " |", d1["Pname"], " |", d1["HalfPrice"], " |", d1["FullPrice"], " |", d1["MfgDate"], " |", d1["ExpDate"])
        
        pname = input("Enter New Food Name: ")
        half_price = int(input("Enter New Half Price: "))
        full_price = int(input("Enter New Full Price: "))
        mfg_date = input("Enter New MFG Date: ")
        exp_date = input("Enter New Expire Date: ")
        
        d1["Pname"] = pname
        d1["HalfPrice"] = half_price
        d1["FullPrice"] = full_price
        d1["MfgDate"] = mfg_date
        d1["ExpDate"] = exp_date
        
        print("Updated Data Successfully:")
        print(d1["Pid"], " |", d1["Pname"], " |", d1["HalfPrice"], " |", d1["FullPrice"], " |", d1["MfgDate"], " |", d1["ExpDate"])
    else:
        print("Data Not Found.!")

def delete():
    found = 0
    id = int(input("Enter The Id For Delete: "))
    for d1 in l1:
        if d1["Pid"] == id:
            found = 1
            break
    if found == 1:
        l1.remove(d1)
        print("Food Item Deleted Successfully!")
    else:
        print("Data Not Found :!")