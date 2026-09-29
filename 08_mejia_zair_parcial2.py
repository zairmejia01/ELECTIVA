productos = [
    {"nombre": "teclado", "precio": 80000, "cantidad": 3},
    {"nombre": "mouse", "precio": 50000, "cantidad": 5},
    {"nombre": "monitor", "precio": 700000, "cantidad": 2},
    {"nombre": "camara", "precio": 120000, "cantidad": 1}
]

def calcular_total(precio, cantidad):
    total= precio * cantidad
    return total

valor_total_inventario = 0
bajo_stock = []

print("RECORRER PRODUCTOS")

for producto in productos:
    producto["total"] = calcular_total(producto["precio"], producto["cantidad"])


    print(f"Producto: {producto['nombre']} | Total: {producto['total']:}")
    
    valor_total_inventario += producto["total"]
    
    if producto["cantidad"] <= 2:
        bajo_stock.append(producto["nombre"])

print("RESUMEN FINAL DEL INVENTARIO")
print(f"Valor total del inventario:{valor_total_inventario}")
print(f"Productos con bajo stock (<= 2): {bajo_stock}")