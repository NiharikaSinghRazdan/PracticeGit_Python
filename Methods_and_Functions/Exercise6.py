# Write a Python function that checks whether a word or phrase is palindrome or not.
#Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, 
# e.g., madam,kayak,racecar, or a phrase "nurses run"

def palindrome(phrase):
    string1=""
    for item in phrase:
        if item==" ":
            continue
        else:
            string1=string1+item
    print(string1)
    #reverse the string
    slice2=string1[::-1]
    print(slice2)
    if string1==slice2:
        print("Phrase is Palindrome")
    else:
        print("Phrase is not Palindrome")
palindrome("nurses run")


# There is more simple approach to resolve this problem

def palindrome_check(s):
    s=s.replace('',' ')
    str2=s[::-1]
    if str2==s:
         print("Palindrome")
    else:
         print("Not Palindrome")
palindrome_check("nurses run")

