__author__="XSyther"
__version__="1.0"


linha1=["|"]
linha2=["|","|","|"]
linha3=["|","|","|","|","|"]
linha4=["|","|","|","|","|","|","|"]
x=0
jogador=1

def tabuleiro():
    print()
    print()
    print(" ".join(linha1).center(15)+"    Fileira A")
    print(" ".join(linha2).center(15)+"    Fileira B")
    print(" ".join(linha3).center(15)+"    Fileira C")
    print(" ".join(linha4).center(15)+"    Fileira D")
    print()
    print()

while True:

    x=0
    tabuleiro()
    print("Jogardor %i\n".center(20) %jogador)
    fileira=input("Digite a fileira a jogar\nA, B, C Ou D: ")
    quant=int(input("Digite a quantida de traços a serem tirados: "))

    if(fileira.upper()=="A"):
        if(quant>=len(linha1)):
            quant=len(linha1)

        while x < quant:
            if(linha1==[]):
                print("Linha vazia!")
                break

            del linha1[0]
            x+=1




    elif(fileira.upper()=="B"):
        if(quant>=len(linha2)):
            quant=len(linha2)

        while x < quant:
            if(linha2==[]):
                print("Linha vazia!")
                break

            del linha2[0]
            x+=1



    elif(fileira.upper()=="C"):
        if(quant>=len(linha3)):
            quant=len(linha3)

        while x < quant:
            if(linha3==[]):
                print("Linha vazia!")
                break
            del linha3[0]
            x+=1

            
    elif(fileira.upper()=="D"):
        if(quant>=len(linha4)):
            quant=len(linha4)

        while x < quant:
            if(linha4==[]):
                print("Linha vazia!")
                break
            del linha4[0]
            x+=1




    if (linha1==[] and linha2==[] and linha3==[] and linha4==[]):
        print("\nParabens vcs zeraram as fileiras, pelo jeito vcs nao sabem jogar!")
        break

    elif(len(linha1)+len(linha2)+len(linha3)+len(linha4)==1):
        print("\njogador %i Ganhou".center(20) %jogador)
        break
    elif(jogador == 1):
        jogador += 1
    else:
        jogador -= 1

