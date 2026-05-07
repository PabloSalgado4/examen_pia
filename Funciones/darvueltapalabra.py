# Definimos la función
def invertir_texto(texto):
    
    # Creamos una variable vacía (sin nada dentro) para ir guardando el resultado
    texto_invertido = ""
    
    # Recorremos el texto original letra por letra
    for letra in texto:
        
        # AQUÍ ESTÁ EL TRUCO:
        # En vez de poner la nueva letra al final, la ponemos DELANTE de lo que ya teníamos.
        # Así, la primera letra del texto original acabará siendo la última.
        texto_invertido = letra + texto_invertido
        
    # Devolvemos el texto ya del revés
    return texto_invertido

# --- ZONA DE PRUEBAS ---
palabra = "aprobado"
resultado = invertir_texto(palabra)
print("La palabra original es:", palabra)
print("La palabra invertida es:", resultado)







#MAS ARTESANAL AUN








# 1. NUESTRA FUNCIÓN CASERA PARA CONTAR (Reemplaza a len)
# Sirve tanto para listas de números como para contar letras en un texto
def contar_elementos(texto):
    total = 0
    for letra in texto:
        total = total + 1
    return total

# 2. NUESTRA FUNCIÓN PARA INVERTIR EL TEXTO A MANO
def invertir_texto(texto):
    
    # Usamos nuestra propia función para saber cuántas letras tiene la palabra
    cantidad = contar_elementos(texto)
    
    # Creamos una variable vacía para ir guardando el resultado
    texto_invertido = ""
    
    # Creamos nuestro propio contador para movernos por las posiciones de la palabra
    i = 0
    
    # Hacemos el bucle mientras no nos pasemos de la cantidad de letras
    while i < cantidad:
        
        # Sacamos a mano la letra exacta que está en la posición 'i'
        letra_actual = texto[i]
        
        # AQUÍ ESTÁ EL TRUCO:
        # Ponemos la letra que acabamos de sacar DELANTE de lo que ya teníamos.
        texto_invertido = letra_actual + texto_invertido
        
        # ¡CRÍTICO! Le sumamos 1 a 'i' a mano para que en la siguiente vuelta
        # mire la siguiente letra de la palabra.
        i = i + 1
        
    # Devolvemos el texto ya del revés
    return texto_invertido

# --- ZONA DE PRUEBAS ---
palabra = "aprobado"
resultado = invertir_texto(palabra)
print("La palabra original es:", palabra)
print("La palabra invertida nivel artesano:", resultado)