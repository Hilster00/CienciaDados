import math

def media(lista):
    """
    Calcula a média de uma lista de valores.
    """
    return sum(lista) / len(lista)

def variancia(lista):
    """
    Calcula a variância de uma lista de valores.
    """
    media_valores = media(lista)
    return sum((x - media_valores) ** 2 for x in lista) / len(lista)

def desvio_padrao(lista):
    """
    Calcula o desvio padrão de uma lista de valores.
    """
    return math.sqrt(variancia(lista))

def correlacao(x, y):
    """
    Calcula o coeficiente de correlação entre duas listas de valores.
    """
    if len(x) != len(y):
        raise ValueError("As listas devem ter o mesmo tamanho.")
    media_x = media(x)
    media_y = media(y)
    numerador = sum((a - media_x) * (b - media_y) for a, b in zip(x, y))
    denominador_x = math.sqrt(sum((a - media_x) ** 2 for a in x))
    denominador_y = math.sqrt(sum((b - media_y) ** 2 for b in y))
    return numerador / (denominador_x * denominador_y)

# Exemplo de uso das funções:
dados_x = [1, 2, 3, 4, 5]
dados_y = [2, 3, 4, 5, 6]

print("Média de x:", media(dados_x))
print("Variância de x:", variancia(dados_x))
print("Desvio padrão de x:", desvio_padrao(dados_x))
print("Coeficiente de correlação entre x e y:", correlacao(dados_x, dados_y))
