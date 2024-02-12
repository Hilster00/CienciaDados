import numpy as np
from scipy import stats

def intervalo_confianca(amostra, confianca=0.95):
    """
    Calcula o intervalo de confiança para a média de uma amostra.

    Args:
        amostra (array-like): A amostra de dados.
        confianca (float, opcional): O nível de confiança desejado. Padrão é 0.95.

    Returns:
        tuple: Uma tupla contendo a média da amostra e o intervalo de confiança.
    """
    amostra = np.array(amostra)
    media = np.mean(amostra)
    n = len(amostra)
    erro_padrao = stats.sem(amostra)
    intervalo = erro_padrao * stats.t.ppf((1 + confianca) / 2.0, n - 1)
    return media, intervalo

# Exemplo de uso
dados_amostra = [25, 30, 35, 40, 45, 50]  # Substitua com sua própria amostra de dados
media, intervalo = intervalo_confianca(dados_amostra)
print(f"Média da amostra: {media}")
print(f"Intervalo de confiança (95%): {media - intervalo} a {media + intervalo}")
