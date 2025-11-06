# Análisis Exploratorio de Datos con Pandas - Población Mundial

## Descripción
Este proyecto implementa un análisis exploratorio de datos (EDA) completo sobre datos de población mundial, aplicando técnicas profesionales de análisis con Pandas. El trabajo sigue la metodología del curso de Alex The Analyst sobre análisis exploratorio con Pandas.

**Curso de referencia:** [Pandas YouTube Series - Alex The Analyst](https://www.youtube.com/watch?v=Liv6eeb1VfE)

## Estructura del Proyecto
analisis-exploratorio-pandas/
├── Analisis Exploratorio - Poblacion Mundial.ipynb
├── world_population.csv
├── README.md
└── requirements.txt

## Técnicas Aplicadas

### Análisis Exploratorio Inicial
- Inspección de estructura de datos con `df.info()` y `df.describe()`
- Identificación de valores faltantes con `isnull().sum()`
- Análisis de valores únicos por columna con `nunique()`

### Manipulación y Ordenamiento de Datos
- Ordenamiento de datos por población con `sort_values()`
- Filtrado de datos por criterios específicos (continentes)
- Identificación de top 10 países por población

### Análisis Estadístico
- Cálculo de matrices de correlación entre variables numéricas
- Agrupación y agregación de datos por continente
- Análisis de tendencias poblacionales temporales

### Visualización de Datos
- Mapas de calor para correlaciones con Seaborn
- Gráficos de líneas para tendencias temporales
- Diagramas de caja para distribución de datos
- Visualizaciones integradas de Pandas
## Instalación y Ejecución

### Prerrequisitos
```bash
pip install pandas seaborn matplotlib jupyter

