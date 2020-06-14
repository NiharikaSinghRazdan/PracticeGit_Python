str="Kitten"
n=1
new_list=str[0:n]
new_list1=str[n+1:]
print(new_list+new_list1)

#exchange first and last charcaters in string
str_first=str[0]
str_last=str[-1]
str_mid=str[1:-1]
print(str_last+str_mid+str_first)

#print first 3 chars of the string
new_str=str[:3]
print(3*new_str)

#string_splosion('Code') → 'CCoCodCode'
#string_splosion('abc') → 'aababc'
#string_splosion('ab') → 'aab'
str1="Code"
result=""
for i in range(len(str1)):
 result=result+str1[:i+1]
print(result)
