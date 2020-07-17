#Write a function that checks whether a number is in a given range (inclusive of high and low)

def range_check(num,low, high):
    if (high>=num>=low):
        print("number is in range")
    else:
        pass
number=int(input("Enter the number"))
lower=int(input("Enter lower range"))
higher=int(input("Enter higher range"))
range_check(number,lower,higher)
