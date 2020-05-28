#Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. 
#If not, return False
def check_num(a,b):
    if ((a==20 or b==20) or (a+b==20)):
        print(True)
    else:
        pass
print(check_num(10,5))