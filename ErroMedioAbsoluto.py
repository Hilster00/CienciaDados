import numpy as np

def erro_medio_absoluto(y_true, y_pred):
    """
    Calcula o erro médio absoluto (MAE).

    Args:
    y_true: array-like, valores verdadeiros.
    y_pred: array-like, valores previstos.

    Returns:
    O MAE.
    """
    return np.mean(np.abs(y_true - y_pred))

# Exemplo de uso:
# Vendas reais de um produto em uma semana
vendas_reais = np.array([100, 150, 200, 250, 300])
# Previsões de vendas do modelo para a mesma semana
vendas_previstas = np.array([110, 160, 180, 240, 310])

# Calcula o MAE entre as vendas reais e previstas
mae = erro_medio_absoluto(vendas_reais, vendas_previstas)

print("O Erro Médio Absoluto (MAE) das previsões de vendas é:", mae)
