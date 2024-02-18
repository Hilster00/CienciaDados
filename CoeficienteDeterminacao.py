import numpy as np

def coeficiente_de_determinacao(y_true, y_pred):
    """
    Calcula o coeficiente de determinação (R²).

    Args:
    y_true: array-like, valores verdadeiros.
    y_pred: array-like, valores previstos.

    Returns:
    O coeficiente de determinação (R²).
    """
    media_y_true = np.mean(y_true)
    ss_total = np.sum((y_true - media_y_true) ** 2)
    ss_residuo = np.sum((y_true - y_pred) ** 2)
    r_squared = 1 - (ss_residuo / ss_total)
    return r_squared
