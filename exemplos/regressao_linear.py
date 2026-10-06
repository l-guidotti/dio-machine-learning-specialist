"""Regressão linear univariada por mínimos quadrados em dados sintéticos."""

import json
import random
from statistics import mean


def ajustar(pares: list[tuple[float, float]]) -> tuple[float, float]:
    media_x = mean(x for x, _ in pares)
    media_y = mean(y for _, y in pares)
    variacao_x = sum((x - media_x) ** 2 for x, _ in pares)
    if not variacao_x:
        raise ValueError("É necessário haver variação na entrada.")
    inclinacao = sum((x - media_x) * (y - media_y) for x, y in pares) / variacao_x
    return inclinacao, media_y - inclinacao * media_x


def avaliar(reais: list[float], previstos: list[float]) -> dict:
    if not reais or len(reais) != len(previstos):
        raise ValueError("As listas devem ter o mesmo tamanho e não estar vazias.")
    soma_erros_quadrados = sum((real - previsto) ** 2 for real, previsto in zip(reais, previstos))
    variacao_y = sum((real - mean(reais)) ** 2 for real in reais)
    return {
        "mae": mean(abs(real - previsto) for real, previsto in zip(reais, previstos)),
        "mse": soma_erros_quadrados / len(reais),
        "r2": 1 - soma_erros_quadrados / variacao_y if variacao_y else None,
    }


if __name__ == "__main__":
    gerador = random.Random(42)
    dados = []
    for _ in range(100):
        x = gerador.uniform(-5, 5)
        dados.append((x, 3 * x + 2 + gerador.gauss(0, 1)))
    gerador.shuffle(dados)
    treino, teste = dados[:75], dados[75:]
    inclinacao, intercepto = ajustar(treino)
    reais = [y for _, y in teste]
    previstos = [inclinacao * x + intercepto for x, _ in teste]
    media_treino = mean(y for _, y in treino)
    resultado = {
        "semente": 42,
        "amostras_treino": len(treino),
        "amostras_teste": len(teste),
        "inclinacao": inclinacao,
        "intercepto": intercepto,
        "modelo_no_teste": avaliar(reais, previstos),
        "baseline_media_treino_no_teste": avaliar(reais, [media_treino] * len(teste)),
    }
    print(json.dumps(resultado, indent=2, ensure_ascii=False))
