from scipy.stats import shapiro

def teste_normalidade_amostra(amostra, alpha=0.05):
    """
    Realiza o teste de Shapiro-Wilk para verificar a normalidade de uma amostra.

    Args:
    amostra: array-like, amostra a ser testada.
    alpha: float, nível de significância (default=0.05).

    Returns:
    Uma tupla contendo o valor do teste estatístico e o p-valor.
    """
    stat, p_valor = shapiro(amostra)
    if p_valor > alpha:
        print("A amostra parece ser normal (p-valor:", p_valor, ")")
    else:
        print("A amostra não parece ser normal (p-valor:", p_valor, ")")

# Exemplo de uso:
amostra_normal = [0.1, 0.5, 0.3, 0.7, 0.2]
amostra_nao_normal = [0.8, 0.9, 0.7, 0.6, 0.5]

print("Teste para uma amostra normal:")
teste_normalidade_amostra(amostra_normal)

print("\nTeste para uma amostra não normal:")
teste_normalidade_amostra(amostra_nao_normal)
