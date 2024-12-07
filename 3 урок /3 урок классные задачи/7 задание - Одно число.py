number = float(input())
if abs(number) < 1 / 1000000:
    print(1000000)
else:
    print(1 / number)