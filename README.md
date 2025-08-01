Este trabajo consiste en proceso de análisis completo utilizando datos de sensores industriales para desarrollar un sistema de **mantenimiento predictivo** básico.

1.	Comprensión de los datos
Se trabaja con un conjunto de datos simulado que representa la lectura de sensores en una planta industrial de producción de motores eléctricos.
Cada registro del dataset incluirá:
- ID_Motor: identificador único del motor.
- Temperatura_C: temperatura medida en grados Celsius.
- Vibracion_mms: vibración medida en milímetros por segundo.
- Presion_bar: presión interna medida en bares.
- Humedad_%: humedad ambiental registrada cerca del motor.
- Horas_funcionamiento: número de horas que el motor ha estado funcionando desde su última revisión.
- Fallo_detectado: variable binaria (0 = no fallo, 1 = fallo) indicando si ocurrió un fallo en la siguiente semana tras la medición.
  
2.	Tratamiento de datos
Se realiza una limpieza básica:
- Eliminamos registros incompletos o inconsistentes.
- Detectamos y tratamos valores atípicos que puedan distorsionar el análisis.
- Normalización de variables.
  
3.	Análisis exploratorio de datos (EDA)
- Visualización de tendencias generales.
- Cálculos estadísticos básicos (media, mediana, desviación estándar).
- Correlaciones entre variables.
  
4.	Modelado predictivo
Implementación de algoritmos diferentes de clasificación para predecir el fallo (Fallo_detectado):
- Árboles de decisión.
- Regresión logística.
- Bosques aleatorios (Random Forest).
- Support Vector Machines (SVM).
Entrenamiento y evaluación de cada modelo utilizando métricas como:
- Precisión (accuracy).
- Recall.
- F1-score.
Comparación del rendimiento de los 4 modelos y selección del más adecuado según las métricas obtenidas.
  
5.	Integración en Business Intelligence
o	Crear un informe en Power BI:
	Cargar los datos procesados.
	Visualizar la distribución de fallos y las variables sensoriales más relevantes.
	Incluir gráficos de barras, líneas o matrices de correlación que ayuden a interpretar el comportamiento de los sensores.
	Presentar un resumen de la comparación de modelos de predicción.
6.	Conclusiones y recomendaciones
o	Redactar un breve informe final con las principales conclusiones extraídas.
o	Justificar la elección del mejor modelo.
o	Proponer acciones preventivas o de optimización basadas en los hallazgos del análisis.
