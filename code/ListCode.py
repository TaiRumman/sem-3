# print Search a number from list.

l1=[10,50,70,30]
x=int(input("Enter The Number:"))

i=0
flag=0
while i<len(l1):
    if (x==l1[i]):
        flag=1
        break
    i=i+1
if (flag==1):
        print("Value found!!!")
else:
        print("value Not Found")