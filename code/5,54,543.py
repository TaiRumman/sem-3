# print pattern 5
#               5 4
#               5 4 3
#               5 4 3 2
#               5 4 3 2 1 . using python and loop.

n=int(input("Enter The Number:"))

for i in range (1,6):
    k=5
    for j in range (1,i+1):
        print (k,end=" ")
        k-=1
    print( )