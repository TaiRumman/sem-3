unit = int ( input ("Enter The Unit:") )
if ( unit <= 100 ):
    print ( "Total Bill Is:",unit * 2)
elif ( unit > 100 and unit <= 200):
    print ( "Total Bill Is:",unit * 3)
elif ( unit > 200 and unit <= 300):
    print ( "Total Bill Is:",unit * 5)
else: 
    print ( "Total Bill Is:",unit * 7)