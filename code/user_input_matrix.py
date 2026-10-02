n=int(input("enter the row:"))
m=int(input("enter the column:"))
a=[]
for i in range(n):
    row=[]
    for j in range(m):
        x=int(input(f"enter value:"))
        row.append(x)
    a.append(x)
for i in a:
    for x in i:
        print(x,end=" ")
    print(" ")