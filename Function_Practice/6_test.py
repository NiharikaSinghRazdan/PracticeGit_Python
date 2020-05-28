# Given an integer n, return True if n is within 10 of either 100 or 200
# almost_there(90) --> True
# almost_there(104) --> True

def num_check(num):
    return (abs(100-num)<=10) or (abs(200-num)<=10)         
print(num_check(212))

