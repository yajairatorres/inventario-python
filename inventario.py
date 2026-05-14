# Matriz de inventario
inventario = [
    ["A101", "Mouse", 3, 10],
    ["A102", "Teclado", 15, 10],
    ["A103", "Monitor", 2, 5],
    ["A104", "Impresora", 8, 8],
    ["A105", "Audifonos", 1, 4]
]

# Función para calcular la cantidad a pedir
def calcular_pedido(stock_actual, stock_minimo):
    
    if stock_actual < stock_minimo:
        cantidad_pedir = stock_minimo - stock_actual
    else:
        cantidad_pedir = 0
        
    return cantidad_pedir

# Mostrar resultados
print("LISTA DE PEDIDOS\n")

for articulo in inventario:
    
    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]
    
    cantidad = calcular_pedido(stock_actual, stock_minimo)
    
    print("Código:", codigo)
    print("Artículo:", nombre)
    print("Cantidad a pedir:", cantidad)
    print("---------------------------")