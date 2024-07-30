texto = input("Ingrese el texto que desea publicar a continuacion: ")
print("A continuacion coloque 3 letras de preferencia")

letras = [input("Letra 1: "),input("Letra 2: "),input("Letra 3: ")]

dicbool = {'True': 'aparece', 'False':'no aparece'}

print(f"""Perfecto, su texto repite la letra '{letras[0]}' unas {texto.count(letras[0])} veces.
La letra '{letras[1]}' {texto.count(letras[1])} veces 
y la letra '{letras[2]}' unas {texto.count(letras[2])} veces.
 
Su texto inicia con la letra {texto[0]} y termina con la letra {texto[-1]} y tiene un largo total de {len(texto.split(" "))} palabras.


La palabra Python {dicbool[str("python" in texto)]}.

El texto al reves es asi: {texto[::-1]}""")