import random

def jogar():

    print('*********************************')
    print('***Bem vindo ao jogo da Forca***!')
    print('*********************************')

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    letras_acertadas = ["_" for letra in palavra_secreta]

    # letras_faltando = str(letras_acertadas.count('_'))
    # print('Aindam faltam acertar {} letras'.format(letras_faltando))

    enforcou = False
    acertou = False
    tentativas = 0

    print(letras_acertadas)

    while (not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            tentativas += 1

        enforcou = tentativas == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print('Voce ganhou!')
    else:
        print('Voce perdeu!')
    print('Fim de Jogo!')

if (__name__ == "__main__"):
    jogar()