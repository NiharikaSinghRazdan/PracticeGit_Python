#check the list and print the list which has number less than 5
list_1=[1,1,3,6,10,5,2,12,15]
list_2=[]
for item in list_1:
    if item<=5:
        list_2.append(item)
print(list_2)