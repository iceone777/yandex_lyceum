line_1 = float(input())
line_2 = float(input())
line_3 = str(input())
if line_3 == '+':
    print(line_1 + line_2)
elif line_3 == '-':
    print(line_1 - line_2)
elif line_3 == '*':
    print(line_1 * line_2)
elif line_2 != 0 and line_3 == '/':
    print(line_1 / line_2)
else:
    print("888888")
