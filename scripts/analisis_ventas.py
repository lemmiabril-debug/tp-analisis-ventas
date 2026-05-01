import pandas as pd
import matplotlib.pyplot as plt
import os

# Se crean las carpetas necesarias para guardar los resultados.
os.makedirs("resultados", exist_ok=True)

# Se carga el archivo CSV desde la carpeta datos.
ventas = pd.read_csv("datos/ventas.csv")

# Se calcula el total de venta de cada registro.
ventas["total"] = ventas["cantidad"] * ventas["precio_unitario"]

# Se calcula el total general de ventas.
ventas_totales = ventas["total"].sum()

# Se identifica el producto con mayor cantidad vendida.
producto_mas_vendido = ventas.groupby("producto")["cantidad"].sum().idxmax()

# Se convierte la fecha a formato de fecha para poder agrupar por mes.
ventas["fecha"] = pd.to_datetime(ventas["fecha"])
ventas["mes"] = ventas["fecha"].dt.to_period("M")

# Se calculan las ventas totales por mes.
ventas_por_mes = ventas.groupby("mes")["total"].sum()

# Se guarda un resumen de los resultados en un archivo de texto.
with open("resultados/resumen_ventas.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Resumen del análisis de ventas\n")
    archivo.write("--------------------------------\n")
    archivo.write(f"Ventas totales: ${ventas_totales}\n")
    archivo.write(f"Producto más vendido: {producto_mas_vendido}\n")
    archivo.write("\nVentas por mes:\n")
    archivo.write(str(ventas_por_mes))

# Se genera un gráfico simple con la evolución mensual de ventas.
ventas_por_mes.plot(kind="bar")
plt.title("Ventas por mes")
plt.xlabel("Mes")
plt.ylabel("Total vendido")
plt.tight_layout()
plt.savefig("resultados/grafico_ventas.png")

print("Análisis finalizado correctamente.")
print(f"Ventas totales: ${ventas_totales}")
print(f"Producto más vendido: {producto_mas_vendido}")
