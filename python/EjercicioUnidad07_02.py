import time

hora = time.strftime('%H')
minutos = time.strftime('%M')

if int(hora) >= 19:
    print("Ya es hora de volver a casa")
else:
    print("Faltan {} horas y {} minutos para volver a casa". format(18-int(hora), 59-int(minutos)))

