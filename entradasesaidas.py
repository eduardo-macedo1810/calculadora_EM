# =============================================================================
# MÓDULO: EntradaSaida.py
# Contém funções de leitura de dados do usuário e exibição de resultados
# =============================================================================


def ler_numero_ou_fim(mensagem):
    """Lê um número digitado pelo usuário ou a palavra FIM.
    Aceita inteiros, decimais e complexos (ex: 3, 2.5, 3+2j).
    Retorna o número como complex, ou None se o usuário digitar FIM."""
    entrada = input(mensagem).strip()
    if entrada.upper() == 'FIM':
        return None
    try:
        return complex(entrada)
    except ValueError:
        raise ValueError(f"Entrada inválida: '{entrada}'. Use formatos como: 3, 2.5 ou 3+2j")


def ler_operacao():
    """Lê a operação desejada pelo usuário.
    Retorna o símbolo da operação (+, -, *, /) ou 'FIM'."""
    opcoes_validas = ['+', '-', '*', '/']
    entrada = input("Digite a operação desejada (+, -, *, /) ou FIM para encerrar: ").strip()
    if entrada.upper() == 'FIM':
        return 'FIM'
    if entrada not in opcoes_validas:
        raise ValueError(f"Operação inválida: '{entrada}'. Escolha entre +, -, *, /")
    return entrada


def formatar_numero(numero):
    """Formata um número para exibição.
    Se a parte imaginária for zero, exibe como número real."""
    if numero.imag == 0:
        real = numero.real
        if real == int(real):
            return str(int(real))
        return f"{real:.6g}"
    return str(numero)


def exibir_resultado(a, operacao, b, resultado):
    """Exibe a operação realizada e o resultado formatado na tela."""
    fa = formatar_numero(a)
    fb = formatar_numero(b)
    fr = formatar_numero(resultado)
    print(f"\nResultado: {fa} {operacao} {fb} = {fr}\n")


def exibir_boas_vindas():
    """Exibe a mensagem de boas-vindas ao iniciar a calculadora."""
    print("=" * 50)
    print("   CALCULADORA MODULARIZADA")
    print("   Suporte a números reais e complexos")
    print("   Digite FIM a qualquer momento para sair")
    print("=" * 50)
    print()


def exibir_encerramento():
    """Exibe mensagem de encerramento ao sair."""
    print("\nCalculadora encerrada. Até logo!")
    print("=" * 50)
