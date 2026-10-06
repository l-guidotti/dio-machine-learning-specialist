# Exemplos autorais

Os exemplos abaixo foram criados para apoiar os estudos. Eles não representam soluções dos desafios oficiais da DIO. Requerem Python 3.10 ou superior e somente a biblioteca padrão.

- `python exemplos/regressao_linear.py`: gera 100 pares sintéticos, separa treino e teste e ajusta uma reta por mínimos quadrados. Compara MAE, MSE e R² com uma previsão constante baseada na média do treino.
- `python exemplos/metricas_classificacao.py`: calcula uma matriz de confusão e métricas binárias em uma lista de oito observações. Métricas indefinidas por denominador zero são retornadas como `null` no JSON.

A semente fixa ajuda a repetir o exemplo de regressão, mas o resultado em dados sintéticos não demonstra qualidade em um problema real. Altere o ruído, a semente e a proporção de teste e explique o que mudou.
