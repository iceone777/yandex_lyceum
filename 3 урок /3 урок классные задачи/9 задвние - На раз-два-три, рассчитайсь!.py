number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
if number_1 < number_2:
    number_1, number_2 = number_2, number_1
if number_2 < number_3:
    number_2, number_3 = number_3, number_2
if number_1 < number_2:
    number_1, number_2 = number_2, number_1
print(number_1)
print(number_2)
print(number_3)