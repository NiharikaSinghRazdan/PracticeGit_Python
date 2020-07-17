#Check the scope of local, global and eclosed function variables

#global variable
x=50

def check():
    #Enclosed function
    x="Niharika"
    print(x)

    def naming():
        #local variable
        x="Siddharth"
        print(x)    
    naming()
check()
print(x)


#Check the scope of the variables

#global variable
y=20
def scope1(y):
    print(y)
    #local variable
    y=40
    print(y)
scope1(10)
print(y)

# Suppose you want your global variable to accept the value given inside the functions as local/enclosed
# variable

#global variable
x=50
def scope2():
    global x
    print(x)
    #local variable
    x="NEW Value"
    print("Changed value= "+x)
scope2()
print(x)


