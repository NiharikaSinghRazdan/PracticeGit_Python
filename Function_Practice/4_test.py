# Write a function that capitalizes the first and fourth letters of a name
def letter_change(a):
    letter=' '
    for item in range(len(a)):
        if item==0 or item==3:
            letter=letter+a[item].upper()
        else:
            letter=letter+a[item]
    print(letter)
print(letter_change("Nisidd"))

# other way of doing it
def letter_change1(a):
    letter_1=a[0]
    mid_letters=a[1:3]
    fourth_letter=a[3]
    last_letters=a[4:]
    return letter_1.upper()+mid_letters+fourth_letter.upper()+last_letters
print(letter_change1("Nihasidd"))

