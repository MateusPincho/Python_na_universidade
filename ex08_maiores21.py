lista_idades = []
lista_nomes = []

while len(lista_idades) < 20:
    n = input("Qual seu nome?")
    lista_nomes.append(n)
    
    i = int(input("Qual sua idade?"))
    lista_idades.append(i)

n_nome = 0

for idade in lista_idades:
    if idade >21:
        print(lista_nomes[n_nome], idade)
    n_nome = n_nome + 1     
