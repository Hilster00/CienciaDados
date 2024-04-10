from sklearn.linear_model import LogisticRegression

# Dados de exemplo
X = [[1], [2], [3], [4]]
y = [0, 0, 1, 1]

# Criando o modelo de regressão logística
model = LogisticRegression()

# Treinando o modelo
model.fit(X, y)

# Predizendo valores
X_test = [[5], [6]]
predictions = model.predict(X_test)

print("Predições:", predictions)
