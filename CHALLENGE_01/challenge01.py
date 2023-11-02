# Función para procesar el mensaje y contar las palabras
def procesar_mensaje(mensaje):
    palabras = mensaje.split()
    contador = {}
    resultado = []

    for palabra in palabras:
        palabra = palabra.lower()  # Convertir la palabra a minúsculas
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1
            resultado.append(palabra)

    # Generar la cadena de texto con las palabras y sus conteos
    resultado_final = "".join(
        [f"{palabra}{contador[palabra]}" for palabra in resultado]
    )
    return resultado_final


# Leer el mensaje desde el archivo
with open("message_01.txt", "r") as archivo:
    mensaje = archivo.read()

# Procesar el mensaje
resultado = procesar_mensaje(mensaje)

# Imprimir el resultado
print(resultado)
