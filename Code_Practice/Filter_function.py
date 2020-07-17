#findout the even nos in list using filter
def check_even(num):
    return num%2==0

my_list=[1,2,4,6,8,7]
my_list1=list(filter(check_even,my_list))
print(my_list1)
