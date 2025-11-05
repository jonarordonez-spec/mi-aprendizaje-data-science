# 📊 Análisis Exploratorio de Datos con Pandas - Población Mundial

## 🎯 Descripción del Proyecto
Análisis exploratorio de datos (EDA) completo de datos de población mundial utilizando Pandas, siguiendo las mejores prácticas de la industria. Este proyecto demuestra técnicas esenciales de análisis de datos para roles de ciencia de datos y analítica.

## 📈 Habilidades Demostradas

### 🔍 Exploración y Limpieza de Datos
- **Inspección de Datos**: `info()`, `describe()`, `dtypes`
- **Análisis de Valores Faltantes**: `isnull().sum()`
- **Valores Únicos**: `nunique()`
- **Ordenamiento de Datos**: `sort_values()` con ordenamiento personalizado

### 📊 Análisis Estadístico
- **Estadísticas Descriptivas**: Media, desviación estándar, valores mínimos/máximos
- **Análisis de Correlación**: Visualización de matriz de correlación
- **Análisis por Grupos**: Agregaciones y comparaciones a nivel continental

### 🎨 Visualización de Datos
- **Mapas de Calor con Seaborn**: Visualización de matrices de correlación
- **Gráficos con Matplotlib**: Análisis de series temporales y comparativo
- **Visualización con Pandas**: Capacidades de visualización integradas
- **Diagramas de Caja**: Análisis de distribución en características numéricas

### 🏗️ Manipulación de Datos
- **Operaciones GroupBy**: Análisis agregado por variables categóricas
- **Transposición de Datos**: Reestructuración para mejor visualización
- **Filtrado**: Selección condicional de datos y subconjuntos

## 📁 Información del Dataset
- **Fuente**: Datos de Población Mundial
- **Período Temporal**: Datos históricos de población hasta 2022
- **Características**: Datos demográficos por país, clasificación continental, tendencias poblacionales
- **Caso de Uso**: Análisis demográfico global e identificación de tendencias

## 🛠️ Stack Tecnológico
- **Python 3.x**
- **Pandas** - Manipulación y análisis de datos
- **Seaborn** - Visualización estadística de datos
- **Matplotlib** - Creación de gráficos y visualizaciones
- **Jupyter Notebook** - Entorno de desarrollo interactivo

## 📊 Análisis Clave Realizados

### 1. Evaluación de Calidad de Datos
- Identificación y manejo de valores faltantes
- Verificación y corrección de tipos de datos
- Resúmenes estadísticos básicos

### 2. Análisis de Tendencias Poblacionales
- Top 10 países más poblados (2022)
- Distribución poblacional por continente
- Contribuciones porcentuales a la población mundial

### 3. Estudios de Correlación
- Correlaciones poblacionales entre años
- Relaciones geográficas y demográficas
- Visualización de relaciones entre variables

### 4. Análisis Comparativo
- Comparaciones de promedios a nivel continental
- Análisis de series temporales del crecimiento poblacional
- Análisis de distribución usando diagramas de caja

## 🚀 Cómo Ejecutar
```bash
# Clonar el repositorio
git clone https://github.com/jonarordonez-spec/mi-aprendizaje-data-science

# Navegar al directorio del proyecto
cd curso-eda-pandas

# Instalar dependencias
pip install pandas seaborn matplotlib jupyter

# Ejecutar Jupyter Notebook
jupyter notebook "EDA con Pandas - Análisis Población Mundial.ipynb"
