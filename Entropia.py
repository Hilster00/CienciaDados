import numpy as np

def entropia(probabilidades):
    """
    Calcula a entropia de uma distribuição de probabilidades.
    
    Args:
    probabilidades: uma lista ou array de probabilidades.
    
    Returns:
    A entropia da distribuição de probabilidades.
    """
    # Remove probabilidades zero para evitar erros de log
    probabilidades = np.array(probabilidades)
    probabilidades = probabilidades[probabilidades != 0]
    
    # Calcula a entropia usando a fórmula de Shannon
    return -np.sum(probabilidades * np.log2(probabilidades))

# Exemplo de uso:
probabilidades = [0.5, 0.3, 0.2]
resultado_entropia = entropia(probabilidades)
print("Entropia:", resultado_entropia)
