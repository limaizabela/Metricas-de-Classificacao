# Metricas-de-Classificacao
## Cálculo de melhor acurácia, melhor precisão e menor taxa de falsos positivos

A fim de desenvolver habilidades práticas em ciência de dados, este projeto explora as métricas de classificação, como acurácia, precisão e taxa de falsos positivos, utilizando dados sintéticos para demonstrar seus cálculos em Python.

Os objetivos do desafio: encontrar a maior acurácia, a melhor precisão e a menor taxa de falsos positivos.

## Desafio 1:
Dadas n matrizes de confusão, crie um algoritmo que determine qual delas possui a maior acurácia (accuracy).

A acurácia é calculada por: accuracy = (TP + TN) / (TP + FP + FN + TN)

Retorne o índice e o valor da acurácia da matriz vencedora.

Entrada
Uma string contendo:

Um inteiro n (quantidade de matrizes).
Em seguida, exatamente n linhas, cada uma com quatro inteiros no formato TP,FP,FN,TN.
Saída
Index: X — onde X é o índice da matriz com maior acurácia.
Accuracy: Y — onde Y é a acurácia da matriz vencedora, arredondada para duas casas decimais (remova zeros finais desnecessários).

## Desafio 2:
Dadas n matrizes de confusão, crie um algoritmo que determine qual delas possui a maior precisão (precision).

A precisão é calculada por: precision = TP / (TP + FP)

Retorne o índice e o valor da precisão da matriz vencedora.

Entrada
Uma string contendo:

Um inteiro n (quantidade de matrizes).
Em seguida, exatamente n linhas, cada uma com quatro inteiros no formato TP,FP,FN,TN.
Saída
Index: X — onde X é o índice da matriz com maior precisão.
Precision: Y — onde Y é a precisão da matriz vencedora, arredondada para duas casas decimais (remova zeros finais desnecessários).

## Desafio 3:
Sua missão é desenvolver um algoritmo que analise n matrizes de confusão e selecione aquela com a menor Taxa de Falsos Positivos (FPR).

A fórmula da FPR (False Positive Rate) é: FPR = FP / (FP + TN)

Entrada
Uma string contendo:

Um número inteiro n, indicando o número de matrizes.
Em seguida, n linhas com 4 valores inteiros cada, separados por vírgula, representando: TP,FP,FN,TN.
Saída
Index: X — onde X é o índice da matriz com menor FPR (início em 0).
FPR: Y — a taxa de falsos positivos da matriz selecionada, com no máximo duas casas decimais (sem zeros finais desnecessários).
