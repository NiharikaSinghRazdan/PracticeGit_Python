#print traingle
x=1
n=3

while x<=n:  
    y=n 
    while y>x:
        print(end=' ') 
        y=y-1 
    z=1       
    while z<=x:
        print("*", end=' ') 
        z=z+1          
    print("\r")
    x=x+1
