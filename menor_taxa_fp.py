def main() -> None:
    # Lê a quantidade de matrizes
    n = int(input().strip())

    best_fpr = float('inf')  # menor FPR encontrado
    best_index = -1          # índice correspondente à menor FPR

    # Itera sobre cada matriz
    for idx in range(n):
        # Lê e separa os valores da matriz: TP, FP, FN, TN
        tp, fp, fn, tn = map(int, input().strip().split(','))

        # TODO: Calcule a taxa de falsos positivos
        fpr = fp / (fp + tn)

        # Atualiza se encontrar FPR menor
        if fpr < best_fpr:
            best_fpr = fpr
            best_index = idx

    # Formata a saída removendo zeros finais desnecessários
    fpr_str = f"{best_fpr:.2f}".rstrip('0').rstrip('.')

    # Exibe o resultado
    print(f"Index: {best_index}")
    print(f"FPR: {fpr_str}")

if __name__ == "__main__":
    main()