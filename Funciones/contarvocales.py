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