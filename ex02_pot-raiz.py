#Aluno Mateus Pincho de Oliveira (121110103)
#Exercício 02 - Crie um programa em Python que receba somente 2 (dois) números (n1 e n2) e imprima o quadrado do menor número e a raiz quadrada do maior número.  Caso os dois números sejam iguais, o programa finaliza e não calcula nenhum número, apenas escrevendo na tela a frase: "Dois numeros iguais"

n1 = float(input('Digite um número:'))
n2 = float(input('Digite outro número:'))

if n1 == n2: 
    print('Dois números iguais')
elif n1 < n2:
    pot = n1**2
    raiz = n2**0.5
    print('O quadrado do menor número é', pot,'e a raiz do maior número é', raiz)
elif n1 > n2:
    pot = n2**2
    raiz = n1**0.5
    print('O quadrado do menor número é', pot,'e a raiz do maior número é', raiz)