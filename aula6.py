# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool
print(1 + 1) # int
print(1 + 1.0) # float
print('a' + 'b') # str
print(int('1'), type(int('1'))) #Aqui o int() converte a string '1' para o tipo inteiro
print(type(float('1') + 1)) #Aqui o float() converte a string '1' para o tipo float e depois soma com 1, que é do tipo int, resultando em um float
print(bool(' ')) #Aqui o bool() converte a string ' ' para o tipo booleano
print(str(11) + 'b') #Aqui o str() converte o número 11 para o tipo string