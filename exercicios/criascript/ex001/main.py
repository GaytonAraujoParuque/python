def segundos(h, m, s):
    horas = h * 60
    hora_em_segundos = horas * 60
    minutos = 60 * m
    segundos = s
    return hora_em_segundos + minutos + segundos

print(segundos(24, 0, 0))
    