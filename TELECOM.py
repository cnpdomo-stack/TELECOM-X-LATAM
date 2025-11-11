import requests
import pandas as pd

# Ejemplo de URL (simula una API que devuelve datos JSON de clientes)
url = 'https://github.com/alura-cursos/challenge2-data-science-LATAM/blob/main/TelecomX_Data.json'

response = requests.get(url)
data = response.json()

# Convertimos los datos JSON en un DataFrame
df = pd.DataFrame(data)
