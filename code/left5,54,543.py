# print pattern            5
#                        5 4
#                      5 4 3
#                    5 4 3 2
#                  5 4 3 2 1 .., using python...
n=5
#k=4
for i in range (1,n+1):
    for j in range (1,(n-i)+1): # range (1,k+1):
        print(" ",end="")
    #k=k-1
    for j in range (5,5-i,-1):
        print(j,end="")
    print()