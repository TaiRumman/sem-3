# print pattern a
#               a b
#               a b c
#               a b c d
#               a b c d e . using python and loop.

n=int(input("Enter The Number:"))

for i in range (65,n):
    for j in range (65,i+1):
        print (chr(j),end=" ")
    print( )