x = int(input())
y = int(input())
if 3 < x < 12 and 3 < y < 12:
    print({
            '+': x + y,
            '-': x - y,
            '*': x * y,
            '/': x / y if y != 0 else 'Деление на 0'
        }[input()])
