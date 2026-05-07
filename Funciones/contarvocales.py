# Definimos la función que recibe una frase
def contar_vocales(texto):
    
    # Creamos una variable para llevar la cuenta, empieza en 0
    contador = 0
    
    # Un string con todas las vocales posibles (minúsculas y mayúsculas)
    vocales = "aeiouAEIOU"
    
    # El bucle 'for' en un texto va cogiendo una a una cada letra de la frase
    for letra in texto:
        
        # Comprobamos si la letra que estamos mirando está dentro de nuestras vocales
        if letra in vocales:
            
            # Si es una vocal, le sumamos 1 a nuestro contador
            contador = contador + 1
            
    # Cuando termina de mirar todas las letras, devolvemos el resultado final
    return contador

# --- ZONA DE PRUEBAS ---
mi_frase = "Hola amigo, que tal el examen"
total_vocales = contar_vocales(mi_frase)
print("La frase tiene", total_vocales, "vocales.")




#MAS ARTESANAL AUN







# 1. NUESTRA FUNCIÓN CASERA PARA CONTAR (Reemplaza a len)
def contar_elementos(texto):
    total = 0
    for elemento in texto:
        total = total + 1
    return total

# 2. NUESTRA FUNCIÓN PARA CONTAR VOCALES NIVEL ARTESANO
def contar_vocales(texto):
    
    # Usamos nuestra propia función para saber cuántas letras tiene la frase
    cantidad_letras = contar_elementos(texto)
    
    # Creamos nuestra variable para llevar la cuenta final
    contador = 0
    
    # Nuestro string con todas las vocales posibles
    vocales = "aeiouAEIOU"
    
    # Usamos también nuestra función para contar cuántas vocales hay en ese string (son 10)
    cantidad_vocales = contar_elementos(vocales)
    
    # Contador para movernos por las posiciones de la frase
    i = 0
    
    # Bucle principal: recorre la frase letra a letra
    while i < cantidad_letras:
        
        # Sacamos a mano la letra exacta de la frase
        letra_actual = texto[i]
        
        # ¡AQUÍ ESTÁ LA MAGIA ARTESANAL!
        # En lugar de usar el atajo de Python "if letra in vocales",
        # creamos un segundo bucle para buscar nosotros mismos esa letra.
        j = 0
        es_vocal = False
        
        # Bucle secundario: recorre nuestro string de vocales
        while j < cantidad_vocales:
            
            # Si la letra de la frase coincide exactamente con la vocal que estamos mirando...
            if letra_actual == vocales[j]:
                es_vocal = True  # ¡Hemos encontrado una coincidencia!
                
            # Sumamos 1 a 'j' a mano para mirar la siguiente vocal
            j = j + 1
            
        # Si nuestra búsqueda manual confirmó que era una vocal...
        if es_vocal == True:
            # ...le sumamos 1 a nuestro contador total
            contador = contador + 1
            
        # Sumamos 1 a 'i' a mano para pasar a la siguiente letra de la frase
        i = i + 1
            
    # Devolvemos el resultado final
    return contador

# --- ZONA DE PRUEBAS ---
mi_frase = "Hola amigo, que tal el examen"
total_vocales = contar_vocales(mi_frase)
print("La frase tiene", total_vocales, "vocales (calculado nivel dios).")