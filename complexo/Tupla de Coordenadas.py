# Crie uma tupla para armazenar coordenadas (x, y) 
# e implemente uma função 
# para calcular a distância entre dois pontos.

from math import sqrt

ponto1 = (3, 7) # indice 0 e 1


def calcular_distancia(p1):
    #Operação com indices 0 e 1
    return sqrt((p1[0] - p1[1])**2)
#0 e 1 nas suas posições
print("Distancia num unico ponto: ", calcular_distancia(ponto1))

point1 = (3, 4) # indice1 - 0 1
point2 = (30, 8) # indice2 - 0 1

def calcular_distancia(p1, p2):
    #Operação com indices 0 e 1
    return sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1]**2))
#0 e 1 nas suas posições
print("Distancia entre dois pontos: ", calcular_distancia(point1, point2))

