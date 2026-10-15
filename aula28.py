"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')

#Aqui você pode usar a avaliação de curto circuito para verificar se 
# nome e idade foram digitados. 
# Se ambos forem verdadeiros (não vazios), o bloco de código dentro do if 
# será executado. Caso contrário, o else será executado.
# Foi utilizado and para garantir que ambas as condições sejam verdadeiras.
# Fazendo isso, você evita a necessidade de escrever uma condição mais longa e 
# complexa.
if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome contém espaços.')
    else:
        print('Seu nome não contém espaços.')
    print(f'Seu nome tem {len(nome)} letras.')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')

else:
    print('Desculpe, você deixou campos vazios.')