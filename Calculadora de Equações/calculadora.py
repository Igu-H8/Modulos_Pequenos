import ast
import operator

operadores = {
    ast.Add: operator.add, # adição 1 + 1
    ast.Sub: operator.sub, # subtração 1 - 1
    ast.Mult: operator.mul, # multiplicação 1 * 1
    ast.Div: operator.truediv, # divisão 1 / 1
    ast.Pow: operator.pow, # potência 1 ** 1
    ast.Mod: operator.mod, # módulo 1 % 1
    ast.USub: operator.neg, # valor negativo -1
}

def ler_calcular(expressao):
    def _eval(no):
        if isinstance(no, ast.Constant):
            return no.value
        
        elif isinstance(no, ast.BinOp):
            return operadores[type(no.op)](_eval(no.left),
                                              _eval(no.right))
        
        elif isinstance(no, ast.UnaryOp):
            return operadores[type(no.op)](_eval(no.operand))
        
        else:
            raise ValueError("Operação não permitida")

    no = ast.parse(expressao, mode='eval').body
    return _eval(no)

def menu():
    while True:
        conta = input("Digite um cálculo (ou 'sair' para encerrar): ")

        if conta.lower() == "sair":
            break

        try:
            resultado = ler_calcular(conta)
            print("Resultado:", resultado)

        except Exception as e:
            print("Erro:", e)

menu()
