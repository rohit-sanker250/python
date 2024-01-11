num=int(input("cost of the bike"))
x=num*(15/100)
y=num*(10/100)
z=num*(5/100)

if num>=100000:
    print(x)
elif num>=50000:
    print(y)
elif num<=100000:
    print(y)
elif num <=5000:
    print(z)            