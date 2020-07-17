#Enter the value and identify whether it is even or odd
def odd_even(number):
    if (number%2==0):
        if (number%4==0):
            print("Number {} is divisible by 4".format(number))
        print("Number {} is even". format(number))
    else:
        print("NUmber {} is odd".format(number))
number=int(input("Enter the number :"))
odd_even(number)