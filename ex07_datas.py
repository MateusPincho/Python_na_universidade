from datetime import date

ano = int(input("Informe o ano:"))
mes = int(input("Informe o mês:"))
dia = int(input("Informe o dia:"))

dataSimples = date(year = ano, month = mes, day = dia)
print(dataSimples)
