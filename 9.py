list=["geeks","for","geeks"]
n=len(list)
word="geeks"
N=2
count=0

for i in range(0,n):
    if list[i]==word:
        count=count+1
        if count==N:
            del list[i]
print(list)


