l1=[2,5,7,9]
l2=[]
for i in l1:
    l2.append(i**2)
print(l2)

l2=[i**2 for x in l1 if x>5]
print(l2)
even=[x for x in l1 if x%2==0]
print("even numbers:", even)
odd=[x for x in l1 if x%2!=0]
print("odd numbers:", odd)