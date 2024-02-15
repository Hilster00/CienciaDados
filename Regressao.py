class RegressaoLinear:
    def __init__(self):
        self.coeficientes = None

    def treinar(self, X, y):
        # Adiciona uma coluna de 1s para representar o termo de viés (intercepto)
        X = self._adicionar_coluna_de_1s(X)
        
        # Calcula os coeficientes usando a equação normal
        self.coeficientes = self._calcular_coeficientes(X, y)

    def prever(self, X):
        # Adiciona uma coluna de 1s para representar o termo de viés (intercepto)
        X = self._adicionar_coluna_de_1s(X)
        
        # Calcula as previsões usando os coeficientes calculados
        return X.dot(self.coeficientes)

    def _adicionar_coluna_de_1s(self, X):
        return np.c_[np.ones(X.shape[0]), X]

    def _calcular_coeficientes(self, X, y):
        return np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)

# Exemplo de uso:
import numpy as np

# Dados de entrada
X = np.array([[1], [2], [3], [4], [5]])
# Dados de saída
y = np.array([2, 4, 5, 4, 5])

# Instancia e treina o modelo de regressão linear
modelo = RegressaoLinear()
modelo.treinar(X, y)

# Realiza previsões para novos dados
novos_dados = np.array([[6], [7]])
previsoes = modelo.prever(novos_dados)
print("Previsões:", previsoes)
