import os
os.chdir('/content/Evaluacion-ConstruccionSW-GrupoBETA')

readme = """# Evaluacion-ConstruccionSW-GrupoBETA

## Integrantes
- Fray Salcedo
- (Integrante 2)
- (Integrante 3)
- (Integrante 4)

## Descripción
Proyecto de evaluación práctica - Construcción de Software.
Implementación de modelos de Machine Learning con gestión colaborativa en Git/GitHub.

## ¿Cómo ejecutar el código?

### Requisitos
pip install pandas numpy matplotlib seaborn scikit-learn

### Pasos
1. Clonar el repositorio:
git clone https://github.com/fray958/Evaluacion-ConstruccionSW-GrupoBETA.git

2. Subir los datasets a la carpeta del proyecto:
   - Housing.csv (Dataset A)
   - healthcare_dataset.csv (Dataset B)

3. Ejecutar cada script:
python regresion_simple.py
python regresion_multiple.py
python regresion_polinomica.py
python regresion_logistica.py

## Tabla de Métricas

| Modelo | R² | MSE | Accuracy |
|--------|-----|-----|----------|
| Regresión Simple | 0.2729 | 3.68e+12 | — |
| Regresión Múltiple | 0.5081 | 2.49e+12 | — |
| Regresión Polinómica | 0.2953 | 3.56e+12 | — |
| Regresión Logística | — | — | 49.40% |

## Conclusiones

El modelo de Regresión Lineal Múltiple obtuvo el mejor rendimiento con R²=0.5081, explicando el 51% de la varianza del precio. Esto se debe a que incorpora más variables (area, bathrooms, stories) capturando más información del valor inmobiliario.

La Regresión Logística alcanzó un Accuracy del 49.40%, cercano al azar, lo que indica que las variables disponibles (edad, género, facturación) no son suficientes para predecir resultados de laboratorio. Se requieren variables clínicas directas para mejorar el modelo.
"""

with open('/content/Evaluacion-ConstruccionSW-GrupoBETA/README.md', 'w') as f:
    f.write(readme)

!git add README.md
!git commit -m "docs: actualiza README con metricas y conclusiones"
!git push https://fray958:TU_TOKEN@github.com/fray958/Evaluacion-ConstruccionSW-GrupoBETA.git main

print("✅ README.md actualizado y subido!")
