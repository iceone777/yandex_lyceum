z = input()
(list(z))
max_z = max(z)
min_z = min(z)
for ost_z in z:
    if (ost_z != max_z) & (ost_z != min_z):
        break
if ((int(min_z) + int(max_z)) / 2 == int(ost_z)):
    print('Вы ввели красивое число')
else:
    print('Жаль, вы ввели обычное число')