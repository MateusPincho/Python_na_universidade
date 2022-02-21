#Mateus Pincho de OLiveira (121110103)
#Escreva um programa em Python que leia as coordenadas (x,y) de um ponto no plano e indique em que quadrante 

x = int(input('Digite a coordenada x:'))
y = int(input('Digite a coordenada y:'))


if x > 0 and y > 0:
    print('O ponto está no 1° quadrante!')

elif x < 0 and y > 0:
    print('O ponto está no 2° quadrante!')

elif x < 0 and y < 0:
    print('O ponto está no 3° quadrante!')

elif x > 0 and y < 0:
    print('O ponto está no 4° quadrante!')
    
else:
    print('ERRO, o programana não aceita valores de x e/ou y igual a ZERO')
