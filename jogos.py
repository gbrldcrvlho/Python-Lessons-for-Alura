import forca
import adivinhacao

def escolha_jogo():
    print('*********************************')
    print('*******Escolha o seu Jogo!*******')
    print('*********************************')

    print('(1) Forca (2) Adivinhacao')

    jogo = int(input('Qual jogo deseja?'))

    if(jogo == 1):
        print('Jogando Forca')
        forca.jogar()
    elif(jogo == 2):
        print('Jogando Adivinhacao')
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolha_jogo()