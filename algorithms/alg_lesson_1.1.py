"""1. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
"""


print('And = ' + str(5 & 6))
print('Or = '  + str(5 | 6))
print('Xor = ' + str(5 ^ 6))
print ('5 shift right = ' + str(5 >> 1) +'\n' + '5 shift left x2 = ' + str(5 << 2))