list1=[1, 2, 3]
list2=['a','b','c']
list3=['x','y','z']
zippedlist=zip(list1, list2, list3)
result=list(zippedlist)
print(result)

unzipped_list=zip(*result)
print(unzipped_list)

unzipped_result= [list(item) for item in unzipped_list]
print(unzipped_result)