import random

quadro = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

jogadorAtual = "X"
ganhador = None

jogo = True

def printQuadro(quadro):
    print("----------")
    print(quadro[0] + " │ " + quadro[1] + " │ " + quadro[2])
    print("----------")
    print(quadro[3] + " │ " + quadro[4] + " │ " + quadro[5])
    print("----------")
    print(quadro[6] + " │ " + quadro[7] + " │ " + quadro[8])
    print("----------")

def playerAdc(quadro):
    inp = int(input("Digite um número de 1 a 9: "))

    if inp >=1 and inp <= 9:
        if quadro[inp-1] == "-":
          quadro[inp-1] = jogadorAtual
        else:
            print("Lugar ja escolhido")
    else:
        print("Apenas números de 1 a 9")

def checaHorizontal(quadro):
    global ganhador
    if quadro[0] == quadro[1] == quadro[2] and quadro[0] != "-":
        ganhador = quadro[0]
        return True
    elif quadro[3] == quadro[4] == quadro[5] and quadro[3] != "-":
        ganhador = quadro[3]
        return True
    elif quadro[6] == quadro[7] == quadro[8] and quadro[6] != "-":
        ganhador = quadro[6]
        return True

def checaVertical(quadro):
    global ganhador
    if quadro[0] == quadro[3] == quadro[6] and quadro[0] != "-":
        ganhador = quadro[0]
        return True
    elif quadro[1] == quadro[4] == quadro[7] and quadro[1] != "-":
        ganhador = quadro[1]
        return True
    elif quadro[2] == quadro[5] == quadro[8] and quadro[2] != "-":
        ganhador = quadro[2]
        return True

def checaDiagonal(quadro):
    global ganhador
    if quadro[0] == quadro[4] == quadro[8] and quadro[0] != "-":
        ganhador = quadro[0]
        return True
    elif quadro[2] == quadro[4] == quadro[6] and quadro[2] != "-":
        ganhador = quadro[2]
        return True

def checaEmpate(quadro):
    global jogo
    if "-" not in quadro:
        printQuadro(quadro)
        print("Jogo empatado")
        jogo = False

def checaVencedor():
    global jogo
    if checaDiagonal(quadro) or checaVertical(quadro) or checaHorizontal(quadro):
        printQuadro(quadro)
        print(f"O ganhador foi {ganhador}")
        jogo = False

def mudarJogador():
    global jogadorAtual
    if jogadorAtual == "X":
        jogadorAtual = "O"
    else:
        jogadorAtual = "X"

def rival(quadro):
    while jogadorAtual == "O":
        posicao = random.randint(0, 8)
        if quadro[posicao] == "-":
            quadro[posicao] = "O"
            mudarJogador()

while jogo:
    printQuadro(quadro)
    playerAdc(quadro)
    checaVencedor()
    checaEmpate(quadro)
    mudarJogador()
    rival(quadro)
    checaVencedor()
    checaEmpate(quadro)