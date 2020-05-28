# Write a function takes a two-word string and returns True if both words begin with same letter
def check_letter(a):
    mylist=a.split()
    first_word=mylist[0]
    sec_word  =mylist[1]
    if (first_word[0].upper()==sec_word[0].upper()) or (first_word[0].lower()==sec_word[0].lower()):
        print (True)
    else:
        pass
print(check_letter("Test thing"))
        
    