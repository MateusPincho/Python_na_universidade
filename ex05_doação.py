#Mateus Pincho de Oliveira (121110103)
#Você foi contrado para desenvolver um programa para a agilizar a triagem da doação de sangue
print('Olá, você está prestes a doar sangue. Preciso apenas que você preencha algumas informações')
sexo = input('Informe seu sexo: ')
idade = float(input('Informe sua idade: '))
peso = float(input('Informe seu peso: '))
apto = input('Você já doou sangue antes? ')
febre = input('Você teve febre nas ultimas 24h?')
gravida = ''
amamentar = ''
parto = ''

if febre == 'sim':
    print('Você não pode doar sangue hoje, devido sua febre :(')
else:
    if 16 > idade or idade > 69:
        print('Você não está apto para doar sangue por não estar na faixa etaria:(')
    elif 60 < idade < 69 and apto == 'nao':
        print('Você não está apto para doar sangue, pois nunca doou antes :(')
    else:
        if sexo == 'masculino' and peso < 60:
            print('Você não está apto para doar sangue por estar abaixo do peso :(')
        elif sexo == 'feminino' and peso < 50:
            print('Você não está apta para doar sangue por estar abaixo do peso :(')
        else: 
            print('Você logo mais estará doando sangue! :)')
            if sexo == 'feminino':
                gravida = input('Você está grávida?')
                if gravida == 'sim':
                    print('Você não esta apta para doar sangue por estar grávida :(')
                else:
                    amamentar = input('Você está amamentando?')
                    if amamentar == 'sim':
                        parto = int(input('Há quanto tempo foi realizado o parto?'))
                        if parto > 12:
                            print ('Você esta apta para doar sangue! :)')                        
                    else:
                        print('Você esta apta para doar sangue! :)')
              