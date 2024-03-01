str="a4b3c2"
op=" "
for ch in str:
    if ch.isalpha():
        x=ch
    else:
        d=int(ch)
        op=op+x*d
print(op)


