import random

def jogar():

    mensagem_abertura()
    palavra_secreta = solicitar_palavra_secreta()
    letras_acertadas = solicitar_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    tentativas = 0

    while (not enforcou and not acertou):

        chute = solicitar_chute()

        if (chute in palavra_secreta):
            seleciona_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            tentativas += 1

        enforcou = tentativas == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        mensagem_sucesso()
    else:
        mensagem_fracasso()


def mensagem_abertura():

    print('*********************************')
    print('***Bem vindo ao jogo da Forca***!')
    print('*********************************')

def solicitar_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

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

def seleciona_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def mensagem_sucesso():
    print('Voce ganhou!')

def mensagem_fracasso():
    print('Voce perdeu!')

if (__name__ == "__main__"):
    jogar()