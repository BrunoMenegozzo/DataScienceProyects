# Importamos algunas librerías generales
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

# Importamos modelo lineal
from sklearn.linear_model import LinearRegression

"""
file = 'C:\\Users\\Bruno\\Desktop\\Data Science\\EjerciciosPandas\\EVI_Lago_SanRoque\\DataSet_EVI_LagoSanRoque.csv' 


df = pd.read_csv(file)
#print(df)

## Graficos

fig, ax = plt.subplots(1, 1, figsize = (6, 4))


# Puntos de entrenamiento
ax.scatter(df['Fecha'], df['EVI'], color = 'b', alpha = 0.35, s = 100)

plt.show()
"""

file = 'C:\\Users\\Bruno\\Desktop\\Data Science\\EjerciciosPandas\\EVI_Lago_SanRoque\\DataSet_EVI_LagoSanRoque.csv' 


datos = pd.read_csv(file, decimal= ",")
df = pd.DataFrame(datos)



# Suponiendo que tienes tu conjunto de datos en un DataFrame llamado 'data'
# Si aún no tienes los datos en un DataFrame, puedes cargarlos desde un archivo CSV o Excel

# Extraer las columnas "Fecha" y "EVI"
fechas = df["Fecha"]
evi = df["EVI"]
index = df["Index"]
x=fechas
y=evi

"""
# Crear el gráfico de dispersión
plt.figure(figsize=(10, 6))  # Tamaño del gráfico (opcional)
plt.scatter(fechas, evi, marker='o', color='b', label='EVI')

# Personalizar el gráfico
plt.title('Gráfico de Puntos de EVI a lo largo del tiempo')
plt.xlabel('Fecha')
plt.ylabel('EVI')
plt.xticks(rotation=45)  # Rotar las etiquetas del eje x para una mejor visualización
plt.grid(True)

# Mostrar la leyenda (opcional)
plt.legend()
"""
##//////////////////////////////////////////////////////////////////////////////////////
## Ajuste del modelo 

# Creación del modelo lineal
reg = LinearRegression()

# Este cambio de dimensiones es necesario ya que scikit-learn espera que x sea una matriz
X = np.reshape(index,(-1,1))

# Ajuste del modelo 
reg.fit(X, evi)

# Coeficientes del modelo 
beta_0_estimado = reg.intercept_
beta_1_estimado = reg.coef_[0]

print('Ordenada al origen = {:.3f}'.format(beta_0_estimado))
print('Pendiente = {:.3f}'.format(beta_1_estimado))

# Calidad del ajuste
print('Calidad de ajuste R^2 = {:.3f}'.format(reg.score(X, evi)))
##//////////////////////////////////////////////////////////////////////////////////////
"""
# Mostrar el gráfico
plt.tight_layout()
plt.show()


## Graficos

fig, ax = plt.subplots(1, 1, figsize = (6, 4))

# Puntos de entrenamiento
ax.scatter(fechas, evi, color = 'b', alpha = 0.35, s = 100)


# Relacion estimada


ax.legend(['Real', 'Estimado'])
plt.gca().yaxis_set_major_formatter(StrMethodFormatter('{x:.2f}'))
plt.show()

"""

## Graficos

fig, ax = plt.subplots(1, 1, figsize = (6, 4))

# Puntos de entrenamiento
ax.scatter(x, y, color = 'b', alpha = 0.35, s = 100)
ax.yaxis.set_major_formatter(str)
# Relacion real
#y_verdadero = np.polyval([beta_1, beta_0], x)
#ax.plot(x, y_verdadero, color = 'r', linestyle = '--', linewidth = 4, alpha = 0.75)

# Relacion estimada
y_estimado = np.polyval([beta_1_estimado, beta_0_estimado], x)
ax.plot(x, y_estimado, color = 'g', linestyle = '-', linewidth = 4, alpha = 0.75)

ax.legend(['Estimado'])
plt.show()

