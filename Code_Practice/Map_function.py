#Use of Map function
def square(number):
    return number**2

my_nums=[1,2,3,4,5]

#print the output in new lines
for item in map(square,my_nums):
    print(item)

#print the output in list
my_list=list(map(square,my_nums))
print(my_list)
 
# Check length of string given in list and find out whether it is even or odd
def my_string(string1):
    if len(string1)%2==0:
        print("String {} is even".format(string1))
    else:
        print("String {} is odd".format(string1))

my_list1=["Niharika","Kaka","Chooja","Siddh"]
for item in map(my_string,my_list1):
    print(item)

