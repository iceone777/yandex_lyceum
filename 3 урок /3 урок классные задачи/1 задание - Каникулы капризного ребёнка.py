city_1 = input()
city_2 = input()
condition_1 = city_1 == 'Тула' and city_2 == 'Пенза'
condition_2 = city_1 == 'Тула' or city_2 == 'Пенза'
condition_3 = city_1 != city_2
if not condition_1 and condition_2 and condition_3:
    print('ДА')
else:
    print('НЕТ')