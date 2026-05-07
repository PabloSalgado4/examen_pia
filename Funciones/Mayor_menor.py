# 1. NUESTRA FUNCIÓN CASERA PARA CONTAR (Reemplaza a len)
def contar_elementos(lista):
    total = 0
    for elemento in lista:
        total = total + 1
    return total

# 2. NUESTRA FUNCIÓN PARA ORDENAR DE MAYOR A MENOR (Sin usar range)
def ordenar_mayor_a_menor(numeros):
    
    # Usamos nuestra propia función para saber cuántos números hay
    cantidad = contar_elementos(numeros)
    
    # Creamos el contador para el primer bucle
    i = 0
    
    # Bucle principal (mientras 'i' sea menor que la cantidad total)
    while i < cantidad:
        
        # Creamos el contador para el segundo bucle
        j = 0
        
        # Bucle secundario para ir comparando de dos en dos
        # (cantidad - i - 1) evita que nos salgamos del límite de la lista
        while j < (cantidad - i - 1):
            
            # Si el número actual es MENOR que el siguiente, los intercambiamos
            if numeros[j] < numeros[j + 1]:
                temporal = numeros[j]
                numeros[j] = numeros[j + 1]
                numeros[j + 1] = temporal
                
            # ¡CRÍTICO! Sumamos 1 a 'j' a mano para que el bucle avance
            j = j + 1
            
        # ¡CRÍTICO! Sumamos 1 a 'i' a mano antes de la siguiente vuelta
        i = i + 1
        
    # Devolvemos la lista ya ordenada
    return numeros

# --- ZONA DE PRUEBAS ---

# Nuestra lista desordenada
mis_numeros = [4, 1, 9, 3, 7, 2]

# Llamamos a la función principal
resultado = ordenar_mayor_a_menor(mis_numeros)

# Imprimimos el resultado final
print("Lista ordenada nivel experto (sin len ni range):", resultado)