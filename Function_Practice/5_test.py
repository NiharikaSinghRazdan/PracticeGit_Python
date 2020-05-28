# Given a sentence, return a sentence with the words reversed
def reverse_word(a):
    mylist=a.split()
    print(mylist)
    mylist.reverse()
    sortedlist=mylist
    print(sortedlist)
print(reverse_word('I am home'))