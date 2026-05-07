# Definimos la función que recibe nuestra lista
def encontrar_mayor(numeros):
    
    # El truco: asumimos de primeras que el mayor es el primer número que vemos
    mayor_hasta_ahora = numeros[0]
    
    # Recorremos todos los números de la lista uno por uno
    for numero in numeros:
        
        # Si el número que estamos mirando ahora mismo es MÁS GRANDE 
        # que el que teníamos guardado como "mayor"...
        if numero > mayor_hasta_ahora:
            
            # ...actualizamos nuestra variable con este nuevo campeón
            mayor_hasta_ahora = numero
            
    # Cuando termine de mirar todos, devolvemos al ganador absoluto
    return mayor_hasta_ahora

# --- ZONA DE PRUEBAS ---
mis_notas = [5, 3, 9, 7, 2, 8]
el_mayor = encontrar_mayor(mis_notas)
print("El número más grande de la lista es:", el_mayor)




#MAS ARTESANAL AUN





# 1. NUESTRA FUNCIÓN CASERA PARA CONTAR (Reemplaza a len)
def contar_elementos(lista):
    total = 0
    for elemento in lista:
        total = total + 1
    return total

# 2. NUESTRA FUNCIÓN PARA ENCONTRAR EL MAYOR
def encontrar_mayor(numeros):
    
    # El truco: asumimos de primeras que el mayor es el número en la posición cero
    mayor_hasta_ahora = numeros[0]
    
    # Usamos nuestra propia función para saber cuántos números hay en total
    cantidad = contar_elementos(numeros)
    
    # Creamos nuestro propio contador para movernos por las posiciones de la lista
    i = 0
    
    # Hacemos el bucle mientras no nos pasemos de la cantidad de números
    while i < cantidad:
        
        # Si el número que estamos mirando ahora mismo en la posición 'i' 
        # es MÁS GRANDE que el que teníamos guardado como "mayor"...
        if numeros[i] > mayor_hasta_ahora:
            
            # ...actualizamos nuestra variable con este nuevo campeón
            mayor_hasta_ahora = numeros[i]
            
        # ¡CRÍTICO! Le sumamos 1 a 'i' a mano para que en la siguiente vuelta 
        # mire la siguiente posición de la lista.
        i = i + 1
            
    # Cuando termine de mirar todos, devolvemos al ganador absoluto
    return mayor_hasta_ahora

# --- ZONA DE PRUEBAS ---
mis_notas = [5, 3, 9, 7, 2, 8]
el_mayor = encontrar_mayor(mis_notas)
print("El número más grande de la lista es:", el_mayor)