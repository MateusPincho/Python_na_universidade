import math

n = int(input('Informe um número: '))

def fatorial (x):
    soma = 0 
    for i in range(n):
        soma += 1/math.factorial(i)
    return soma

print(fatorial(n))