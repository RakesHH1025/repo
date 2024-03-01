list=[1,2,3,4,5,6,7,8,9,10]
max=list[0]
for i in range(1,len(list)):
    if list[i]>max:
        max=list[i]
print(max)