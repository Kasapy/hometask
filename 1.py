x = input()
y = input()

if x.isdigit() and y.isdigit():
    x = int(x)
    y = int(y)
    print(abs(x - y))
else:
    print(x + y)
