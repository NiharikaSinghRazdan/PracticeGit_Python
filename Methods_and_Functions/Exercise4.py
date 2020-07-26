# Write a Python function that takes a list and returns a new list with unique elements of the first list
def listing(mylist):
    myset=set(mylist)
    mylist1=list(myset)
    print(mylist1)
listing([1,2,3,1,2,4])