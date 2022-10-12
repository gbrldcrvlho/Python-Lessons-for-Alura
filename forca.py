import random

def jogar():

    mensagem_abertura()
    palavra_secreta = solicitar_palavra_secreta()
    letras_acertadas = solicitar_letras_acertadas(palavra_secreta)

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



def mensagem_abertura():

    print('*********************************')
    print('***Bem vindo ao jogo da Forca***!')
    print('*********************************')

def solicitar_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def solicitar_letras_acertadas(palavra):
    return ["_" for letra in palavra]

if (__name__ == "__main__"):
    jogar()