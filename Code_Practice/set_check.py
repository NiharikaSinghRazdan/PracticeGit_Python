#in set you cannot add similar items. This is the main characteristic of set. There is item 1 and when you try to 
# add item 1 again it will error out.
myset=set()
print(type(myset))
myset.add(1)
print(myset)
myset.add(2)
print(myset)
mylist=[1,1,1,1,1,2,2,3,3]
print(set(mylist))

