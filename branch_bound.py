from itertools import permutations

digitos = '123456789'
operadores = '+-*/'

resultados = set()
resultado_a_expresion = {}
contador = 0

def eval_expr(expr):
    try:
        val = eval(expr)
        if isinstance(val, int) or val.is_integer():
            return int(val)
        return None
    except Exception:
        return None

def backtrack(expr, usados_dig, usados_op, empieza_con='digito'):
    global contador

    if empieza_con == 'digito':
        if len(usados_dig) >= 2 and 1 <= len(usados_op) <= 4:
            val = eval_expr(expr)
            if val is not None:
                contador += 1
                resultados.add(val)
                resultado_a_expresion.setdefault(val, []).append(expr)

        if len(usados_op) < 4:
            for op in operadores:
                if op not in usados_op:
                    backtrack(expr + op, usados_dig, usados_op | {op}, empieza_con='operador')

    else:  # empieza_con == 'operador'
        if len(usados_dig) < 9:
            for d in digitos:
                if d not in usados_dig:
                    # Poda para división no exacta
                    if len(expr) >= 2 and expr[-1] == '/':
                        try:
                            izq = int(expr[-2])
                            der = int(d)
                            if izq % der != 0:
                                continue  # poda
                        except:
                            continue
                    backtrack(expr + d, usados_dig | {d}, usados_op, empieza_con='digito')

# Caso 1: expresiones que empiezan con dígito
for o in range(1, 5):  # 1 a 4 operadores
    d = o + 1
    for digs in permutations(digitos, d):
        first_d = digs[0]
        expr = first_d
        usados_d = {first_d}
        backtrack(expr, usados_d, set(), empieza_con='digito')

# Caso 2: expresiones que empiezan con operador unario + o -
for o in range(1, 5):
    d = o
    for digs in permutations(digitos, d):
        for first_op in ['+', '-']:
            expr = first_op + digs[0]
            usados_d = {digs[0]}
            usados_o = {first_op}
            backtrack(expr, usados_d, usados_o, empieza_con='digito')

min_val = min(resultados)
max_val = max(resultados)
is_continuous = set(range(min_val, max_val + 1)).issubset(resultados)

print(f"Valor mínimo: {min_val}")
print(f"Valor máximo: {max_val}")
print(f"Cantidad total de resultados enteros distintos: {len(resultados)}")
print(f"¿Intervalo entero completo entre mínimo y máximo?: {is_continuous}")
print(f"Expresiones evaluadas: {contador}")

