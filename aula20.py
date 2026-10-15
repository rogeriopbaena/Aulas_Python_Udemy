# Exercício de comparação, que vai receber dois valores do usuário e comparar 
# eles, mostrando o resultado da comparação.

primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

if primeiro_valor > segundo_valor:
    print(f' O primeiro valor {primeiro_valor=} é maior que o segundo valor {segundo_valor=}.')

elif primeiro_valor == segundo_valor:
    print(f' O primeiro valor {primeiro_valor=} é igual ao segundo valor {segundo_valor=}.')

else:
    print(f' O segundo valor {segundo_valor=} é maior que o primeiro valor {primeiro_valor=}.')