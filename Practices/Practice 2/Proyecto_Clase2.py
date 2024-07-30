#Calculadora de comisiones

nombre= input("Ingrese su nombre completo: ")
ingresos=float(input("Por favor, coloque los ingresos totales de este mes: $"))
comision=ingresos*13/100
print(f"Perfecto {nombre},\nde los ingresos totales de este mes que son ${ingresos} te corresponde por comision del 13% un total de ${round(comision,2)}")