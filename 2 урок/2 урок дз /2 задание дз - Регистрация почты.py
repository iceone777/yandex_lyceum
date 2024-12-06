a = input()
b = input()
if '@' in a:
    print('Некорректный логин')
elif '@' not in b:
    print('Некорректный адрес')
else:
    print('OK')