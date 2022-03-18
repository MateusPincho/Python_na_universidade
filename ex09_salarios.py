lista_nomes = []
lista_salarios = []

while len(lista_salarios) < 5:
    n = input('Qual seu nome?')
    lista_nomes.append(n)
    s = int(input('Qual seu salário?'))
    lista_salarios.append(s)
    
n_nome = 0
    
for salario in lista_salarios: 
    if salario < 600:
        print(f'{lista_nomes[n_nome]}, para o seu salário de {salario}, você está isento de imposto')
    elif salario > 600 and salario < 1500:
        imposto = salario*0.1
        print(f'{lista_nomes[n_nome]}, para o seu salário de {salario}, você deve pagar {imposto} reais de imposto')
    else:
        imposto = salario*0.15
        print(f'{lista_nomes[n_nome]}, para o seu salário de {salario}, você deve pagar {imposto} reais de imposto')
    n_nome = n_nome + 1 
    
