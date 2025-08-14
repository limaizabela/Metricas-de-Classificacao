def main() -> None:
    # Lê a quantidade de matrizes
    n = int(input().strip())
    
    best_precision = -1.0  # melhor precisão encontrada
    best_index = -1        # índice da melhor matriz (inicia em 0)
    
    # Percorre cada matriz
    for idx in range(n):
        # Lê e separa os valores TP, FP, FN, TN
        tp, fp, fn, tn = map(int, input().strip().split(','))

        # TODO: Calcule a precisão
        if (tp + fp) > 0:
            precision = tp / (tp + fp)
        else:
            precision = 0.0
        # Atualiza a melhor precisão, se necessário
        if precision > best_precision:
            best_precision = precision
            best_index = idx
    
    # Formata a precisão para remover zeros finais e ponto desnecessário
    precision_str = f"{best_precision:.2f}".rstrip('0').rstrip('.')
    
    # Imprime o resultado
    print(f"Index: {best_index}")
    print(f"Precision: {precision_str}")

if __name__ == "__main__":
    main()