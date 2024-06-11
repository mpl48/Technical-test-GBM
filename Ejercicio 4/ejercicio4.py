import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Cargando los datos desde el archivo Excel
file_path = 'data_customer_classification 1.xlsx'
data = pd.read_excel(file_path)


customer_data = data.groupby('customer_id').agg(
    total_spent=pd.NamedAgg(column='tran_amount', aggfunc='sum'),
    max_spent=pd.NamedAgg(column='tran_amount', aggfunc='max'),
    frequency=pd.NamedAgg(column='tran_amount', aggfunc='size')
).reset_index()

percentiles = customer_data['total_spent'].quantile([0.33, 0.66]).tolist()

# Crear la columna de categorías basada en los percentiles
customer_data['value_category'] = pd.cut(customer_data['total_spent'],
                                         bins=[0, 973, 1414, float('inf')],
                                         labels=['low', 'medium', 'high'])

# Visualizar la distribución de las categorías
category_counts = customer_data['value_category'].value_counts(normalize=True) * 100

# Extracción de características y etiquetas
X = customer_data[['total_spent', 'max_spent', 'frequency']]
y = customer_data['value_category']

# Normalización de las características
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# División en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Construcción del modelo de red neuronal
model = Sequential([
    Dense(64, input_shape=(3,), activation='relu'),
    Dense(64, activation='relu'),
    Dense(3, activation='softmax')
])

# Compilación del modelo
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Convertir las etiquetas a códigos numéricos para usar en Keras
y_train_encoded = y_train.astype('category').cat.codes
y_test_encoded = y_test.astype('category').cat.codes

# Entrenamiento del modelo
history = model.fit(X_train, y_train_encoded, epochs=50, batch_size=32, validation_split=0.2, verbose=1)

from sklearn.metrics import classification_report, confusion_matrix
import numpy as np

# Realizar predicciones en el conjunto de prueba
y_pred = model.predict(X_test)
y_pred_classes = np.argmax(y_pred, axis=1)

# Matriz de confusión
cm = confusion_matrix(y_test_encoded, y_pred_classes)
print("Matriz de Confusión:")
print(cm)

# Informe de clasificación
cr = classification_report(y_test_encoded, y_pred_classes, target_names=['low', 'medium', 'high'])
print("Informe de Clasificación:")
print(cr)