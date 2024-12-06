print('Назовите себя, пожалуйста!')
name = input()
print('Введите текст.')
text_1 = input()
print('Повторите текст.')
text_2 = input()
if text_1 == text_2:
    print(name + ', введено верно!')
else:
    print(name + ', пока не получилось, попробуйте снова!')