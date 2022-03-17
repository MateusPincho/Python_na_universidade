#Mateus Pincho de Oliveira (121110103)
#Exercicio 14

def fatorial (n): 
    lista_euler = []
    fact_n = 1

    while n > 0:
        lista_euler.append(n)
        n -= 1

    for n in lista_euler:
        fact_n *= n
    return fact_n

n = 0 
lista_fatorial = []

fatores = int(input('Informe o número de fatores: '))

while n < fatores:
    x = 1/fatorial(n)
    lista_fatorial.append(x)
    n +=1 
    
print(sum(lista_fatorial))
