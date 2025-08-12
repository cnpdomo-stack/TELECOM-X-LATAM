Proyedto de TELECOM X LATAM
Descripción

Proyecto de análisis de datos de ventas de varias tiendas, enfocado en analizar la razon de abandono por parte de los clientes (Churn)
Tabla de Contenidos

    Dependencias
    Uso
    Análisis y Resultados
    Problemas comunes y soluciones
    Contribuciones
    Licencia

El proyecto utiliza las siguientes librerías principales:

Python 3.8 o superior

pandas

matplotlib

seaborn


Puedes instalar todas con:

pip install pandas matplotlib seaborn folium

Uso

El análisis está contenido en un notebook de Jupyter (TelecomX_LATAM.ipynb) que puedes abrir con:

jupyter notebook TelecomX_LATAM.ipynb

O en Google Colab para ejecutar en la nube.

El notebook incluye instrucciones para cargar tus archivos de datos y ejecutar cada paso del análisis. Análisis y Resultados

El proyecto realiza los siguientes análisis:

cuentas _diarias

churn de los clientes, 

relacion de los costos con el Churn

Relacion del genero con el Churn

Variables numericas


Además, genera gráficos que permiten visualizar y comparar el desempeño de cada tienda en los diferentes aspectos analizados. Problemas comunes y soluciones

KeyError al acceder a columnas en pandas:
Verifica que los nombres de las columnas coincidan exactamente (mayúsculas, espacios, etc.). Usa print(df.columns) para inspeccionar.

Errores por falta de librerías:
Asegúrate de instalar todas las dependencias con pip install.

Valores nulos en datos numéricos:
Algunos cálculos pueden fallar si hay datos faltantes. Usa df.dropna() o fillna() para limpiar los datos.

Contribuciones

Las contribuciones son bienvenidas. Puedes abrir issues para reportar problemas o sugerir mejoras, y enviar pull requests para colaborar. Licencia

Este proyecto está bajo la licencia CNPDOMO.
