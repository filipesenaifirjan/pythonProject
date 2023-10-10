# -*- coding : utf-8 -*-
casos = int(input())
for caso in range(casos):
    a, b, c, d = [int(i) for i in input().split()]
    exibir = "%.3lf" % ((d - b) / float(c - a))
    novoexbir = [i for i in exibir]
    novoexbir.pop()
    print("".join(novoexbir).replace(".", ","))
