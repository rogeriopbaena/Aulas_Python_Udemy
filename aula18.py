# Aqui vamos ver como funciona o if / elif / else, que são estruturas de decisão 
# que permitem executar diferentes blocos de código dependendo das condições
# avaliadas.
# Nessa aula ira ser mostrado como usar o debugger do VSCode para debugar 
# o código e ver como ele funciona passo a passo.
# if / elif      / else
# se / se não se / se não

condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = True
# Ai no geral, o if é usado para verificar uma condição, e se essa condição for 
# verdadeira, o bloco de código dentro do if será executado.
# Se a condição for falsa, o programa verifica a próxima condição no elif,
#  e assim por diante.
if condicao1:
    print('Código para condição 1')
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi satisfeita.')

if 10 == 10:
    print('Outro if')

print('Fora do if')