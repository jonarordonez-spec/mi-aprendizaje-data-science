# Predicción de Incumplimiento de Pago en Tarjetas de Crédito

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

Proyecto final del curso *De cero a Ciencia de Datos* — desarrollo y comparación de modelos de machine learning para predecir defaults en tarjetas de crédito.

## 📌 Descripción

Este proyecto aplica técnicas de aprendizaje supervisado para predecir si un cliente incumplirá en el siguiente mes, utilizando el [UCI Credit Card Dataset](https://doi.org/10.24432/C55S3H) (30,000 observaciones). Se comparan dos modelos:
- **Regresión Logística**
- **Árbol de Decisiones**

El objetivo es identificar clientes de alto riesgo con base en su historial de pagos, facturación y perfil demográfico.

## 📊 Resultados clave

| Métrica     | Regresión Logística | Árbol de Decisiones |
|-------------|---------------------|---------------------|
| **F1-Score** | 0.5065              | **0.5189**          |
| **ROC-AUC**  | 0.7434              | **0.7580**          |

✅ El **Árbol de Decisiones** se selecciona como modelo final por su mejor equilibrio entre precisión y recall, así como su alta interpretabilidad.

🔍 **Variables más influyentes**:
1. `AVG_PAY_DELAY` (66.0% de importancia)
2. `PAY_0` (retraso en el pago más reciente)
3. `BILL_AMT1` (monto facturado)

## 🗂 Estructura del repositorio
├── notebooks/ # Jupyter Notebook con código completo
├── output/figuras/ # Gráficas generadas
├── output/tabla_comparacion.csv # Métricas comparativas
├── docs/ # Documentación (informe final)
└── README.md
## 📚 Referencias

- Yeh, I. C., & Lien, C. H. (2009). *The comparisons of data mining techniques for the predictive accuracy of probability of default of credit card clients*. Expert Systems with Applications, 36(2), 2473–2480. https://doi.org/10.1016/j.eswa.2007.12.020  
- UCI Machine Learning Repository. (2019). *Default of Credit Card Clients Dataset*. https://doi.org/10.24432/C55S3H

## 📄 Informe técnico

El informe completo (PDF) está disponible en [`docs/`](docs/).

---

> ✉️ Consultas: [jona.r.ordonez@gmail.com](mailto:jona.r.ordonez@gmail.com)
