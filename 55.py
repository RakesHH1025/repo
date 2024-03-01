num=[1,1,2,2,3,4,5,6,55,6,6,6,7]
number=[ ]
for i in num:
    if i not in number:
        number.append(i)
print(number)