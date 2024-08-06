import re

texto = 'si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online'

patron = 'ayuda'

busqueda = re.search(patron,texto)
print(busqueda)
#<re.Match object; span=(13, 18), match='ayuda'>
print(busqueda.span())
#(13, 18)
print(busqueda.group())
#ayuda
print(re.findall(patron,texto))
#['ayuda', 'ayuda']
for hallazgo in re.finditer(patron,texto):
    print(hallazgo.span())
#(13, 18)
#(71, 76)

#--------------------------------------------------------#

texto = 'llama al 564-525-6588 ya mismo'

patron = r'\d\d\d-\d\d\d-\d\d\d\d'

resultado = re.search(patron, texto) #---> detecta si encuentra el patron brindado

print(resultado)
#<re.Match object; span=(9, 21), match='564-525-6588'>
print(resultado.group())
#564-525-6588

patron = re.compile(r'(\d{3})-(\d{3})-(\d{4})') #---> con los parentesis armo grupos de patron

resultado = re.search(patron,texto)

print(resultado.group(1))
#564
print(resultado.group(2))
#525
print(resultado.group(3))
#6588

#--------------------------------------------------------#

clave = input('Clave: ')

patron = r'\D{1}\w{7}' #---> primer digito no numerico y luego 7 caracteres alfanumericos

chequear = re.search(patron,clave) #---> input: e546tera

print(chequear)
#<re.Match object; span=(0, 8), match='e546tera'>

#--------------------------------------------------------#

texto = 'No atendemos los lunes por la tarde'

buscar = re.search(r'lunes|martes',texto)

print(buscar)
#<re.Match object; span=(17, 22), match='lunes'>