txt_1 = input()
txt_2 = input()
txt_3 = input()
usl_1 = ((txt_1 == 'раз' or txt_1 == 'один') and txt_2 == 'два' and txt_3 == 'три') 
if usl_1 or (txt_1 == '1' and txt_2 == '2' and txt_3 == '3'):
    print('ГОРИ')
else:
    print('НЕ ГОРИ')