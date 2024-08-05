import datetime

mi_hora = datetime.time(17, 35)

print(mi_hora)
#17:35:00

mi_fecha = datetime.datetime(2025,5,15,22,10,15,2500)
print(mi_fecha)
#2025-05-15 22:10:15.002500

nacimiento = datetime.date(1995,3,5)
defuncion = datetime.date(2095,6,19)

vida = defuncion - nacimiento

print(vida)
#36631 days, 0:00:00

print(vida.days)
#36631