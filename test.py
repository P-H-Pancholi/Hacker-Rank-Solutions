a = '10101'
a = int(a,2)
b = '11101'
b = int(b,2)
c = bin(a|b)
print(c.count('1'))
