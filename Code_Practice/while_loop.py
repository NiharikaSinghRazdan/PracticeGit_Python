#start basic while loop
x=0
while x < 10:
    print(x)
    x=x+1

#only print even number by using pass keyword
#pass- it does nothing and move to next statement
x=0
while x<=10:
    if(x%2==0):
        pass
    else:
        print("The number {} is odd".format(x))
    x=x+1

#Break keyword: comes out of the closest loop
#If the number is equals to 5 then come out of the loop
x=0
while x<=10:
    if x==5:
        break
    else:
        print("The number is {}".format(x))
    x=x+1

#Continue keyword: it goes to the top of closest loop
#If the number is 5 then skip it and move with rest of the numbers
x=0
while x<=10:
    if x==5:
        x=x+1
        continue        
    else:
        print("list is getting printed {}".format(x))
    x=x+1