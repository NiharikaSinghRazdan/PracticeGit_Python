def name_age(name,age):
    print("Your name is {}".format(name))
    print("Your age is {}".format(age))
    current_age=age
    current_year=2020
    age_100=100-current_age
    year_100=current_year+age_100
    print("You will be turned 100 in year {}".format(year_100))
print(name_age("Niharika",31))

#This input() method gives you ability to enter the value
name=input("Give me your name :")
print("Your name is "+name)