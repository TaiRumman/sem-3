a,b,c,d =(input ("Enter Value:")).split(",")
if a>b and a>c and a>d:
    print("Maximum No Is A=",a)
elif b>a and b>c and b>d:
    print("Maximum No Is B=",b)
elif c>a and c>b and c>d:
    print("Maximum No Is C=",c)
else:
    print("Maximum No Is D=",d)