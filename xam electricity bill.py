
limit=float(input("enter the electricity unit"))
if limit<=100:
    Amount=0
    print("No charge",Amount)
elif limit<=200:
    p=limit-100
    Amount=p*5
    print("RS 5 per unit is=",Amount)  
elif limit>200:
    x=200*5
    p=limit-200
    Amount=(p*10)+x
    print("RS 10 per unit is=",Amount)       

        