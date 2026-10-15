# Aqui é a ordem de precedência dos operadores matemáticos:

# 1. (n + n) o parênteses tem a maior precedência, então o que estiver dentro do parênteses será resolvido primeiro.
# 2. ** a exponenciação vem em seguida, então o que estiver dentro do parênteses será resolvido primeiro.
# 3. * / // % a multiplicação, divisão, divisão inteira e módulo vem em seguida, então o que estiver dentro do parênteses será resolvido primeiro.
# 4. + - e por último a adição e subtração, então o que estiver dentro do parênteses será resolvido primeiro.
# A execução da conta é feita da esquerda para a direita, então o que estiver dentro do parênteses será resolvido primeiro.

conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_1)