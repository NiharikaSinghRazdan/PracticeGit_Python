# Lambda functions are tricky if you are not much experienced in Python
# We have used map and filter function by defining regular expression but here we will use Lambda expression

def check_even(num):
    if num%2==0:
        print("Number {} is even".format(num))
    else:
        print("Number {} is odd".format(num))
my_list=[1,4,6,2,3,7,8]
my_list1=list(map(check_even,my_list))
print(my_list1)

def check_odd(numbers):
    return numbers%2!=0
my_listing=[1,2,4,5,8,6,3]
my_listing1=list(filter(check_odd,my_listing))
print(my_listing1)

#see how we are going to use lambda function for both the above case
my_lists=[1,2,4,6,8,3]
my_list2=list(map(lambda num:num**2,my_lists))
print(my_list2)

my_listings=[2,4,3,5,8,7]
my_listing2=list(filter(lambda number:number%2!=0, my_listings))
print(my_listing2)
