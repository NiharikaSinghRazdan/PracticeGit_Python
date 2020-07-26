# Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not
# have any punctuation

import string

def Pangram(str1, alphabet=string.ascii_lowercase):
#create the set of alphabets
    alphaset=set(alphabet)
    print(alphaset)
# replace method takes only 3 arguments
    str1=str1.replace(' ','')
    str1=str1.lower()
    str1=set(str1)
    print(str1)
    if str1==alphaset:
        print("Pangram")
    else:
        print("Not Pangram")
Pangram("The quick brown fox jumps over the lazy dog")





