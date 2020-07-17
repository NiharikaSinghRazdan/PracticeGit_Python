# write a function that accepts the string and counts upper and lower case letters
def match(str):
    upper_count=0
    lower_count=0
    for item in str:
        if item==item.upper() and item !=" ":
            upper_count=upper_count+1
        elif item==item.lower() and item !=" ":
            lower_count=lower_count+1
    print("Count of lower case letters is {}".format(lower_count))
    print("Count of upper case letter is {}".format(upper_count))
match("This IS nEw")

            