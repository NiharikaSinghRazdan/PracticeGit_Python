# Write a Python function to multiply all the numbers in a list.
def multiply_number(mylist):
    result=1
    for no in mylist:
        result=result*no
    print("Result= {}".format(result))
multiply_number([1,2,3,5])