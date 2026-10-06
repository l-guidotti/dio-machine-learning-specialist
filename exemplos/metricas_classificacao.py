"""Métricas binárias didáticas, com classe positiva igual a 1."""

import json


def dividir(numerador: int, denominador: int) -> float | None:
    return numerador / denominador if denominador else None


def avaliar(y_real: list[int], y_previsto: list[int]) -> dict:
    if not y_real or len(y_real) != len(y_previsto):
        raise ValueError("As listas devem ter o mesmo tamanho e não estar vazias.")
    if any(valor not in (0, 1) for valor in y_real + y_previsto):
        raise ValueError("Este exemplo aceita somente classes 0 e 1.")
    vp = sum(real == 1 and previsto == 1 for real, previsto in zip(y_real, y_previsto))
    vn = sum(real == 0 and previsto == 0 for real, previsto in zip(y_real, y_previsto))
    fp = sum(real == 0 and previsto == 1 for real, previsto in zip(y_real, y_previsto))
    fn = sum(real == 1 and previsto == 0 for real, previsto in zip(y_real, y_previsto))
    return {
        "classe_positiva": 1,
        "matriz_confusao": [[vn, fp], [fn, vp]],
        "ordem": "linhas = classe real [0, 1]; colunas = classe prevista [0, 1]",
        "acuracia": dividir(vp + vn, len(y_real)),
        "precisao": dividir(vp, vp + fp),
        "recall": dividir(vp, vp + fn),
        "especificidade": dividir(vn, vn + fp),
        "f1": dividir(2 * vp, 2 * vp + fp + fn),
    }


if __name__ == "__main__":
    reais = [1, 1, 1, 1, 0, 0, 0, 0]
    previstos = [1, 1, 1, 0, 1, 0, 0, 0]
    print(json.dumps(avaliar(reais, previstos), indent=2, ensure_ascii=False))
