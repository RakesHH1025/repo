# Write a program to display all prime numbers within a range
start = 25
end = 50
count=0
for i in range(start,end+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)