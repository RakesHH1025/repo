list=[0,1,2,3,4,5,6]
x=5
count=0

for i in list:
    if i==x:
        count=count+1
print(count)

from collections import Counter
res=Counter(list)
print(res)
