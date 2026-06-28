def saludar(nombre_completo):
    if nombre_completo.strip() == "":
        return "Debe ingresar un nombre."

    return f"Hola {nombre_completo}"

print(saludar("Efrain Norberto Alanoca Aguilar "))