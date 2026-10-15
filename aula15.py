# Aqui temos um exemplo de como ler entradas do usuário e realizar 
# operações matemáticas com elas.
# Além disso, utilizamos f-strings para formatar a saída de forma clara e legível.
# Tamém é possível utilizar o método `format()` para formatar strings, 
# mas neste exemplo,
# optamos por usar f-strings, que são mais modernas e geralmente mais fáceis de
# E iremos aprender a função `input()` que permite ler entradas 
# do usuário no console.

nome = input('Qual o seu nome? ')
print(f'O seu nome é {nome}')

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')

