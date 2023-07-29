e0, e1 = 0, 0                           # Variáveis para o somatório do primeiro e segundo exército

n, m, s = map(int, input().split())     # Entradas de n, m e s

coef = n / m                            # Coeficiente angular da linha do rio

for _ in range(s):                          # Loop para cada soldado

    x, y, h = map(int, input().split())     # Entrada de x, y e h

    if x < y * coef:                        # Caso o soldado esteja acima do rio

        e0 += h                             # Faz o somatório para o primeiro exército
    else:                                   # Caso o soldado esteja abaixo do rio

        e1 += h                             # Faz o somatório para o segundo exército

print("{0} {1}".format(e0, e1))     # Exibe o resultado
