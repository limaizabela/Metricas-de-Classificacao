def main() -> None:
    # Lê a quantidade de matrizes
    n = int(input().strip())
    
    best_accuracy = -1.0   # melhor acurácia encontrada
    best_index = -1        # índice da melhor matriz (inicia em 0)
    
    # Percorre cada matriz
    for idx in range(n):
        # Lê e separa os valores TP, FP, FN, TN
        tp, fp, fn, tn = map(int, input().strip().split(','))

        # TODO: Calcule a acurácia
        accuracy = (tp + tn) / (tp + fp + fn + tn)
        
        # Atualiza a melhor acurácia, se necessário
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_index = idx
                
    # Formata a acurácia para remover zeros finais e ponto desnecessário
    accuracy_str = f"{best_accuracy:.2f}".rstrip('0').rstrip('.')
    
    # Imprime o resultado
    print(f"Index: {best_index}")
    print(f"Accuracy: {accuracy_str}")

if __name__ == "__main__":
    main()