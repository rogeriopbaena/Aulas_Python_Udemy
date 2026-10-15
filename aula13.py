# Aqui temos um exemplo de f-strings, que é uma forma de formatar strings em Python. As f-strings permitem incluir expressões dentro de chaves `{}` que são avaliadas em tempo de execução e inseridas na string resultante.
# Nessa forma, podemos formatar números, como no caso da altura e do IMC, 
# para exibir apenas duas casas decimais usando `:.2f`.

nome = 'Luiz Otávio'
altura = 1.80
peso = 95
imc = peso / altura ** 2

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Luiz Otávio tem 1.80 de altura,
# pesa 95 quilos e seu IMC é
# 29.320987654320987