str1 = "PyNaTive"
lower=[ ]
upper=[ ]

for i in str1:
    if i.isupper():
        upper.append(i)
    else:
        if i.islower():
            lower.append(i)

print(lower)
print(upper)
res="".join(lower+upper)
print(res)

