# Armstrong number using python...

n=int(input("Enter The Number:"))
temp=n
rev=0

while(n!=0):
    
    rem=n%10
    rev=rev+(rem*rem*rem)
    n=n//10
if (temp == rev):
        print(temp,"Is Armstrong Number")
else:
        print(temp,"Is Not Armstrong Number")
