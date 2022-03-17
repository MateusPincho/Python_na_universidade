def contagem_segundos (hora, minuto, seg):
    n_hora = hora*3600
    n_minuto = minuto*60
    n_segundo = seg
    total = n_hora + n_minuto + n_segundo
    return total

hora2 = int(input('informe as horas'))
minuto2 = int(input('informe os minutos'))
seg2 = int(input('informe os segundos'))

print(contagem_segundos(hora2, minuto2, seg2),'segundos')