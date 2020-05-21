#check for loop conditions
#add the items of list and sum of the list
result=0
my_list=[1,2,3,4,5,6,7,8]
for i in my_list:
     result=result+i
     print(result)
result=0
for i in my_list:
     result=result+i
print("The sum of list is {}".format(result))

#check odd and even no in the list
for item in my_list:
     if(item%2==0):
          print("Number {} is even". format(item))
     else:
          print("Number {} is odd".format(item))

