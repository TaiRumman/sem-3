# print pattern            1
#                        1 2   
#                      1 2 3
#                    1 2 3 4
#                  1 2 3 4 5 .., using python...
n=5
#k=4
for i in range (1,n+1):
    for j in range (1,(n-i)+1): # range (1,k+1):
        print(" ",end="")
    #k=k-1
    for j in range (1,i+1):
        print(j,end="")
    print()