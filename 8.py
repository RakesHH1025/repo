input=[1,2,3,4,5,6,7,8,9,10]

first=input.pop(0)
last=input.pop(-1)

input.append(first)
input.insert(0,last)
print(input)
