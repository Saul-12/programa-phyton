cadena = input("Ingrese una cadena de texto: ").lower()
cadena=cadena.split()

for i in range(len(cadena)):
    for j in range(i+1, len(cadena)):
        if cadena[i] > cadena[j]:
            cadena[j], cadena[i] = cadena[i], cadena[j]
            
for palabra in cadena:
    print(palabra)