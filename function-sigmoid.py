import sympy as sp

# Define a variável simbólica
x = sp.Symbol('x')

# Define a função sigmoide
def sigmoid(x):
    return 1 / (1 + sp.exp(-x))

# Calcula a derivada da função sigmoide em relação a x
derivada = sp.diff(sigmoid(x), x)

# Imprime a função sigmoide e sua derivada
print("Função sigmoide:", sigmoid(x))
print("Derivada da função sigmoide em relação a x:", derivada)

# Expandindo a derivada passo a passo
print("\nPasso a passo da expansão da derivada:")
passos = sp.steps(derivada, method='all')
for passo in passos:
    print(passo)
