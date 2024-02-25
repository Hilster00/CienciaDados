# Importando as bibliotecas necessárias
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Dados de exemplo
# Vamos supor que você tem uma tabela com três colunas: X1, X2 e X3 como características e Y como o alvo que você deseja prever.
# Aqui, criaremos dados de exemplo aleatórios para demonstração.

# Gerando dados de entrada (características)
X = np.random.rand(100, 3)

# Gerando dados de saída (alvo)
# Suponha que a relação alvo seja: Y = 2*X1 + 3*X2 + 4*X3 + erro
Y = 2*X[:,0] + 3*X[:,1] + 4*X[:,2] + np.random.randn(100)

# Dividindo os dados em conjuntos de treinamento e teste
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Criando e treinando o modelo de regressão linear
model = LinearRegression()
model.fit(X_train, Y_train)

# Avaliando o modelo
train_score = model.score(X_train, Y_train)
test_score = model.score(X_test, Y_test)

print("R² do conjunto de treinamento:", train_score)
print("R² do conjunto de teste:", test_score)

# Fazendo previsões
# Vamos supor que você tenha novos dados de entrada (X_new) para os quais deseja fazer previsões.
X_new = np.random.rand(5, 3)  # Gerando 5 exemplos de novos dados de entrada

predictions = model.predict(X_new)
print("Previsões:", predictions)
