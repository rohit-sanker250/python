def my_list(lists,index):
    try:
        print("the elements is:",lists(index))
    except IndexError e:
        raise exception("index is nout of range",e)
    
    limit=int(input("enter the ist"))
    list1=[]
    for i in range(limit):
        number=int(input("enter the number:"))
        list1.append(number)

    print("the list elements are:",list1) 
    index=int(input("enter the index of element:")
    my_list(list,index)          )   




