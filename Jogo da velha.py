def velha(jogo):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(jogo[i][j], "|", end=" ")
        print("\n-------------")

def verificar_vitoria(jogo, jogador):
    for i in range(3):
        if jogo[i][0] == jogo[i][1] == jogo[i][2] == jogador:
            return True
    for j in range(3):
        if jogo[0][j] == jogo[1][j] == jogo[2][j] == jogador:
            return True
    if jogo[0][0] == jogo[1][1] == jogo[2][2] == jogador:
        return True
    if jogo[0][2] == jogo[1][1] == jogo[2][0] == jogador:
        return True
    return False

def jogar():
    jogo = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    while True:
        velha(jogo)
        print("É a vez do jogador", jogador_atual)
        linha = int(input("Digite o número da linha (0, 1 ou 2): "))
        coluna = int(input("Digite o número da coluna (0, 1 ou 2): "))
        if jogo[linha][coluna] == " ":
            jogo[linha][coluna] = jogador_atual
            if verificar_vitoria(jogo, jogador_atual):
                print("O jogador", jogador_atual, "venceu")
                break
            elif " " not in jogo[0] and " " not in jogo[1] and " " not in jogo[2]:
                print("Empate")
                break
            jogador_atual = "O" if jogador_atual == "X" else "X"
        else:
            print("Essa posição já está ocupada")

jogar()