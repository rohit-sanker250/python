my_list=[]
print("numbers=",my_list)
for i in range (3):
    digit= int(input("enter the element"))
    my_list.append(digit)
print(my_list)
my_variable= True
while my_variable:
    i=0
    my_variable=False
    while i<len(my_list)-1:
        if my_list[i]>my_list[i+1]:
            my_list[i],my_list[i+1]=my_list[i+1],my_list[i]
            my_variable=True
        i+=1
    third_largest =my_list[-3]
    print("third largest number :",third_largest)           