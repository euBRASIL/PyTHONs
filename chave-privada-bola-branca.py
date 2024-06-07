import ecdsa

# Parâmetros da curva elíptica secp256k1 (usada no Bitcoin)
curve = ecdsa.SECP256k1.curve
generator = ecdsa.SECP256k1.generator

def reflect_point(point):
    # Reflete o ponto na curva elíptica
    return ecdsa.ellipticcurve.Point(curve, point.x(), -point.y() % curve.p())

def double_and_reflect(point):
    # Duplica o ponto e reflete o resultado na curva elíptica
    doubled_point = double_point(point)
    return reflect_point(doubled_point)

# Chave pública inicial
public_key = generator

# Número de vezes para duplicar e refletir a chave pública
num_iterations = 5

# Duplicação e reflexão da chave pública
for i in range(num_iterations):
    public_key = double_and_reflect(public_key)
    print(f"Iteração {i+1}:")
    print("X:", public_key.x())
    print("Y:", public_key.y())
    print()  # Adiciona uma linha em branco para separar as coordenadas

print("Coordenadas finais após", num_iterations, "iterações:")
print("X:", public_key.x())
print("Y:", public_key.y())
