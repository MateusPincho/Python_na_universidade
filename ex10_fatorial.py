"""
Mateus Pincho de Oliveira (121110103)
Exercício 10 
"""
def fatorial (n): 
    fact_n = 1
    if n > 0:
        while n > 0:
            fact_n *= n
            n -= 1
        return fact_n 
    else: 
        print('Fim do programa')

n = 1
while n > 0:
    n = int(input('Informe um número: '))
    print('O fatorial do número', n, 'é', fatorial(n))
