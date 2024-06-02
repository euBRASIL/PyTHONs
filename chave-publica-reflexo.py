import ecdsa

# Parâmetros da curva elíptica secp256k1 (usada no Bitcoin)
curve = ecdsa.SECP256k1.curve
generator = ecdsa.SECP256k1.generator

def double_point(point):
    # Duplica o ponto na curva elíptica
    slope = (3 * point.x()**2 + curve.a()) * pow(2 * point.y(), -1, curve.p()) % curve.p()
    x = (slope**2 - 2 * point.x()) % curve.p()
    y = (slope * (point.x() - x) - point.y()) % curve.p()
    return ecdsa.ellipticcurve.Point(curve, x, y)

# Chave pública inicial
public_key = generator

# Número de vezes para duplicar a chave pública
num_duplications = 5

# Duplicação da chave pública
for i in range(num_duplications):
    public_key = double_point(public_key)
    print(f"Loop {i+1}:")
    print("X:", public_key.x())
    print("Y:", public_key.y())
    print()  # Adiciona uma linha em branco para separar as coordenadas

print("Coordenadas finais após", num_duplications, "duplicações:")
print("X:", public_key.x())
print("Y:", public_key.y())
