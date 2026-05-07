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