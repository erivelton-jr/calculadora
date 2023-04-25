def validate(x):
    '''

    :param x: valor digitado na calculadora, se o valor não for digito
    a calculadora irá pedir novamente um numero.
    :return: se o valor digitado for um digito, ele retornará float.
    '''
    while True:
        if x.isdigit():
            return float(x)
        else:
            x = input('Erro: valor digitado não é um numero. Tente novamente.')


def operator(op):
    '''

    :param op: pergunta qual operação o usuario quer usar. se a operação não estiver na lista (operators)
    a caluculadora irá perguntaro novamente.
    :return: se a operação estiver na lista (operators), o valor será armazenado para fazer a operação.
    '''

    operators = ['+', '-', '/', '*']
    while op in operators:
        return op
    else:
        op = input(f'Erro! So podemos fazer com as seguintes operações: {operators}')


def math(op, x, y):
    '''

    :param op: Operação armazenada para fazer o cálculo.
    :param x: Primeiro numero (já validado) digitado pelo usuario.
    :param y: Segundo numero (já validado) digitado pelo usuario.
    :return: Retorna o resultado da operação.
    '''
    if operator(op) == '+':
        return x + y
    elif operator(op) == '-':
        return x - y
    elif operator(op) == '/':
        if x or y <= 0:
            return 0
        else:
            return x / y
    elif operator(op) == '*':
        return x * y


