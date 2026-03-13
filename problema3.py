import re

# Función para contar caracteres
def contar_caracteres(texto):
    return len(texto)


# Función para contar palabras
def contar_palabras(texto):
    return len(texto.split())


# Función para contar oraciones
def contar_oraciones(texto):
    oraciones = re.split(r"[.!?]+", texto)
    return len([o for o in oraciones if o.strip()])


# Función para encontrar la palabra más larga
def palabra_mas_larga(texto):
    palabras = texto.split()

    if not palabras:
        return ""

    return max(palabras, key=len)


# Función para encontrar la palabra más corta
def palabra_mas_corta(texto):
    palabras = texto.split()

    if not palabras:
        return ""

    return min(palabras, key=len)


# Función para contar vocales
def contar_vocales(texto):
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    return sum(1 for c in texto if c in vocales)


# Función para contar consonantes
def contar_consonantes(texto):
    letras = sum(1 for c in texto if c.isalpha())
    vocales = contar_vocales(texto)
    return letras - vocales


# Función principal
def main():

    # Validar que el texto no esté vacío
    while True:
        texto = input("Ingresa un texto: ")

        if texto.strip():
            break

        print("El texto no puede estar vacío.")

    print("\n----- Estadísticas del Texto -----")

    print(f"Total de caracteres: {contar_caracteres(texto)}")
    print(f"Total de palabras: {contar_palabras(texto)}")
    print(f"Total de oraciones: {contar_oraciones(texto)}")
    print(f"Palabra más larga: {palabra_mas_larga(texto)}")
    print(f"Palabra más corta: {palabra_mas_corta(texto)}")
    print(f"Número de vocales: {contar_vocales(texto)}")
    print(f"Número de consonantes: {contar_consonantes(texto)}")


if __name__ == "__main__":
    main()