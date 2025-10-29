# Sistema de Recomendación usando Redes Bipartitas

Sistema de recomendación de productos basado en grafos bipartitos y proyección ponderada, utilizando el dataset de Amazon Electronics Reviews.

## 📋 Descripción

Este proyecto implementa un sistema de recomendación que:
- Construye un **grafo bipartito** conectando usuarios y productos
- Realiza una **proyección ponderada** sobre los productos
- Calcula la **similaridad de Jaccard** entre productos
- Proporciona recomendaciones personalizadas con métricas de calidad
- Incluye **visualizaciones interactivas** de la red

## 🎯 Características

✅ Análisis de red bipartita (usuarios ↔ productos)  
✅ Matriz de biadyacencia dispersa para eficiencia  
✅ Proyección ponderada de productos con usuarios compartidos  
✅ Algoritmo de Similaridad de Jaccard (0-100%)  
✅ Visualización de red estrella (star network)  
✅ Interfaz interactiva con ipywidgets  
✅ Filtrado inteligente de productos duplicados  
✅ Rutas relativas para portabilidad  

## 📊 Estructura del Proyecto

```
recommender_system_using_bipartite_network/
│
├── src/
│   ├── app/
│   │   ├── main.ipynb              # Notebook principal
│   │   ├── data/
│   │   │   └── amazon-products-reviews/
│   │   │       └── ratings_electronics.csv
│   │   └── utils/
│   │       └── download_dataset.py  # Script para descargar datos
│   │
└── README.md
```

## 🚀 Instalación y Uso

### Requisitos

```bash
pip install pandas numpy matplotlib seaborn networkx ipywidgets scipy
```

### Bibliotecas Principales

- **Pandas**: Procesamiento de datos
- **NetworkX**: Construcción y análisis de grafos
- **Matplotlib/Seaborn**: Visualizaciones
- **IPyWidgets**: Interfaz interactiva
- **NumPy**: Cálculos numéricos
- **SciPy**: Matrices dispersas

### Ejecución

1. Abrir `src/app/main.ipynb` en Jupyter Notebook/Lab o VS Code
2. Ejecutar las celdas en orden secuencial
3. Usar los dropdowns interactivos en la última sección

## 📐 Algoritmo: Similaridad de Jaccard

La similaridad entre dos productos A y B se calcula como:

```
J(A, B) = |A ∩ B| / |A ∪ B| × 100%
```

Donde:
- **A, B**: Conjuntos de usuarios que calificaron cada producto
- **|A ∩ B|**: Usuarios que calificaron ambos productos
- **|A ∪ B|**: Usuarios que calificaron al menos uno

**Ventajas:**
- Normalizado entre 0% y 100%
- Simétrico: J(A,B) = J(B,A)
- No sesgado por popularidad del producto

## 📈 Secciones del Notebook

### 1. Construcción del Grafo Bipartito
- Carga del dataset (rutas relativas)
- Filtrado de reseñas de 5 estrellas
- Eliminación de usuarios/productos con pocas conexiones
- Creación del grafo bipartito con NetworkX

### 2. Análisis de la Red Bipartita
- Matriz de biadyacencia (formato disperso)
- Visualización de la matriz
- Análisis de grados de conectividad
- Identificación de nodos más activos

### 3. Proyección a Red de Productos
- Proyección ponderada con `weighted_projected_graph()`
- Análisis de pesos (usuarios compartidos)
- Distribución de conexiones

### 4. Sistema de Recomendación
- Implementación de Similaridad de Jaccard
- Función `get_product_recommendations()`
- Filtrado de duplicados perfectos (100% similaridad)
- Demostración con productos aleatorios

### 5. Visualización e Interactividad
- **Red Estrella**: Producto central con vecinos
- **Dropdowns Interactivos**: Selección de productos y N recomendaciones
- Actualización dinámica de visualizaciones

## 🔍 Casos Especiales

### Similaridad del 100%
Indica que dos productos tienen **exactamente el mismo conjunto de usuarios**. Esto puede significar:
- Productos duplicados en el catálogo
- Variantes del mismo producto (diferentes colores/tamaños)
- Productos en bundle

El sistema puede filtrar estos casos usando `exclude_perfect_match=True`.

## 📊 Dataset

**Amazon Electronics Reviews**
- Fuente: Amazon Product Reviews
- Contenido: Calificaciones de usuarios sobre productos electrónicos
- Campos: `userId`, `productId`, `Rating`, `timestamp`
- Filtrado: Solo reseñas de 5 estrellas
- Umbral: Mínimo 4 conexiones por usuario/producto

## 🎨 Visualizaciones

1. **Matriz de Biadyacencia**: Heatmap mostrando conexiones usuario-producto
2. **Distribuciones de Grado**: Histogramas de conectividad
3. **Red Estrella**: Visualización interactiva con:
   - Nodo central (verde): Producto seleccionado
   - Nodos vecinos (naranja): Productos recomendados
   - Aristas rojas: Grosor proporcional a la similaridad

## 🛠️ Personalización

El sistema permite ajustar:
- `min_user_reviews`: Mínimo de reseñas por usuario
- `min_product_reviews`: Mínimo de reseñas por producto
- `sample_ratio`: Proporción del dataset a usar
- `n_recommendations`: Número de recomendaciones
- `exclude_perfect_match`: Filtrar duplicados perfectos

## 📝 Notas Técnicas

- **Eficiencia**: Usa matrices dispersas de SciPy para grandes grafos
- **Portabilidad**: Rutas relativas con `os.path.join()`
- **Escalabilidad**: Muestreo configurable del dataset
- **Interactividad**: Widgets de IPython para exploración dinámica

## 🤝 Contribuciones

Proyecto académico desarrollado como parte del estudio de sistemas de recomendación basados en grafos bipartitos.

## 📄 Licencia

Proyecto educativo de código abierto.
