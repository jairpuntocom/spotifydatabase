# 🎵 Análisis Musical con Spotify

**Autor:** Jair Alejandro Gutiérrez Gonzales  
**Universidad Cuauhtémoc**  
**Materia:** Big Data  
**Profesora:** Tania García Muñoz  

## 📌 Objetivo

Aplicar conocimientos adquiridos sobre Python, manipulación de datos y visualización en Power BI. Este proyecto busca representar datos musicales reales provenientes de la API de Spotify, enfocándose en la popularidad, año de lanzamiento, artista y género musical.

## 🛠 Herramientas Utilizadas

- **Python 3 + Spotipy:** para conectarse con la API de Spotify y recolectar datos.
- **Pandas / Openpyxl:** para estructurar y exportar datasets.
- **Power BI:** para construir dashboards y análisis visual.
- **Spotify Web API:** como fuente principal de datos.

## 🧪 Proceso

### 1. Extracción de Datos
Se recolectaron dos datasets:
- `spotify_canciones_por_genero_10000.csv`: contiene canciones agrupadas por géneros musicales.
- `spotify_top_tracks_global.csv`: lista global de canciones más populares según Spotify.

### 2. Limpieza
En Python, se extrajeron campos relevantes como:
- Nombre de la canción
- Artista
- Popularidad
- Año de lanzamiento
- Género

### 3. Visualización en Power BI
Se importaron ambos archivos CSV para desarrollar dashboards con:
- Tablas dinámicas
- Gráficos de barras
- Líneas temporales
- Filtros por género y artista

## 📊 Dashboards Incluidos

- Top 10 canciones por popularidad
- Popularidad a través del tiempo
- Canciones por artista
- Comparaciones interactivas
- Dashboard exclusivo para el Top Global

## 📝 Conclusiones

El proyecto demuestra cómo integrar varias tecnologías para analizar datos reales. A pesar de las limitaciones de la API (como el límite de resultados por género), se logró obtener una visión amplia y atractiva del consumo musical actual.

---

## 📂 Archivos Incluidos

- `spotify_canciones_por_genero_10000.csv`
- `spotify_top_tracks_global.csv`
- `Documentacion Spotify.docx` (documento completo del proyecto)
- `Proyecto_PowerBI.pbix` (archivo Power BI, si aplica)
- Código fuente Python (bajo solicitud)

---

> Proyecto académico desarrollado para la materia de Big Data.
