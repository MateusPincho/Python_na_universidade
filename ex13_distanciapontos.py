#Mateus Pincho de Oliveira(121110103)
#Exercicio 13 

from cmath import sqrt
import math 

def distancia (xa, ya, xb, yb):
    dab = math.sqrt(((xb-xa)**2) + ((yb-ya)**2))
    return dab 

xa = float(input('Informe a abscissa do ponto A:'))
ya = float(input('Informe a ordenada do ponto A:'))
xb = float(input('Informe a abscissa do ponto B:'))
yb = float(input('Informe a ordenada do ponto B:'))

print ('A distância entre os dois pontos é', distancia(xa,ya,xb,yb), 'unidades')