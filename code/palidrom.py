# palidrom number using python...

n=int(input("Enter The Number:"))
temp=n
rev=0

while(n!=0):
    
    rem=n%10
    rev=rev*10+rem
    n=n//10
if (temp == rev):
        print(temp,"Is Palidrom Number")
else:
        print(temp,"Is Not Palidrom Number")
