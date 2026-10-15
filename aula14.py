# Aqui temos um exemplo de formatação de strings usando o método `format()`. 
# Esse método permite inserir valores em uma string de forma organizada, 
# utilizando chaves `{}` como marcadores para os valores que serão substituídos.

a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(nome1=a, nome2=b, nome3=c) # Significa que o valor de `a` será 
# inserido onde está `{nome1}`, o valor de `b` onde está `{nome2}` 
# e o valor de `c` onde está `{nome3}`. O `:.2f` indica que queremos formatar 
# o número `c` com duas casas decimais.

print(formato)