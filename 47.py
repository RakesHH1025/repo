str1 = "Welcome to USA usa awesome, isn't it?"
str=str1.lower()
print(str)
s="usa"
str2=str.split(' ')
count=0
for i in str2:
    if i==s:
        count=count+1
print(count)

str2=str.split(' ')
str=str2.count(s)
print(str)

