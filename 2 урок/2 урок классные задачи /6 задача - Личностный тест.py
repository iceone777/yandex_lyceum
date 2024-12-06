print('Любите ли вы котиков? Ответьте да или нет.')
question_1 = input()
print('Умеете ли вы программировать? Ответьте да или нет.')
question_2 = input()
if question_1 == 'да' and question_2 == 'да':
    print('Ты крут!')
elif question_1 == 'нет' and question_2 == 'нет':
    print('ТЫ НЕ УМЕЕШЬ ПРОГАТЬ, И ЕЩЕ НЕ ЛЮБИШЬ КОТОВ?!')
elif question_1 == 'да' and question_2 == 'нет':
    print('Ты обизательно научишься програмировать ;)')
elif question_1 == 'нет' and question_2 == 'да':
    print('Не любить котов? Не разговаривай со мной')
else:
    print('ERROR')
    print('А ты чо думал, отвечай правильно!!!')