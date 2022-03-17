#Mateus Pincho de Oliveira (121110103)
#Exercicio 12

def contagem_dias (anos,meses,dias):
    dias_totais = anos*365 + meses*30 + dias
    return dias_totais

print('Vamos agora calcular sua idade!')
valor_anos = int(input('Anos:'))
valor_meses = int(input('Meses:'))
valor_dias = int(input('Dias:'))

print(contagem_dias(valor_anos,valor_meses,valor_dias),'dias')

