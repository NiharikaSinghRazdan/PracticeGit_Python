# Convert string into list
mystring="This is the new change"
mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)

# Change string into list with different convert format and in one line
mystring1="Hi There"
mylist1 =[letter for letter in mystring1]
print(mylist1)

# Check other usage of this new one liner format to convert string into list
#Check the odd no in list
mylist2=[num for num in range(0,11) if num%2==0]
print(mylist2)

mylist2=[num**2 for num in range(0, 11)]
print(mylist2)