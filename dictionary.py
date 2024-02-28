productos_bebidas = {
    'Agua Mineral': 1500,
    'Refresco de Cola': 2500,
    'Jugo de Naranja': 2000,
    'Café Americano': 1800,
    'Té Verde': 2200,
    'Batido de Frutas': 3000,
    'Limonada Natural': 2300,
    'Cerveza Nacional': 3500,
    'Vino Tinto': 5000,
    'Smoothie de Mango': 2800
    }
productos_postres = {
    'Helado de Vainilla': 3500,
    'Tarta de Chocolate': 4500,
    'Cupcake de Fresa': 1800,
    'Brownie con Nueces': 2800,
    'Mousse de Limón': 3200,
    'Gelatina de Frutas': 2000,
    'Crepe de Nutella': 4000,
    'Churros con Chocolate': 2500,
    'Pastel de Queso': 3800,
    'Donut Glaseado': 1500
}

productos_comidas = {
    'Hamburguesa Clásica': 6000,
    'Ensalada César': 4500,
    'Pizza Margarita': 7000,
    'Sushi Variado': 8500,
    'Tacos de Pollo': 5000,
    'Pasta Alfredo': 5800,
    'Burrito de Carne': 6500,
    'Pollo a la Parrilla': 7500,
    'Sandwich de Pavo': 3200,
    'Ceviche de Camarones': 6800
}
print(f"""Categorías disponibles: 
      1. Bebidas 
      2. postres 
      3. comidas""")
categoria_elegida = int(input("Seleccione una categoría: "))
if categoria_elegida == 1:
    categoria_elegida = "Bebidas"
elif categoria_elegida == 2:
    categoria_elegida = "Postres"
else:
    categoria_elegida = "Comidas"

if categoria_elegida in ["Bebidas", "Postres", "Comidas"]:
    print(f"Productos de la categoría {categoria_elegida}:")
    if categoria_elegida == "Bebidas":
        productos_categoria = productos_bebidas
    elif categoria_elegida == "Postres":
        productos_categoria = productos_postres
    else:
        productos_categoria = productos_comidas
    for i, (val, money) in enumerate(productos_categoria.items()): 
        print(f"{i+1}. {val} = ${money}")

    promocion = input(f"¿Desea aprovechar una promoción? (Sí/No): ").lower()

    if promocion == 'si':
        print("Promoción aplicada: Descuento del 10% en todos los productos.")
        descuento = 0.10
        producto_elegido = int(input("Seleccione un producto: "))
        if 1 <= producto_elegido <= len(productos_categoria):
            producto_elegido = list(productos_categoria.keys())[producto_elegido - 1]
            precio_original = productos_categoria[producto_elegido]
            precio_descuento = precio_original * (1 - descuento)

            print(f"Producto elegido: {producto_elegido}")
            print(f"Precio original: ${precio_original}")
            print(f"Precio con descuento: ${precio_descuento}")
            dinero = int(input(f"Ingrese la cantidad de dinero que va a pagar: $"))
            if dinero < precio_descuento:
                print(f"Lo sentimos, no tienes suficiente dinero")
            else:
                print(f"Su cambio es de ${dinero - precio_descuento}")
        else:
            print("Selección no válida.")

    else:
        producto_elegido = int(input("Seleccione un producto: "))
        if 1 <= producto_elegido <= len(productos_categoria):
            producto_elegido = list(productos_categoria.keys())[producto_elegido - 1]
            precio_original = productos_categoria[producto_elegido] 
            print(f"Producto elegido: {producto_elegido}")
            print(f"Precio original: ${precio_original}")
            dinero = int(input(f"Ingrese la cantidad de dinero que va a pagar: $"))
            if dinero < precio_original:
                print(f"Lo sentimos, no tienes suficiente dinero")
            else:
                print(f"Su cambio es de ${dinero - precio_original}")
        else:
            print("Selección no válida.")