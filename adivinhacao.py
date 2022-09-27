import random

def jogar():
    print('*********************************')
    print('Bem vindo ao jogo da Adivinhacao!')
    print('*********************************')

    numero_secreto = random.randrange(1, 101)
    total_tentativas = 0
    pontos = 1000

    print('**** Niveis de Dificuldades *****')
    print('(1) Facil (2) Medio (3) Dificil')
    print('*********************************')

    nivel = int((input('Escolha um nivel de dificuldade: ')))
    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print('Tentativa {} de {}.'.format(rodada, total_tentativas))

        chute = int(input('Digite um numero entre 1 e 100: '))
        print('Voce digitou: ', chute)

        if (chute < 1 or chute > 100):
            print('O numero digitado deve estar entre 1 e 100!')
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (acertou):
            print(f'Voce acertou e fez {pontos} pontos!')
            break
        else:
            if (maior):
                print('Voce errou! Seu chute foi maior do que o Numero Secreto.')
            elif (menor):
                print('Voce errou! Seu chute foi menor do que o Numero Secreto.')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print(f'O numero secreto foi {numero_secreto}, Fim de Jogo!')

if(__name__ == "__main__"):
    jogar()