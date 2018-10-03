from time import sleep
from Functions import CriaMatriz, Mudar_lugar


def verificar_jogada(pos1, matriz_gerada):

    # Se [...,..., pos1,''] (Uma posição depois estiver vazia)
    if pos1 % 10 < 4 and 11 <= pos1 <= 44 and matriz_gerada[pos1 // 10 - 1][(pos1 % 10 - 1) + 1] == '':
        posVazia = (pos1 // 10 * 10) + ((pos1 % 10) + 1)
        Mudar_lugar(pos1, posVazia, matriz_gerada)  # Chamando a funçção que muda a peça de lugar
        return True

    # Se ['', pos1,...,... ]  (Uma posição antes estiver vazia)
    elif pos1 % 10 <= 4 and 11 <= pos1 <= 44 and matriz_gerada[pos1 // 10 - 1][(pos1 % 10 - 1) - 1] == '':
        posVazia = (pos1 // 10 * 10) + (pos1 % 10 - 1)
        Mudar_lugar(pos1, posVazia, matriz_gerada)   # Chamando a funçção que muda a peça de lugar
        return True

    # Se [...,...,  '' ,...]
    #    [...,..., pos1,...]  (Uma posição acima estiver vazia)
    elif pos1 % 10 <= 4 and 11 <= pos1 <= 44 and matriz_gerada[(pos1 // 10 - 1) - 1][pos1 % 10 - 1] == '':
        posVazia = ((pos1 // 10 - 1) * 10) + (pos1 % 10)
        Mudar_lugar(pos1, posVazia, matriz_gerada)   # Chamando a funçção que muda a peça de lugar
        return True

    # Se [...,..., pos1,...]
    #    [...,...,  '' ,...]  (Uma posição abaixo estiver vazia)
    elif pos1 % 10 <= 4 and 11 <= pos1 < 44 and matriz_gerada[(pos1 // 10 - 1) + 1][pos1 % 10 - 1] == '':
        posVazia = ((pos1 // 10 + 1) * 10) + (pos1 % 10)
        Mudar_lugar(pos1, posVazia, matriz_gerada)   # Chamando a funçção que muda a peça de lugar
        return True
    else:
        print('\n \033[0;31;40mJOGADA INVALIDA!!!\033[m\n')
        return False

def verificaSeVenceu(matriz_gerada):
   matriz_ganhou = [[10, 11, 12, 13], [14, 15, 16, 17], [18, 19, 20, 21], [22, 23, 24, '']]
   if matriz_gerada == matriz_ganhou:
       return True
   else:
       return False

def main():
    matriz_gerada = CriaMatriz()    # Chamando função que cria matriz

    jogando = True
    count = 0
    print('')
    while jogando:
        count += 1  # Conta a quantidade de jogadas
        # Mostra a matriz
        for a in range(4):
            print('\033[1;35;m', matriz_gerada[a], '\033[m')

        verifica = False
        while not verifica:
            pos1 = int(input('\033[34m Escolha a peça a ser mexida:\033[m'))
            verifica = verificar_jogada(pos1, matriz_gerada)
        venceu_ou_nao = verificaSeVenceu(matriz_gerada)

        # Quantidade de vezes jogadas para a pergunta (continuar ou desistir) ser feita.
        if count == 50 or count == 100 or count == 150 or count == 200 or count == 250 and 300:
            jogando = bool(int(input(' \033[1;30;47m >>>>>> Deseja ->  continuar(1) ou desistir (0):\033[m ')))

        if venceu_ou_nao:
            print('--=---0---=--' * 4)
            print(' \033[1;36mParabéns! Vc conseguiu vencer!\033[m\n Total de jogadas: \033[34m{}\033[m'.format(count))
            print('--=---0---=--' * 4)
            print(' ')
            count = 0
            sleep(4)
            jogando = bool(int(input('\033[1;30;47m >>>>>>>> Deseja: Jogar novamente(1) ou Finalizar(0):\033[m ')))
            if jogando:
                matriz_gerada = CriaMatriz()
            else:
                print(' Finalizando....\n')
                sleep(2)
                print(' Parabéns! Foi um bom jogo!\n')

        if venceu_ou_nao == jogando == False:
            sleep(2)
            print('\n \033[7;33maahh, Que pena!!! Você estava fazendo um bom jogo!\033[m \n')

#Chamada da função "main" para iniciar o jogo.
main()
