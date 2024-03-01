num=[1,2,3,4,5,6,7,9,10]
n=len(num)+1
total=n*(n+1)//2
print(total)
sum=0

for i in num:
    sum=sum+i
print(sum)

res=total-sum
print(res)
