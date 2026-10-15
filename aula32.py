# Exercicios
"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# Primeira forma de fazer o exercício

entrada = input('Digite um número inteiro: ')

if entrada.isdigit():
    numero = int(entrada)
    if numero % 2 == 0:
        print('O número é par.')
    else:
        print('O número é ímpar.')
else:
    print('O valor digitado não é um número inteiro.')

entrada = input('Digite um número inteiro: ')

# Segunda forma de fazer o mesmo exercício, utilizando uma variável para armazenar o resultado

entrada = input('Digite um número inteiro: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'impar'

    if par_impar:
        par_impar_texto = 'par'

        print(f'O número {entrada_int} é {par_impar_texto}.')
else:
    print('O valor digitado não é um número inteiro.')

# Terceira forma de fazer o mesmo exercício, utilizando Try e Except para tratar a exceção 
# caso o usuário não digite um número inteiro

try:
    entrada_int = float(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'impar'

    if par_impar:
        par_impar_texto = 'par'

        print(f'O número {entrada_int} é {par_impar_texto}.')
except:
    print('O valor digitado não é um número inteiro.')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
entrada = input('Digite a hora em números: ')

try:
    hora = int(entrada)

    if hora <= 0 and hora <= 11:
        print('Bom dia!')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde!')
    elif hora >= 18 and hora <= 23:
        print('Boa noite!')
except:
    print('Por favor, digite um número inteiro válido.')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""
#Primeira forma de fazer o exercício utilizando a função len() para contar o tamanho do nome.
nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto.')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal.')
    else:
        print('Seu nome é muito grande.')
else:
    print('Por favor, digite mais de uma letra.')
