a = int(input())
b = int(input())
r = 0
while a - b != 0 or b - a !=0:
    if a > b:
        r = a - b
        a = r
    else:
        r = b - a
        b = r
print(a)
