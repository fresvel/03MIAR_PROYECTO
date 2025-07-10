from itertools import permutations

# Conjuntos de dígitos y operadores
digitos = '123456789'
operadores = '+-*/'

# Almacenar resultados únicos y sus expresiones
resultados = set()
resultado_a_expresion = {}
contador = 0

# Función para evaluar expresiones seguras
def evaluar_expresion(expr_str):
    try:
        val = eval(expr_str)
        if isinstance(val, int) or val.is_integer():
            return int(val)
        return None
    except:
        return None

# Backtracking con poda basada en divisiones exactas
def backtracking(expr_list, usados_digitos, usados_operadores):
    global contador

    # Evaluar solo si termina en dígito
    if len(expr_list) >= 3 and expr_list[-1].isdigit():
        expr_str = ''.join(expr_list)
        val = evaluar_expresion(expr_str)
        contador += 1
        print(f"Eval #{contador:6} || Expr: {expr_str:15} || Resultado: {val}")
        if val is not None:
            resultados.add(val)
            resultado_a_expresion.setdefault(val, []).append(expr_str)

    ultimo = expr_list[-1]

    if ultimo.isdigit():
        # Añadir operador no repetido
        for op in operadores:
            if op not in usados_operadores:
                backtracking(expr_list + [op], usados_digitos, usados_operadores | {op})
    else:
        # Añadir dígito no repetido
        for d in digitos:
            if d not in usados_digitos:
                if expr_list[-1] == '/':
                    # Validar que la división sea exacta
                    if len(expr_list) >= 2 and expr_list[-2].isdigit():
                        num = int(expr_list[-2])
                        den = int(d)
                        if den == 0 or num % den != 0:
                            continue  # Poda: división no exacta
                    else:
                        continue  # No es seguro dividir
                backtracking(expr_list + [d], usados_digitos | {d}, usados_operadores)

# ----------- Caso 1: Comenzar con un dígito -----------
for d in digitos:
    backtracking([d], {d}, set())

# ----------- Caso 2: Comenzar con operador unario + o - -----------
for unario in ['+', '-']:
    for d in digitos:
        backtracking([unario, d], {d}, {unario})

# ----------- Resultados finales -----------
min_val = min(resultados)
max_val = max(resultados)
is_continuous = set(range(min_val, max_val + 1)).issubset(resultados)

print(f"\nTotal expresiones evaluadas: {contador}")
print(f"Resultados enteros encontrados: {len(resultados)}")
print(f"Min: {min_val}, Max: {max_val}")
print(f"¿Intervalo completo? {is_continuous}")

