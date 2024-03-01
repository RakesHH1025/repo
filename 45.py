str1 = "P@#yn26at^&i5ve"
chars=0
digits=0
symbol=0

for i in str1:
    if i.isdigit():
        digits=digits+1
    if i.isalpha():
        chars=chars+1
    else:
        symbol=symbol+1

print(chars)
print(digits)
print(symbol)