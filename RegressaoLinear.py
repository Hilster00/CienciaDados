import numpy as np
from sklearn.linear_model import LinearRegression

# Dados de exemplo
X = np.array([[1], [2], [3], [4]])
y = np.array([2, 3, 4, 5])

# Criando o modelo de regressão linear
model = LinearRegression()

# Treinando o modelo
model.fit(X, y)

# Predizendo valores
X_test = np.array([[5], [6]])
predictions = model.predict(X_test)

print("Predições:", predictions)
