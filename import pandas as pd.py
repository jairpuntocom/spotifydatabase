import pandas as pd

archivo_csv = 'Spotify Most Streamed Songs.csv'  

df = pd.read_csv(archivo_csv)

# Quitar espacios en los nombres de columnas
df.columns = df.columns.str.strip()

# Limpiar columnas numéricas que están como texto
columnas_a_numerico = ['streams', 'in_deezer_playlists', 'in_shazam_charts']

for col in columnas_a_numerico:
    df[col] = df[col].astype(str).str.replace(',', '').str.strip()  
    df[col] = pd.to_numeric(df[col], errors='coerce')  

#  Limpiar columna 'cover_url'
df['cover_url'] = df['cover_url'].replace('Not Found', pd.NA)

#  Eliminar filas con datos nulos críticos
df = df.dropna(subset=['key'])  

#  Llenar otros nulos con 0 si tiene sentido
df[['in_shazam_charts']] = df[['in_shazam_charts']].fillna(0)

#  Eliminar filas duplicadas
df = df.drop_duplicates()

#  Renombrar columnas para que sean más amigables
df = df.rename(columns={
    'artist(s)_name': 'artist_name',
    'danceability_%': 'danceability',
    'valence_%': 'valence',
    'energy_%': 'energy',
    'acousticness_%': 'acousticness',
    'instrumentalness_%': 'instrumentalness',
    'liveness_%': 'liveness',
    'speechiness_%': 'speechiness'
})

# Elimina todas las columnas desde la columna 9 hasta el final
df = df.iloc[:, :9]


print(df.columns)

print(df.head())

 # Crea un nuevo archivo CSV
df.to_csv('base_datos_limpia.csv', index=False)
