#Write a function that returns the lesser of two given numbers if both numbers are even, but returns the 
#greater if one or both numbers are odd

def check_num(a,b):
    if (a%2==0 and b%2==0):
        if a<b:
            print (a)
        else:
            print (b)
    else:
        if a>b:
            print (a)
        else:
            print (b)
print(check_num(7,5))
        