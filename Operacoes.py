# MÓDULO: Operacoes.py

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("Erro: divisão por zero não é permitida.")
    return a / b

def executar_operacao(operacao, a, b):
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
