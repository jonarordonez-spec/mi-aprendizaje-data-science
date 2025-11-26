"""
Demostración Profesional de Regresión Lineal
Clase 7 - Curso de Ciencia de Datos
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import warnings
warnings.filterwarnings('ignore')

class ProfessionalLinearRegression:
    def __init__(self):
        self.setup_visualization_style()
        self.models = {}
        
    def setup_visualization_style(self):
        plt.style.use('seaborn-v0_8-whitegrid')
        sns.set_palette("tab10")
        plt.rcParams['figure.figsize'] = (10, 6)
        
    def basic_regression_demonstration(self):
        print("📈 DEMOSTRACIÓN BÁSICA DE REGRESIÓN LINEAL")
        print("=" * 50)
        
        # Datos de ejemplo simples (de tu notebook)
        X_train = np.array([[1], [2], [3]])
        y_train = np.array([[100], [150], [125]])
        
        print("📊 Datos de Entrenamiento:")
        training_data = pd.DataFrame({
            'X': X_train.flatten(),
            'y': y_train.flatten()
        })
        print(training_data)
        
        # Crear y entrenar modelo
        model = LinearRegression()
        model.fit(X_train, y_train)
        
        # Coeficientes del modelo
        slope = model.coef_[0][0]
        intercept = model.intercept_[0]
        
        print(f"\n🔧 Parámetros del Modelo:")
        print(f"   Pendiente (β1): {slope:.4f}")
        print(f"   Intercepto (β0): {intercept:.4f}")
        print(f"   Ecuación: y = {slope:.4f} * x + {intercept:.4f}")
        
        # Predicciones
        X_test = np.array([[4], [5]])
        predictions = model.predict(X_test)
        
        print(f"\n🎯 Predicciones:")
        for i, (x, pred) in enumerate(zip(X_test.flatten(), predictions.flatten())):
            print(f"   X = {x} → y_pred = {pred:.2f}")
        
        # Visualización profesional
        self._plot_basic_regression(X_train, y_train, model, slope, intercept)
        
        self.models['basic'] = model
        return model, predictions
    
    def _plot_basic_regression(self, X_train, y_train, model, slope, intercept):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Gráfica 1: Datos y línea de regresión
        x_range = np.linspace(0, 6, 100).reshape(-1, 1)
        y_range = model.predict(x_range)
        
        ax1.scatter(X_train, y_train, color='blue', s=100, 
                   label='Datos de entrenamiento', alpha=0.7, edgecolors='black')
        ax1.plot(x_range, y_range, color='red', linewidth=2, 
                label=f'y = {slope:.2f}x + {intercept:.2f}')
        
        # Predicciones
        X_pred = np.array([[4], [5]])
        y_pred = model.predict(X_pred)
        ax1.scatter(X_pred, y_pred, color='green', s=150, marker='*',
                   label='Predicciones', edgecolors='black')
        
        ax1.set_title('Regresión Lineal Simple', fontweight='bold', fontsize=14)
        ax1.set_xlabel('Variable Independiente (X)')
        ax1.set_ylabel('Variable Dependiente (y)')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Gráfica 2: Residuals
        y_train_pred = model.predict(X_train)
        residuals = y_train - y_train_pred
        
        ax2.scatter(y_train_pred, residuals, color='purple', s=100, alpha=0.7)
        ax2.axhline(y=0, color='red', linestyle='--', alpha=0.7)
        ax2.set_title('Análisis de Residuales', fontweight='bold', fontsize=14)
        ax2.set_xlabel('Valores Predichos')
        ax2.set_ylabel('Residuales')
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('../images/basic_regression_analysis.png', dpi=300, 
                   bbox_inches='tight')
        plt.show()
    
    def sales_prediction_case_study(self):
        print("\n🏢 CASO DE ESTUDIO: PREDICCIÓN DE VENTAS")
        print("=" * 50)
        
        # Datos de ejemplo de ventas (de tu notebook)
        months = np.array([[1], [2], [3], [4], [5], [6]])
        sales = np.array([[7000], [9000], [5000], [11000], [10000], [13000]])
        
        sales_data = pd.DataFrame({'Mes': months.flatten(), 'Ventas': sales.flatten()})
        print("📈 Datos Históricos de Ventas:")
        print(sales_data.to_string(index=False))
        
        # Entrenar modelo
        sales_model = LinearRegression()
        sales_model.fit(months, sales)
        
        slope = sales_model.coef_[0][0]
        intercept = sales_model.intercept_[0]
        print(f"\n🔧 Modelo de Ventas Entrenado:")
        print(f"   Pendiente: ${slope:.2f} (incremento mensual)")
        print(f"   Intercepto: ${intercept:.2f} (ventas base)")
        
        # Predicciones
        future_months = np.array([[7], [8], [9], [10]])
        future_predictions = sales_model.predict(future_months)
        
        print(f"\n🎯 Predicciones de Ventas Futuras:")
        future_forecast = pd.DataFrame({
            'Mes': future_months.flatten(),
            'Ventas_Predichas': future_predictions.flatten()
        })
        print(future_forecast.to_string(index=False))
        
        print(f"\n✅ Demostración completada!")
        
        self.models['sales'] = sales_model
        return sales_model, future_predictions
    
    def run_complete_demonstration(self):
        print("🚀 DEMOSTRACIÓN PROFESIONAL DE REGRESIÓN LINEAL")
        print("=" * 70)
        
        self.basic_regression_demonstration()
        self.sales_prediction_case_study()
        
        print("\n✅ DEMOSTRACIÓN COMPLETADA EXITOSAMENTE")
        return self.models

if __name__ == "__main__":
    demo = ProfessionalLinearRegression()
    models = demo.run_complete_demonstration()
