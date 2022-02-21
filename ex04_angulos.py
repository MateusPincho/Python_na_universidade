#Mateus Pincho de Oliveira (12110103)
#leia os valores dos três ângulos de um triângulo e o classifique como equilátero (três ângulos iguais), isósceles (dois ângulos iguais) ou escaleno (caso contrârio).

angulo_01 = int(input('Digite um ângulo:'))
angulo_02 = int(input('Digite um ângulo:'))
angulo_03 = int(input('Digite um ângulo:'))

if angulo_01 + angulo_02 + angulo_03 == 180:
    if angulo_01 == angulo_02 == angulo_03:
        print('O triângulo é equilátero!')
    elif (angulo_01 == angulo_02 or angulo_01 == angulo_03 or angulo_02 == angulo_03):
        print('O triângulo é isóceles!')
    elif angulo_01 != angulo_02 != angulo_03: 
        print('O triângulo é escaleno!')
    if angulo_01 == 90:
        print('E também é retângulo')
    elif angulo_02 == 90:
        print('E também é retângulo')
    elif angulo_03 == 90:
         print('E também é retângulo')    
else:
    print('Os ângulos informados não formam triângulos')
