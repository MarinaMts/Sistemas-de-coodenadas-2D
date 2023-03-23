import math

quad1 = quad2 = quad3 = quad4 = 0
coordXMaior = coordYMaior = coordXMenor= coordYMenor = 0
distanciaMenor = float('inf')
distanciaMaior = float('-inf')
tempoInicial = 0

origemX = int(input('Digite a coordenada de origem X: '))
origemY = int(input('Digite a coordenada de origem Y: '))
print(f'Coordenada de origem ({origemX},{origemY})')

N = int(input('Digite quantas coodenadas deseja adicionar: '))

for i in range(N):
    coordX = int(input('Digite a coordenada X: '))
    coordY = int(input('Digite a coordenada Y: '))

    distancia = math.sqrt((coordX - origemX) ** 2 + (coordY - origemY) ** 2)

    if N == 1:
        distanciaMaior = distanciaMenor = distancia
    else:
        if distancia > distanciaMaior:
            distanciaMaior = distancia
            coordXMaior = coordX
            coordYMaior = coordY
        if distancia < distanciaMenor:
            distanciaMenor = distancia
            coordXMenor = coordX
            coordYMenor = coordY

    if coordX > origemX and coordY > origemY:
        print(f'Ponto ({coordX}, {coordY}) esta no 1o quadrante.')
        quad1 =+ 1
    elif coordX < origemX and coordY > origemY:
        print(f'Ponto ({coordX}, {coordY}) esta no 2o quadrante.')
        quad2 =+ 1
    elif coordX < origemX and coordY < origemY:
        print(f'Ponto ({coordX}, {coordY}) esta no 3o quadrante.')
        quad3 =+ 1
    elif coordX > origemX and coordY < origemY:
        print(f'Ponto ({coordX}, {coordY}) esta no 4o quadrante.')
        quad4 =+ 1
    elif coordX == origemX and coordY > origemY or coordY < origemY:
        print(f'Ponto ({coordX}, {coordY}) está sobre o eixo das ordenadas.')
    elif coordX > origemX or coordX < origemX and coordY == origemY:
        print(f'Ponto ({coordX}, {coordY}) está sobre o eixo das abcissas.')

print(f'Ponto {coordXMaior, coordYMaior} é o mais distante, distancia =', format(distanciaMaior , ".2f"))
print(f'Ponto {coordXMenor, coordYMenor} é o menos distante, distancia=', format(distanciaMenor , ".2f"))
print(f'Existe(m) {quad1} ponto(s) no 1º quadrante; {quad2} no 2º quadrante; {quad3} no 3º quadrante e {quad4} no 4º quadrante.')


coordXRobo = int(input('Digite a coordenada X do ponto de origem A do robô: '))
coordYRobo = int(input('Digite a coordenada Y do ponto de origem A do robô: '))
tempoFinal = int(input('Digite por quanto tempo o robô irá caminhar: '))

while tempoInicial < tempoFinal:
    coordYRobo = coordYRobo + 1
    tempoInicial = tempoInicial + 1
    if tempoInicial < tempoFinal:
        coordXRobo = coordXRobo + 1
        tempoInicial = tempoInicial + 1
    if tempoInicial < tempoFinal:
        coordXRobo = coordXRobo + 1
        tempoInicial = tempoInicial + 1

print(f'Ao final da caminhada o robô estará no ponto ({coordXRobo}, {coordYRobo}) do plano cartesiano.')