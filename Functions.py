from random import choice

# Função que muda as peças de lugar!!!
def Mudar_lugar(pos1, pos2, matriz):
    lugar1 = matriz[pos1 // 10 - 1][pos1 % 10 - 1]
    lugar2 = matriz[pos2 // 10 - 1][pos2 % 10 - 1]
    matriz[pos1 // 10 - 1][pos1 % 10 - 1] = lugar2
    matriz[pos2 // 10 - 1][pos2 % 10 - 1] = lugar1

# Função que cria a matriz já misturada.
def CriaMatriz():
    matriz = [[10, 11, 12, 13],
              [14, 15, 16, 17],
              [18, 19, 20, 21],
              [22, 23, 24, '']]

    jogadas = 0
    vazio = 44  # Posição que está vazia.

    while jogadas <= 100:
        lista = []
        
        # Criando uma lista com as posições das peças que são possiveis mexer
        if 0 <= (vazio // 10 - 1) < 4 and 0 <= ((vazio % 10 - 1) + 1) < 4:
            lista.append((vazio // 10 * 10) + (vazio % 10 + 1))

        if 0 <= (vazio // 10 - 1) < 4 and 0 <= ((vazio % 10 - 1) - 1) < 4:
            lista.append((vazio // 10 * 10) + (vazio % 10 - 1))

        if 0 <= ((vazio // 10 - 1) - 1) < 4 and 0 <= (vazio % 10 - 1) < 4:
            lista.append((vazio // 10 * 10 - 10) + (vazio % 10))

        if 0 <= ((vazio // 10 - 1) + 1) < 4 and 0 <= (vazio % 10 - 1) < 4:
            lista.append((vazio // 10 * 10 + 10) + (vazio % 10))

        numero = choice(lista)  # Sorteando a posição a ser mexida

        Mudar_lugar(numero, vazio, matriz)  # Chamando a função que mudar o lugar das peças

        vazio = numero   # Vazio passa a ser o número sorteado

        jogadas += 1

    # Retorna uma matriz misturada, possível de ser ordenada.    
    return matriz
