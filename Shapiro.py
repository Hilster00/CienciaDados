import numpy as np

def shapiro_wilk_test(data):
    n = len(data)
    data = sorted(data)
    m = np.mean(data)
    s = np.std(data, ddof=1)

    # Calculando os coeficientes W
    a = [0.0000000000006711, 0.0251960328241694, -0.399078163927465, -0.967468097056937, -1.8068993138886, -2.0052640144489]
    m_prime = np.mean([data[i] for i in range(n // 2)])
    w = np.dot(a, [np.log(data[i] - m_prime) - np.log(data[n - i - 1] - m_prime) for i in range(n // 2)])

    # Calculando a estatística de teste W
    W = (1 - 0.666666666666667 / n - 0.1 / n**2) * (w**2)

    # Calculando o p-valor
    mu = 0.9976948891432494  # média dos coeficientes para n<=11
    sigma = 0.0037336687093218  # desvio padrão dos coeficientes para n<=11
    Z = (np.log(1 - W) - mu) / sigma
    p_value = 2 * (1 - stats.norm.cdf(abs(Z)))

    return W, p_value

# Dados de exemplo (substitua isso pelos seus dados)
data = np.random.normal(loc=0, scale=1, size=100)

# Teste de Shapiro-Wilk
statistic, p_value = shapiro_wilk_test(data)

# Exibir resultados
print("Estatística de teste:", statistic)
print("Valor p:", p_value)

# Interpretar o resultado
alpha = 0.05
if p_value > alpha:
    print("Não rejeitamos a hipótese nula - os dados parecem ser normalmente distribuídos.")
else:
    print("Rejeitamos a hipótese nula - os dados não parecem ser normalmente distribuídos.")
