num01 = int(input("Digite um número:"))
num02 = int(input("Digite outro número:"))
num03 = int(input("Digite outro número:"))
num04 = int(input("Digite outro número:"))
num05 = int(input("Digite o ultimo número:"))

lista = []
lista.append(num01)
lista.append(num02)
lista.append(num03)
lista.append(num04)
lista.append(num05)
lista.sort()
print("O menor número é",lista[0],"e o maior é ",lista[4])
