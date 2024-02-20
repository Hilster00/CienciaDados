import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Função para gerar dados aleatórios a partir de uma distribuição normal
def gerar_dados_normal(media, desvio_padrao, tamanho_amostra):
    return np.random.normal(media, desvio_padrao, tamanho_amostra)

# Exemplo 1: Idade de pessoas
idade_media = 30
desvio_padrao_idade = 5
tamanho_amostra = 1000
idade = gerar_dados_normal(idade_media, desvio_padrao_idade, tamanho_amostra)

# Exemplo 2: Peso de pessoas (em kg)
peso_media = 70
desvio_padrao_peso = 10
peso = gerar_dados_normal(peso_media, desvio_padrao_peso, tamanho_amostra)

# Exemplo 3: Altura de pessoas (em cm)
altura_media = 170
desvio_padrao_altura = 8
altura = gerar_dados_normal(altura_media, desvio_padrao_altura, tamanho_amostra)

# Exemplo 4: Salário de trabalhadores (em milhares de reais)
salario_media = 5000
desvio_padrao_salario = 1000
salario = gerar_dados_normal(salario_media, desvio_padrao_salario, tamanho_amostra)

# Visualização dos dados gerados
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Histograma de idade
axs[0, 0].hist(idade, bins=30, density=True, color='blue', alpha=0.7)
x_idade = np.linspace(idade.min(), idade.max(), 100)
axs[0, 0].plot(x_idade, norm.pdf(x_idade, idade_media, desvio_padrao_idade), color='red', linestyle='--')
axs[0, 0].set_title('Distribuição de Idade')
axs[0, 0].set_xlabel('Idade')
axs[0, 0].set_ylabel('Densidade')

# Histograma de peso
axs[0, 1].hist(peso, bins=30, density=True, color='green', alpha=0.7)
x_peso = np.linspace(peso.min(), peso.max(), 100)
axs[0, 1].plot(x_peso, norm.pdf(x_peso, peso_media, desvio_padrao_peso), color='red', linestyle='--')
axs[0, 1].set_title('Distribuição de Peso')
axs[0, 1].set_xlabel('Peso (kg)')
axs[0, 1].set_ylabel('Densidade')

# Histograma de altura
axs[1, 0].hist(altura, bins=30, density=True, color='orange', alpha=0.7)
x_altura = np.linspace(altura.min(), altura.max(), 100)
axs[1, 0].plot(x_altura, norm.pdf(x_altura, altura_media, desvio_padrao_altura), color='red', linestyle='--')
axs[1, 0].set_title('Distribuição de Altura')
axs[1, 0].set_xlabel('Altura (cm)')
axs[1, 0].set_ylabel('Densidade')

# Histograma de salário
axs[1, 1].hist(salario, bins=30, density=True, color='purple', alpha=0.7)
x_salario = np.linspace(salario.min(), salario.max(), 100)
axs[1, 1].plot(x_salario, norm.pdf(x_salario, salario_media, desvio_padrao_salario), color='red', linestyle='--')
axs[1, 1].set_title('Distribuição de Salário')
axs[1, 1].set_xlabel('Salário (milhares de R$)')
axs[1, 1].set_ylabel('Densidade')

plt.tight_layout()
plt.show()
