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