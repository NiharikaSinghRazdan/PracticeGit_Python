#retrun the list where the passed arguments are even
def myfunc(*args):
    mylist=[]
    for item in args:
        if item%2==0:
            mylist.append(item)
        else:
            continue
    print(mylist)
print(myfunc(-2,4,3,5,7,8,10))

# return a string where every even letter is in uppercase and every odd letter is in lowercase
def myfunct(*args):
    mylist1=[]
    for item in args:
        # find the index of the items
        index=args.index(item)
        if (item==item.upper() and index%2==0) or (item==item.lower() and index%2!=0):
            mylist1.append(item)
    print(mylist1)
print(myfunct('A','B','C','D','e',"f"))

# check the index of the list and verify that even is in uppercase and odd index is in lower case
def myfunc1(*args):
    mystring=' '
    mystring_t=args[0]
    print(len(mystring_t))
    for item in range(len(mystring_t)):
        if (item%2==0):
            mystring=mystring+mystring_t[item].upper()
        else:
            mystring=mystring+mystring_t[item].lower()
    print(mystring)
print(myfunc1("supercalifragilisticexpialidocious"))

# print the argument in upper and lowercase alternate
def myfunc2(*args):
    mystring_total=args[0]
    c_string=' '
    for item in mystring_total:
        index1=mystring_total.index(item)
        if (index1%2==0):
            item=item.upper()
            c_string=c_string+item
        else:
            item=item.lower()
            c_string=c_string+item
    print(mystring_total)
    print(c_string)
print(myfunc2("AbcdEFGHijKL"))

                
    