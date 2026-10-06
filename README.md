# DIO · Formação Machine Learning Specialist

Repositório de estudos para acompanhar a formação da [DIO](https://web.dio.me/track/formacao-machine-learning-specialist), registrar aprendizados e desenvolver um portfólio de Machine Learning.

**Autor:** [Lucas Guidotti](https://github.com/l-guidotti) · **Carga horária divulgada:** 92 horas · **Nível divulgado:** avançado.

## O que você encontra aqui

- Grade de 59 atividades, organizada nos oito módulos exibidos na plataforma.
- Resumos conceituais autorais para iniciar as anotações de cada módulo.
- Estrutura para os sete desafios de projeto e para o desafio de código.
- Dois exemplos autorais executáveis em Python: regressão linear e métricas de classificação.
- Modelos de notebook, anotações e registro de experimentos.

**Estado inicial:** atividades pendentes e desafios a implementar. Os resumos e exemplos foram preparados como apoio de estudo; não representam aulas assistidas, projetos entregues ou certificação concluída. Este repositório reúne um índice da formação e material autoral; aulas, vídeos, apostilas e arquivos privados permanecem na DIO.

## Trilha de estudos

| Módulo | Atividades | Conteúdo |
|---|---:|---|
| 01. Introdução ao Machine Learning | 8 | [Grade e anotações](modulos/01-introducao-machine-learning/README.md) |
| 02. Programação para Machine Learning | 9 | [Grade e anotações](modulos/02-programacao-machine-learning/README.md) |
| 03. Algoritmos de Treinamento em Machine Learning | 7 | [Grade e anotações](modulos/03-algoritmos-treinamento/README.md) |
| 04. Teoria do Aprendizado Estatístico | 6 | [Grade e anotações](modulos/04-aprendizado-estatistico/README.md) |
| 05. Fundamentos e Práticas de Deep Learning | 7 | [Grade e anotações](modulos/05-fundamentos-deep-learning/README.md) |
| 06. Frameworks de Deep Learning | 7 | [Grade e anotações](modulos/06-frameworks-deep-learning/README.md) |
| 07. Processamento de Imagens com Machine Learning | 8 | [Grade e anotações](modulos/07-processamento-imagens/README.md) |
| 08. Visão Computacional com Machine Learning | 7 | [Grade e anotações](modulos/08-visao-computacional/README.md) |

[Grade completa](docs/grade-do-curso.md) · [Progresso](docs/progresso.md) · [Glossário](docs/glossario.md)

## Projetos do portfólio

| Projeto | Pasta | Estado |
|---|---|---|
| 1. Treinamento de Redes Neurais com Transfer Learning | [Abrir roteiro](projetos/01-transfer-learning/README.md) | A implementar |
| 2. Redução de Dimensionalidade em Imagens para Redes Neurais | [Abrir roteiro](projetos/02-reducao-dimensionalidade-imagens/README.md) | A implementar |
| 3. Cálculo de Métricas de Avaliação de Aprendizado | [Abrir roteiro](projetos/03-metricas-avaliacao/README.md) | A implementar |
| 4. Criação de Uma Base de Dados e Treinamento da Rede YOLO | [Abrir roteiro](projetos/04-treinamento-yolo/README.md) | A implementar |
| 5. Criando um Sistema de Reconhecimento Facial do Zero | [Abrir roteiro](projetos/05-reconhecimento-facial/README.md) | A implementar |
| 6. Criando um Sistema de Recomendação por Imagens Digitais | [Abrir roteiro](projetos/06-recomendacao-imagens/README.md) | A implementar |
| 7. Criando um sistema de assistência virtual do zero | [Abrir roteiro](projetos/07-assistencia-virtual/README.md) | A implementar |

Cada pasta contém um roteiro de planejamento e um notebook inicial sem resultados. Os roteiros são sugestões autorais baseadas nos títulos; consulte o enunciado na DIO antes de implementar e enviar. O desafio de código está em [desafios/programacao-machine-learning](desafios/programacao-machine-learning/README.md).

## Começar a praticar

Os exemplos usam apenas a biblioteca padrão do Python 3.10 ou superior e dados sintéticos ou definidos no próprio código:

```bash
python exemplos/regressao_linear.py
python exemplos/metricas_classificacao.py
```

Para trabalhar com notebooks, crie um ambiente virtual e instale as ferramentas opcionais:

```bash
python -m venv .venv
```

No Windows PowerShell, é possível instalar e abrir o Jupyter sem ativar o ambiente:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m jupyterlab
```

No Linux ou macOS:

```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m jupyterlab
```

TensorFlow, Keras, OpenCV e ferramentas específicas de YOLO devem ser configurados dentro de cada projeto conforme o enunciado, o sistema e o hardware. Registre as versões efetivamente utilizadas; o arquivo inicial de dependências não é um lockfile.

## Rotina de estudo

1. Abra a atividade na DIO e escreva suas anotações no módulo correspondente.
2. Registre uma dúvida e um pequeno experimento que ajude a respondê-la.
3. Complete o projeto com dados, implementação, métricas e instruções de execução.
4. Atualize o [progresso](docs/progresso.md) e a tabela do projeto apenas após concluir o trabalho.
5. Faça um commit que descreva o aprendizado ou a alteração.

Consulte [como documentar os estudos](docs/como-estudar.md), [referências](docs/referencias.md) e [boas práticas de contribuição](CONTRIBUTING.md).

## Fonte e licença

Grade e títulos conferidos na [página da formação](https://web.dio.me/track/formacao-machine-learning-specialist) em **06/10/2026**. A página anuncia 51 cursos, sete desafios de projeto e um desafio de código. A soma das durações individuais exibidas nos cartões é 90 horas; mantive as 92 horas divulgadas como informação da plataforma, sem ajustar os cartões.

O material autoral deste repositório está sob [licença MIT](LICENSE). Conteúdos, marcas, enunciados e materiais de terceiros conservam seus próprios direitos e licenças. Este é um repositório pessoal de estudos, sem vínculo oficial com a DIO.
