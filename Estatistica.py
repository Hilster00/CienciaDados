import scipy
import numpy as np


def binomial(evento,chance,tentativas):
    return scipy.stats.binom.pmf(evento,tentativas,chance)

# Função para calcular os coeficientes da regressão linear
def regressao_linear(x, y):
    n = len(x)
    # Calculando as médias de x e y
    x_medio = np.mean(x)
    y_medio = np.mean(y)
    
    # Calculando os coeficientes da regressão
    b1 = np.sum((x - x_medio) * (y - y_medio)) / np.sum((x - x_medio) ** 2)
    b0 = y_medio - b1 * x_medio
    
    return b0, b1

# Função para fazer a previsão com base nos coeficientes da regressão
def prever(b0, b1, x):
    return b0 + b1 * x

# Função para calcular o coeficiente de determinação (R²)
def coeficiente_determinacao(y_real, y_pred):
    ss_res = np.sum((y_real - y_pred) ** 2)
    ss_tot = np.sum((y_real - np.mean(y_real)) ** 2)
    r2 = 1 - (ss_res / ss_tot)
    return r2


if __name__=="__main__":
  print(binomial(0, 1/99, 200))

# Dados de exemplo
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 4, 5, 6])

# Calculando os coeficientes da regressão
b0, b1 = regressao_linear(x, y)

# Fazendo previsões
previsao = prever(b0, b1, x)

# Calculando o coeficiente de determinação
r2 = coeficiente_determinacao(y, previsao)

# Exibindo os resultados
print("Coeficiente b0:", b0)
print("Coeficiente b1:", b1)
print("Previsões:", previsao)
print("Coeficiente de determinação (R²):", r2)
