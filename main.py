# =============================================================================
# MÓDULO: Main.py
# Ponto de entrada do programa. Importa EntradaSaida e Operacoes.
# =============================================================================

from EntradaSaida import (ler_numero_ou_fim, ler_operacao,
                          exibir_resultado, exibir_boas_vindas,
                          exibir_encerramento)
from Operacoes import executar_operacao


def realizar_calculo():
    """Executa um ciclo completo de cálculo:
    lê os dois números e a operação, exibe o resultado.
    Retorna False se o usuário digitar FIM, True para continuar."""
    try:
        a = ler_numero_ou_fim("Digite o primeiro número (ou FIM para encerrar): ")
        if a is None:
            return False

        operacao = ler_operacao()
        if operacao == 'FIM':
            return False

        b = ler_numero_ou_fim("Digite o segundo número (ou FIM para encerrar): ")
        if b is None:
            return False

        resultado = executar_operacao(operacao, a, b)
        exibir_resultado(a, operacao, b, resultado)

    except ValueError as e:
        print(f"\n[!] {e}\n")

    return True


def loop_principal():
    """Mantém a calculadora rodando até o usuário digitar FIM."""
    continuar = True
    while continuar:
        continuar = realizar_calculo()


def main():
    """Ponto de entrada do programa."""
    exibir_boas_vindas()
    loop_principal()
    exibir_encerramento()


# =============================================================================
if __name__ == "__main__":
    main()
