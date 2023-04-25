from calculadora import *

x = validate(input('Diga um valor: '))
y = validate(input('Diga outro valor: '))

op = operator(input('Qual operador deseja usar? '))
result = math(op, x, y)
print(result)
