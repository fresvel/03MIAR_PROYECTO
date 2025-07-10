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

def puede_dividirse(num, den):
    # Verifica división exacta entera
    return den != 0 and num % den == 0

def backtracking(expr_list, usados_digitos, usados_operadores, resultado_parcial=None):
    global contador

    # Si la expresión termina con un dígito, evaluar y guardar resultado
    if len(expr_list) >= 3 and isinstance(expr_list[-1], str) and expr_list[-1].isdigit():
        expr_str = ''.join(expr_list)
        val = evaluar_expresion(expr_str)
        contador += 1
        if val is not None:
            resultados.add(val)
            resultado_a_expresion.setdefault(val, []).append(expr_str)

    # Alternar: si último es dígito, agregar operador; si último operador, agregar dígito
    ultimo = expr_list[-1]

    if ultimo.isdigit():
        # Agregar operador no usado
        for op in operadores:
            if op not in usados_operadores:
                # Poda: si operador es / y no hay dígito siguiente, no seguir (se agregará después)
                backtracking(expr_list + [op], usados_digitos, usados_operadores | {op}, resultado_parcial)
    else:
        # Último es operador, agregar dígito no usado
        for d in digitos:
            if d not in usados_digitos:
                # Si operador previo es '/', verificar divisibilidad
                if expr_list[-1] == '/':
                    # Extraer número antes del operador y comparar divisibilidad
                    # Esto es más complejo: idealmente evaluar resultado parcial paso a paso
                    # Para simplificar, evaluamos la expresión parcial y si no es entero, podar
                    expr_temp = ''.join(expr_list + [d])
                    val = evaluar_expresion(expr_temp)
                    if val is None:
                        continue  # poda
                backtracking(expr_list + [d], usados_digitos | {d}, usados_operadores, resultado_parcial)

# Inicialización: comenzar con dígito (sin operador unario)
for d in digitos:
    backtracking([d], {d}, set())

print(f"Total expresiones evaluadas: {contador}")
print(f"Resultados enteros encontrados: {len(resultados)}")
print(f"Min: {min(resultados)}, Max: {max(resultados)}")

