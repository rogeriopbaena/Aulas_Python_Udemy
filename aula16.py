# Agora vamos ver como funciona o if / elif / else, que são estruturas de decisão 
# que permitem executar diferentes blocos de código dependendo das 
# condições avaliadas.
# if / elif      / else
# se / se não se / se não
entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar': # aqui estamos verificando se a entrada do usuário é igual a "entrar"
    print('Você entrou no sistema')

    print(12341234)
elif entrada == 'sair': # aqui estamos verificando se a entrada do usuário é igual a "sair"
    print('Você saiu do sistema')
else:  # aqui estamos tratando o caso em que a entrada do usuário não é nem "entrar" nem "sair"
    print('Você não digitou nem entrar e nem sair.')

print('FORA DOS BLOCOS')
