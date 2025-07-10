from itertools import permutations

# Conjuntos de dígitos y operadores
digitos = '123456789'
operadores = '+-*/'

# Almacenar resultados únicos y sus expresiones
resultados = set()
resultado_a_expresion = {}

# Variables de control
contador = 0

# Función para construir la expresión alternando símbolos
def intercalar(digs, ops, empieza_con='digito'):
    expr = []
    if empieza_con == 'digito':
        for d, o in zip(digs, ops + ('',)):  # Añadir operador si lo hay
            expr.append(d)
            if o:
                expr.append(o)
    else:  # empieza con operador unario (+ o -)
        expr.append(ops[0])
        for d, o in zip(digs, ops[1:] + ('',)):
            expr.append(d)
            if o:
                expr.append(o)
    return ''.join(expr)

# ----------- Caso 1: Expresiones que empiezan con dígito -----------
for o in range(0, 5):  # o = número de operadores (0 a 4)
    d = o + 1          # d = número de dígitos
    for digs in permutations(digitos, d):
        for ops in permutations(operadores, o):
            expr = intercalar(digs, ops, empieza_con='digito')
            try:
                val = eval(expr)
                contador += 1
                print(f"Process: {contador} -- expresión: {expr} -- valor {val}")
                if isinstance(val, int) or val.is_integer():
                    val = int(val)
                    resultados.add(val)
                    resultado_a_expresion.setdefault(val, []).append(expr)
            except Exception:
                continue

# ----------- Caso 2: Expresiones que empiezan con operador unario -----------
for o in range(1, 5):  # total operadores incluyendo el unario inicial
    d = o  # número de dígitos
    for digs in permutations(digitos, d):
        for first_op in ['+', '-']:  # únicos unarios válidos
            if o == 1:
                ops = (first_op,)
                expr = intercalar(digs, ops, empieza_con='operador')
                try:
                    val = eval(expr)
                    contador += 1
                    print(f"Process: {contador} -- expresión: {expr} -- valor {val}")
                    if isinstance(val, int) or val.is_integer():
                        val = int(val)
                        resultados.add(val)
                        resultado_a_expresion.setdefault(val, []).append(expr)
                except Exception:
                    continue
            else:
                for ops_rest in permutations('*/-', o - 1):
                    ops = (first_op,) + ops_rest
                    expr = intercalar(digs, ops, empieza_con='operador')
                    try:
                        val = eval(expr)
                        contador += 1
                        print(f"Process: {contador} -- expresión: {expr} -- valor {val}")
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

# Mostrar resumen
print(f"Valor mínimo: {min_val}")
print(f"Valor máximo: {max_val}")
print(f"Cantidad total de resultados enteros distintos: {len(resultados)}")
print(f"¿Intervalo entero completo entre mínimo y máximo?: {is_continuous}")

