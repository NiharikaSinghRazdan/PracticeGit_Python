#function to compute the volume of a sphere

def volume(r):
    volume_sphere=(4/3)*(22/7)*r**3
    print("Volume of sa sphere is {}".format(volume_sphere))

r=int(input("Enter the radius"))
volume(r)