age = int ( input ( " Enter The Age: " ))
if ( age < 5 ):
    print ( " FREE... " )
elif ( age >= 5 and age <= 12 ):
    print ( " 100_rs " )
elif ( age >= 13 and age <= 59 ):
    print ( " 200_rs " )
elif ( age >= 60 ):
    print ( " 150_rs " )
else:
    print ( " Invalid Choice " )