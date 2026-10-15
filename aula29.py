"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input('Vou dobrar o número que vc digitar: ')

# Dessa forma utilizando o try/except, conseguimos tratar o erro e mostrar uma mensagem 
# amigável para o usuário, sem quebrar o código. E ele nos permite colocar o ponto flutuante, 
# então se digitarmos 5.5 ele vai aceitar e mostrar o dobro do número.
try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')

# nesse caso, podemos fazer a mesma coisa com o if/else, só que qundo usamos o isdigit() ele só vai 
# aceitar números inteiros, então se digitarmos 5.5 ele vai dar erro, mostrando assim a mensagem 
# de que não é um número, mesmo sendo um número válido. Tudo porque tem um ponto no meio do número, 
# então o isdigit() não vai aceitar. Ele só aceita números inteiros.
if numero_str.isdigit():
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
else:
     print('Isso não é um número')