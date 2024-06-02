def derivada_curva_eliptica(x, y, a):
    # Calculando a derivada da equação da curva elíptica em relação a x
    numerador = 3 * x ** 2 + a
    denominador = 2 * y
    
    # Imprimindo o cálculo passo a passo
    print("Passo 1: Derivando a equação da curva elíptica")
    print("y^2 = x^3 + ax + b")
    print("Derivada em relação a x:")
    print("2y(dy/dx) = 3x^2 + a")
    print("dy/dx = (3x^2 + a) / (2y)")
    print()
    
    print("Passo 2: Substituindo os valores calculados")
    print(f"x = {x}, y = {y}, a = {a}")
    print(f"Numerador = 3 * {x}^2 + {a} = {numerador}")
    print(f"Denominador = 2 * {y} = {denominador}")
    print()
    
    # Verificando se o denominador é diferente de zero (para evitar divisão por zero)
    if denominador != 0:
        derivada = numerador / denominador
        print("Passo 3: Calculando a derivada")
        print(f"dy/dx = {numerador} / {denominador} = {derivada}")
        print()
        return derivada
    else:
        print("Divisão por zero! Denominador é igual a zero.")
        return None

# Exemplo de uso da função
x = 2
y = 3
a = 5

print("Calculando a derivada da curva elíptica:")
resultado_derivada = derivada_curva_eliptica(x, y, a)
