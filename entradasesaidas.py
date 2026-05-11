# =============================================================================
# MÓDULO: EntradaSaida.py
# Contém funções de leitura de dados do usuário e exibição de resultados
# =============================================================================


def ler_numero_ou_fim(mensagem):
       entrada = input(mensagem).strip()
    if entrada.upper() == 'FIM':
        return None
    try:
        return complex(entrada)
    except ValueError:
        raise ValueError(f"Entrada inválida: '{entrada}'. Use formatos como: 3, 2.5 ou 3+2j")


def ler_operacao():
        opcoes_validas = ['+', '-', '*', '/']
    entrada = input("Digite a operação desejada (+, -, *, /) ou FIM para encerrar: ").strip()
    if entrada.upper() == 'FIM':
        return 'FIM'
    if entrada not in opcoes_validas:
        raise ValueError(f"Operação inválida: '{entrada}'. Escolha entre +, -, *, /")
    return entrada


def formatar_numero(numero):
        if numero.imag == 0:
        real = numero.real
        if real == int(real):
            return str(int(real))
        return f"{real:.6g}"
    return str(numero)


def exibir_resultado(a, operacao, b, resultado):
       fa = formatar_numero(a)
    fb = formatar_numero(b)
    fr = formatar_numero(resultado)
    print(f"\nResultado: {fa} {operacao} {fb} = {fr}\n")


def exibir_boas_vindas():
        print("=" * 50)
    print("   CALCULADORA MODULARIZADA")
    print("   Suporte a números reais e complexos")
    print("   Digite FIM a qualquer momento para sair")
    print("=" * 50)
    print()


def exibir_encerramento():
    print("\nCalculadora encerrada. Até logo!")
    print("=" * 50)
