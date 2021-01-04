
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da forca****")
    print("*********************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    #Enquanto (TRUE)
    while(not enforcou and not acertou):
        chute = input("Qual letra? ")
        index = 0

        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}".format(chute,index))
            index = index + 1

        print("Jogando...")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()



