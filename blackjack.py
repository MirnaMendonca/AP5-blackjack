import random

def criar_baralho():
    baralho = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
    random.shuffle(baralho)
    return baralho

def calcular_pontuacao(mao):
    pontuacao = 0
    ases = 0
    for carta in mao:
        if carta.isdigit():
            pontuacao += int(carta)
        elif carta in ['J', 'Q', 'K']:
            pontuacao += 10
        elif carta == 'A':
            ases += 1
            pontuacao += 11
    while pontuacao > 21 and ases:
        pontuacao -= 10
        ases -= 1
    return pontuacao

def jogar_blackjack():
    baralho = criar_baralho()
    mao_jogador = [baralho.pop(), baralho.pop()]
    mao_crupie = [baralho.pop(), baralho.pop()]

    print("Mão do crupiê:", mao_crupie[0])
    print("Sua mão:", mao_jogador)
    mostrar_soma = input("Deseja mostrar sua pontuação a cada jogada? (s/n):")
    if mostrar_soma.lower() == 's':
        print("Sua pontuação é ", calcular_pontuacao(mao_jogador))
    
    while True:
        pontuacao_jogador = calcular_pontuacao(mao_jogador)
        if pontuacao_jogador == 21:
            print("Você tem 21! Você ganhou!")
            break
        elif pontuacao_jogador > 21:
            print("Você estourou! Você perdeu. Sua pontuação foi", pontuacao_jogador)
            break
        else:
            continuar = input("Deseja continuar? (s/n): ")
            if continuar.lower() == 's':
                mao_jogador.append(baralho.pop())
                print("Sua mão:", mao_jogador)
                pontuacao_jogador = calcular_pontuacao(mao_jogador)
                if mostrar_soma.lower() == 's':
                    print("Sua pontuação é", pontuacao_jogador)
            else:
                pontuacao_crupie = calcular_pontuacao(mao_crupie)
                while pontuacao_crupie < 17:
                    mao_crupie.append(baralho.pop())
                    pontuacao_crupie = calcular_pontuacao(mao_crupie)
                print("Mão do crupiê:", mao_crupie)
                if pontuacao_crupie > 21 or pontuacao_crupie < pontuacao_jogador:
                    print("Você ganhou! Sua pontuação foi", pontuacao_jogador)
                elif pontuacao_crupie > pontuacao_jogador:
                    print("Você perdeu. Sua pontuação foi", pontuacao_jogador)
                else:
                    print("Empate! Sua pontuação foi", pontuacao_jogador)
                break

if __name__ == '__main__':
    jogar_blackjack()
