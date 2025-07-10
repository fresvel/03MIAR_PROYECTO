digitos = '123456789'
operadores = '+-*/'

resultados = set()
resultado_a_expresion = {}
contador = 0

def evaluar_expresion(expr_str):
    try:
        val = eval(expr_str)
        if isinstance(val, int) or val.is_integer():
            return int(val)
        return None
    except:
        return None

def backtracking(expr_list, usados_digitos, usados_operadores, puede_empezar_operador_unario):
    global contador

    # Si la expresión termina con dígito, evaluar resultado
    if len(expr_list) >= 3 and expr_list[-1].isdigit():
        expr_str = ''.join(expr_list)
        val = evaluar_expresion(expr_str)
        contador += 1
        if val is not None:
            resultados.add(val)
            resultado_a_expresion.setdefault(val, []).append(expr_str)

    ultimo = expr_list[-1]

    if ultimo.isdigit():
        # Agregar operador no usado
        for op in operadores:
            if op not in usados_operadores:
                backtracking(expr_list + [op], usados_digitos, usados_operadores | {op}, False)
    else:
        # Último es operador, agregar dígito no usado
        for d in digitos:
            if d not in usados_digitos:
                backtracking(expr_list + [d], usados_digitos | {d}, usados_operadores, False)

    # Solo al inicio permitir operador unario
    if puede_empezar_operador_unario:
        for op_unario in ['+', '-']:
            if op_unario not in usados_operadores:
                for d in digitos:
                    backtracking([op_unario, d], {d}, {op_unario}, False)

# Iniciar backtracking con dígitos (sin operador unario)
for d in digitos:
    backtracking([d], {d}, set(), True)

print(f"Total expresiones evaluadas: {contador}")
print(f"Resultados enteros encontrados: {len(resultados)}")
print(f"Min: {min(resultados)}, Max: {max(resultados)}")

