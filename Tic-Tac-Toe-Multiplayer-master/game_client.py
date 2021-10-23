import socket
import json


def iniciar_jogo():
    client_socket.sendto(str(1).encode(), (host, port))
    client_socket.sendto(name.encode(), (host, port))
    print("Aguardando um adversário ...")
    opponent, address = client_socket.recvfrom(1024)
    opponent = opponent.decode()
    player, address = client_socket.recvfrom(1024)
    player = player.decode()

    while True:
        vez, address = client_socket.recvfrom(1024)
        vez = int(vez.decode())
        tabuleiro, address = client_socket.recvfrom(1024)
        tabuleiro = json.loads(tabuleiro.decode())

        mostrar_jogo(tabuleiro, opponent, player)

        if (vez != 7) and (vez == 1):
            jogada = False
            while not jogada:
                print("Digite a linha:")
                playL = int(input())
                print("Digite a coluna:")
                playC = int(input())
                if tabuleiro[playL][playC] == "":
                    tabuleiro[playL][playC] = player
                    mostrar_jogo(tabuleiro, opponent, player)
                    jogada = True
                    client_socket.sendto(json.dumps(tabuleiro).encode(), (host, 8001))
                else:
                    print("O local escolhido é inválido!!")
                    print("Tente Novamente\n")
                    mostrar_jogo(tabuleiro, opponent, player)
        elif vez == 7:
            msg, address = client_socket.recvfrom(1024)
            print(msg.decode())
            input()
            break


def mostrar_jogo(tabuleiro, opponent, player):
    if player == "X":
        player_opponent = "O"
    else:
        player_opponent = "X"
    print(name+"("+player+")\t\t\t\t\t\t\t\t\t\t"+opponent+"("+player_opponent+")\n\t\t\t\t\t", end="")
    for c in range(0, 3):
        print("  " + str(c) + " ", end="")
    print("\n\t\t\t\t\t ", end="")
    print(" ___" * 3)
    l = 0
    for linha in tabuleiro:
        print("\t\t\t\t\t"+str(l), end="")
        for coluna in linha:
            if coluna == "":
                print("|___", end="")
            else:
                print("|_" + coluna + "_", end="")
        print("|")
        l += 1


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 8000
host = "127.0.0.1"
op = 0
while op != 1:
    
    print(" Digite um nome de Usuário:  ")
    name = input()
    client_socket.sendto(str(0).encode(), ('127.0.0.1', port))
    client_socket.sendto(name.encode(), (host, port))
    op, address = client_socket.recvfrom(1024)
    op = int(op.decode())


while True:

    print("(1)JOGAR")
    print("(2) SAIR")
    op = int(input())

    if op == 1:
        iniciar_jogo()
    elif op == 2:
        break
    else:
        pass