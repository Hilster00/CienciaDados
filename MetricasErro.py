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

def erro_quadratico_medio(y_true, y_pred):
    """
    Calcula o erro quadrático médio (MSE).

    Args:
    y_true: array-like, valores verdadeiros.
    y_pred: array-like, valores previstos.

    Returns:
    O MSE.
    """
    return np.mean((y_true - y_pred)**2)

# Exemplo de uso:
y_true = np.array([3, -0.5, 2, 7])
y_pred = np.array([2.5, 0.0, 2, 8])
mae = erro_medio_absoluto(y_true, y_pred)
mse = erro_quadratico_medio(y_true, y_pred)

print("Erro Médio Absoluto (MAE):", mae)
print("Erro Quadrático Médio (MSE):", mse)
