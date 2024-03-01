r1="Ravi"
r2="teja"
res=' '
i,j=0,0

while i<len(r1) or i<len(r2):
    res=res+r1[i]+r2[i]
    i=i+1
    j=j+1
print(res)

r1="Ravikiran"
r2="Teja"
i,j=0,0
op=" "

while i<len(r1) or i<len(r2):
    if i<len(r1):
        op=op+r1[i]
        i=i+1
    if j<len(r2):
        op=op+r1[j]
        j=j+1
print(op)

