input=[1,2,3,4,5,6,7,8,9,10]
n=len(input)
max=input[0]
min=input[0]

for i in range(1,n):
    if input[i]>max:
        max=input[i]
print(max)

for i in range(1,n):
    if input[i]<min:
        min=input[i]
print(min)

