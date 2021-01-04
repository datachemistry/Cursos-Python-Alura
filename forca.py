import random

def jogar():
    
    abertura()

    palavra_secreta = carregar_palavra_secreta()
    letras_acertadas = ["_" for letra in palavra_secreta]
    print(letras_acertadas)
    
    enforcou = False
    acertou = False
    erros = 0
    
    #Enquanto (TRUE)
    while(not enforcou and not acertou):
        chute = input_chute()

        if(chute in palavra_secreta):
            marcar_chute_correto(palavra_secreta, chute, letras_acertadas)
            
        else:
            erros = erros + 1
            print("Ops, você errou! Faltam {} tentativas.".format(6-erros))
            desenha_forca(erros)
            
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
                

    if(acertou):
        menssagem_ganhador()
    else:
        menssagem_perdedor(palavra_secreta)

    print("Fim do jogo")

def menssagem_ganhador():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def menssagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def marcar_chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0            
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra        
        index = index + 1

def input_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def abertura():

    print("*********************************")
    print("***Bem vindo ao jogo da forca****")
    print("*********************************")

def carregar_palavra_secreta(): 
    arquivo = open("palavras.txt", "r")
    palavras = []
    
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    
    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta 

if(__name__ == "__main__"):
    jogar()