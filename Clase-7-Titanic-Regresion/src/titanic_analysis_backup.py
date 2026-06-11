"""
Análisis Profesional del Dataset Titanic
Clase 7 - Curso de Ciencia de Datos
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

class TitanicProfessionalAnalysis:
    def __init__(self, data_path="../data/titanic.csv"):
        self.data = pd.read_csv(data_path)
        self.results = {}
        self.setup_visualization_style()
        
    def setup_visualization_style(self):
        plt.style.use('seaborn-v0_8-whitegrid')
        sns.set_palette("husl")
        plt.rcParams['figure.figsize'] = (12, 8)
        
    def comprehensive_data_overview(self):
        print("🔍 ANÁLISIS COMPLETO DEL DATASET TITANIC")
        print("=" * 70)
        print(f"📊 DIMENSIONES: {self.data.shape[0]} filas × {self.data.shape[1]} columnas")
        print("\n📝 PRIMERAS FILAS:")
        print(self.data.head())
        
        print("\n📈 ESTADÍSTICAS DESCRIPTIVAS:")
        print(self.data.describe())
        
        # Valores nulos
        print("\n⚠️  ANÁLISIS DE VALORES NULOS:")
        null_analysis = pd.DataFrame({
            'Valores_Nulos': self.data.isnull().sum(),
            'Porcentaje_Nulos': (self.data.isnull().sum() / len(self.data)) * 100
        })
        print(null_analysis[null_analysis['Valores_Nulos'] > 0])
        return self.data.shape, null_analysis
    
    def data_cleaning_and_transformation(self):
        print("\n🧹 TRANSFORMACIÓN Y LIMPIEZA DE DATOS")
        # Transformar género (usando tu función original)
        def sex_transform(x):
            d = {'male': 'M', 'female': 'F'}
            return d[x]
        
        self.data['Sex'] = self.data['Sex'].apply(sex_transform)
        self.data['FamilySize'] = self.data['SibSp'] + self.data['Parch'] + 1
        self.data['IsAlone'] = (self.data['FamilySize'] == 1).astype(int)
        print("✅ Transformaciones aplicadas correctamente")
        print("\n📊 DATOS TRANSFORMADOS - PRIMERAS FILAS:")
        print(self.data[['Sex', 'FamilySize', 'IsAlone']].head())
        return self.data[['FamilySize', 'IsAlone']].head()
    
    def survival_analysis_by_demographics(self):
        print("\n👥 ANÁLISIS DE SUPERVIVENCIA POR DEMOGRÁFICAS")
        survival_rate = self.data['Survived'].mean() * 100
        print(f"📊 Tasa general de supervivencia: {survival_rate:.2f}%")
        
        # Supervivencia por género
        gender_survival = self.data.groupby('Sex')['Survived'].mean() * 100
        print(f"\n🎯 Supervivencia por género:")
        for gender, rate in gender_survival.items():
            print(f"   {gender}: {rate:.2f}%")
        
        # Supervivencia por clase
        class_survival = self.data.groupby('Pclass')['Survived'].mean() * 100
        print(f"\n💺 Supervivencia por clase:")
        for pclass, rate in class_survival.items():
            print(f"   Clase {pclass}: {rate:.2f}%")
        
        # Tabla cruzada
        print(f"\n📋 TABLA CRUZADA - Supervivencia vs Sexo:")
        survival_sex_table = pd.crosstab(self.data['Survived'], self.data['Sex'])
        print(survival_sex_table)
        
        self.results['survival_rates'] = {
            'general': survival_rate,
            'by_gender': gender_survival,
            'by_class': class_survival
        }
        return gender_survival, class_survival
    
    def explore_special_cases(self):
        print("\n🔍 CASOS ESPECIALES - ANÁLISIS")
        
        # Pasajeros que abordaron sin pagar
        free_passengers = self.data[self.data['Fare'] == 0]
        print(f"🎫 Pasajeros que abordaron sin pagar: {len(free_passengers)}")
        if len(free_passengers) > 0:
            print("   Detalles:")
            print(free_passengers[['Name', 'Pclass', 'Sex', 'Age']].head())
        
        # Persona que pagó más
        max_fare = self.data['Fare'].max()
        highest_payer = self.data[self.data['Fare'] == max_fare]
        print(f"\n💰 Pasajero que pagó más: ${max_fare:.2f}")
        if len(highest_payer) > 0:
            print("   Detalles:")
            print(highest_payer[['Name', 'Pclass', 'Sex', 'Age']].head())
        
        # Menores de 1 año
        babies = self.data[self.data['Age'] < 1]
        print(f"\n👶 Menores de 1 año: {len(babies)}")
        if len(babies) > 0:
            print("   Detalles:")
            print(babies[["Name", "Sex", "Age", "Survived"]].head())
    
    def advanced_visualizations(self):
        print("\n📊 GENERANDO VISUALIZACIONES PROFESIONALES...")
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        fig.suptitle('Análisis Exploratorio - Dataset Titanic', fontsize=16, fontweight='bold')
        
        # 1. Supervivencia general
        survival_counts = self.data['Survived'].value_counts()
        axes[0,0].pie(survival_counts, labels=['No Sobrevivió', 'Sobrevivió'], 
                     colors=['#e74c3c', '#2ecc71'], autopct='%1.1f%%', startangle=90)
        axes[0,0].set_title('Distribución de Supervivencia', fontweight='bold')
        
        # 2. Supervivencia por género
        gender_survival = pd.crosstab(self.data['Sex'], self.data['Survived'])
        gender_survival.plot(kind='bar', ax=axes[0,1], color=['#e74c3c', '#2ecc71'])
        axes[0,1].set_title('Supervivencia por Género', fontweight='bold')
        axes[0,1].set_xlabel('Género')
        axes[0,1].set_ylabel('Cantidad')
        axes[0,1].legend(['No', 'Sí'])
        axes[0,1].tick_params(axis='x', rotation=0)
        
        # 3. Supervivencia por clase
        class_survival = pd.crosstab(self.data['Pclass'], self.data['Survived'])
        class_survival.plot(kind='bar', ax=axes[0,2], color=['#e74c3c', '#2ecc71'])
        axes[0,2].set_title('Supervivencia por Clase', fontweight='bold')
        axes[0,2].set_xlabel('Clase')
        axes[0,2].set_ylabel('Cantidad')
        axes[0,2].legend(['No', 'Sí'])
        axes[0,2].tick_params(axis='x', rotation=0)
        
        # 4. Distribución de edades por supervivencia
        for survived in [0, 1]:
            subset = self.data[self.data['Survived'] == survived]['Age'].dropna()
            sns.histplot(subset, kde=True, label=f"Sobrevivió: {survived}", 
                        alpha=0.6, ax=axes[1,0])
        axes[1,0].set_title('Distribución de Edades por Supervivencia', fontweight='bold')
        axes[1,0].set_xlabel('Edad')
        axes[1,0].set_ylabel('Densidad')
        axes[1,0].legend()
        
        # 5. Tarifa vs Edad
        scatter = axes[1,1].scatter(self.data['Age'], self.data['Fare'], 
                                  c=self.data['Survived'], alpha=0.6, 
                                  cmap='coolwarm')
        axes[1,1].set_title('Tarifa vs Edad', fontweight='bold')
        axes[1,1].set_xlabel('Edad')
        axes[1,1].set_ylabel('Tarifa')
        plt.colorbar(scatter, ax=axes[1,1], label='Sobrevivió')
        
        # 6. Distribución de edades por clase
        for clase in [1, 2, 3]:
            self.data.Age[self.data.Pclass == clase].plot(kind='kde', ax=axes[1,2], 
                                                         label=f'Clase {clase}')
        axes[1,2].set_title('Distribución de Edades por Clase', fontweight='bold')
        axes[1,2].set_xlabel('Edad')
        axes[1,2].legend()
        
        plt.tight_layout()
        plt.savefig('../images/titanic_comprehensive_analysis.png', dpi=300, 
                   bbox_inches='tight', facecolor='white')
        plt.show()
        print("✅ Visualizaciones guardadas en 'images/titanic_comprehensive_analysis.png'")
    
    def generate_insights_report(self):
        print("\n💡 REPORTE EJECUTIVO DE INSIGHTS")
        print("=" * 60)
        
        # Cálculos de insights
        female_survival = self.data[self.data['Sex'] == 'F']['Survived'].mean() * 100
        male_survival = self.data[self.data['Sex'] == 'M']['Survived'].mean() * 100
        class1_survival = self.data[self.data['Pclass'] == 1]['Survived'].mean() * 100
        class3_survival = self.data[self.data['Pclass'] == 3]['Survived'].mean() * 100
        
        insights = [
            f"🎯 **Las mujeres tuvieron {female_survival:.1f}% de supervivencia vs {male_survival:.1f}% de los hombres**",
            f"💺 **La 1ra clase tuvo {class1_survival:.1f}% de supervivencia vs {class3_survival:.1f}% de la 3ra clase**"
        ]
        
        print("PRINCIPALES HALLAZGOS:")
        for i, insight in enumerate(insights, 1):
            print(f"{i}. {insight}")
        
        return insights
    
    def run_complete_analysis(self):
        print("🚀 INICIANDO ANÁLISIS PROFESIONAL DEL TITANIC")
        print("=" * 70)
        
        # Ejecutar todos los análisis
        self.comprehensive_data_overview()
        self.data_cleaning_and_transformation()
        self.survival_analysis_by_demographics()
        self.explore_special_cases()
        self.advanced_visualizations()
        insights = self.generate_insights_report()
        
        print("\n" + "=" * 70)
        print("✅ ANÁLISIS COMPLETADO EXITOSAMENTE")
        print("=" * 70)
        
        return self.results, insights

if __name__ == "__main__":
    analyzer = TitanicProfessionalAnalysis("../data/titanic.csv")
    results, insights = analyzer.run_complete_analysis()
