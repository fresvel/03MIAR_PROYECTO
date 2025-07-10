from itertools import permutations

digitos = '123456789'
operadores = '+-*/'

resultados = set()
resultado_a_expresion = {}
contador = 0

# Función para construir la expresión alternando símbolos
def intercalar(digs, ops, empieza_con='digito'):
    expr = []
    if empieza_con == 'digito':
        for d, o in zip(digs, ops + ('',)):
            expr.append(d)
            if o:
                expr.append(o)
    else:  # operador unario
        expr.append(ops[0])
        for d, o in zip(digs, ops[1:] + ('',)):
            expr.append(d)
            if o:
                expr.append(o)
    return ''.join(expr)

# ----------- Caso 1: Expresiones que empiezan con dígito -----------
for o in range(0, 5):  # o = número de operadores (0 a 4)
    for ops in permutations(operadores, o):  # operadores sin repetir
        d = o + 1
        for digs in permutations(digitos, d):
            expr = intercalar(digs, ops, empieza_con='digito')
            try:
                val = eval(expr)
                contador += 1
                print(f"Process: {contador} || expresión: {expr} ")

                if isinstance(val, int) or val.is_integer():
                    val = int(val)
                    resultados.add(val)
                    resultado_a_expresion.setdefault(val, []).append(expr)
            except Exception:
                continue

# ----------- Caso 2: Expresiones que empiezan con operador unario + o - -----------
for o in range(1, 5):  # total operadores (incluye el unario inicial)
    for first_op in ['+', '-']:
        otros_ops = [op for op in operadores if op != first_op]
        for ops_rest in permutations(otros_ops, o - 1):
            ops = (first_op,) + ops_rest
            d = o  # número de dígitos igual al total de operadores
            for digs in permutations(digitos, d):
                expr = intercalar(digs, ops, empieza_con='operador')
                try:
                    val = eval(expr)
                    contador += 1
                    print(f"Process: {contador} || expresión: {expr} ")
                    if isinstance(val, int) or val.is_integer():
                        val = int(val)
                        resultados.add(val)
                        resultado_a_expresion.setdefault(val, []).append(expr)
                except Exception:
                    continue

# ----------- Resultados finales -----------
min_val = min(resultados)
max_val = max(resultados)
is_continuous = set(range(min_val, max_val + 1)).issubset(resultados)

print(f"Valor mínimo: {min_val}")
print(f"Valor máximo: {max_val}")
print(f"Cantidad total de resultados enteros distintos: {len(resultados)}")
print(f"¿Intervalo entero completo entre mínimo y máximo?: {is_continuous}")
print(f"Total expresiones evaluadas: {contador}")

