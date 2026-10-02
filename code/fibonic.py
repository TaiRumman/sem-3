# print number of Fibonic series...

n = int ( input ( "Enter The Number:" ))
a=0
b=1
count = 0

while ( count < n ):
    print (a)
    c = a + b
    a = b
    b = c
    count = count + 1