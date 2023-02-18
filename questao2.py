if __name__ == '__main__':

    # Variables:
    numero = int(input('número de nós: '))
    grafo = []
    contador = 0

    # Input Check:
    if numero > 9 or numero < 0:
        print('Número para nós é invalido!!!')
        exit()

    # Matrix Generetor:
    for i in range(numero):
        linha = []
        for j in range(numero):
            if contador == j:
                linha.append(0)
            else:
                linha.append(1)
        grafo.append(linha)
        contador += 1

    # Matrix Printer:
    for i in range(numero):
        for j in range(numero):
            print(grafo[i][j], end=' ')
        print("\n")