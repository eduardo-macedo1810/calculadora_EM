# =============================================================================
# MÓDULO: Operacoes.py
# Contém as quatro operações fundamentais com suporte a números complexos
# =============================================================================


def somar(a, b):
    """Retorna a soma de dois números (reais ou complexos)."""
    return a + b


def subtrair(a, b):
    """Retorna a subtração de dois números (reais ou complexos)."""
    return a - b


def multiplicar(a, b):
    """Retorna a multiplicação de dois números (reais ou complexos)."""
    return a * b


def dividir(a, b):
    """Retorna a divisão de dois números (reais ou complexos).
    Lança ValueError se o divisor for zero."""
    if b == 0:
        raise ValueError("Erro: divisão por zero não é permitida.")
    return a / b


def executar_operacao(operacao, a, b):
    """Recebe o símbolo da operação e dois números,
    chama a função correspondente e retorna o resultado."""
    if operacao == '+':
        return somar(a, b)
    elif operacao == '-':
        return subtrair(a, b)
    elif operacao == '*':
        return multiplicar(a, b)
    elif operacao == '/':
        return dividir(a, b)
    else:
        raise ValueError(f"Operação desconhecida: '{operacao}'")
