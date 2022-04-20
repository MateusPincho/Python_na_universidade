import random 
from fractions import Fraction
vetor_x = []

n = int(input('Informe o tamanho do vetor X: '))

for i in range(n):
    i = random.randint(1,101)
    vetor_x.append(i)
    
print('O vetor X é ', vetor_x)

def med_ari ():
    
    soma_vx = sum(vetor_x)
    
    result_med_ari = soma_vx/n
    print(f"A média aritmética do vetor X é {result_med_ari}")

def med_geo ():
    
    produto_vx = 1
    for numero in vetor_x:
        produto_vx *= numero
    
    result_med_geo = (produto_vx)**(1/n)
    print(f"A média geométrica do vetor X é {result_med_geo}")

def med_har():
    
    soma_inversos_vx = 0
    for numero in vetor_x:
        fracao = Fraction(1,numero)
        soma_inversos_vx += fracao
    
    result_med_har = n / soma_inversos_vx
    print(f"A média harmônica do vetor X é {result_med_har}")

def desvio_padrão():
    
    soma_variancia = 0 
    variancia = 0
    media = sum(vetor_x)/n
    for numero in vetor_x:
        soma_variancia += (numero - media)**2
        variancia = soma_variancia / n
    
    result_desvio_padrao = (variancia)**0.5
    print(f"O desvio padrão do vetor X é {result_desvio_padrao}")

med_ari()
med_geo()
med_har()
desvio_padrão()
