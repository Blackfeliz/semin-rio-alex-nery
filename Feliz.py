import math

# Função para calcular a segunda derivada numericamente
def segunda_derivada(f, x, h=1e-5):
    return (f(x + h) - 2*f(x) + f(x - h)) / (h ** 2)

# Entrada da função como string
f_str = input("Digite a função f(x) (ex: x**2 + 3*x): ")

# Converter string para função
def f(x):
    return eval(f_str)

# Entradas do intervalo e erro
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
erro_max = float(input("Digite o erro máximo permitido: "))

# Estimar máximo de |f''(x)| numericamente
samples = 1000
xs = [a + i * (b - a) / samples for i in range(samples + 1)]
max_f2 = max(abs(segunda_derivada(f, x)) for x in xs)

# Calcular n necessário com base no erro
n = math.ceil(math.sqrt(((b - a)**3 * max_f2) / (24 * erro_max)))
h = (b - a) / n

# Método do ponto médio
soma = 0
for i in range(n):
    xi = a + i * h
    mi = xi + h / 2
    soma += f(mi)

integral_aprox = h * soma

print(f"\nNúmero de subintervalos necessário: {n}")
print(f"Valor aproximado da integral: {integral_aprox:.8f}")


# Estimar máximo de |f''(x)| numericamente
samples = 1000
xs = [a + i * (b - a) / samples for i in range(samples + 1)]
max_f2 = max(abs(segunda_derivada(f, x)) for x in xs)

# Calcular n necessário com base no erro
n = math.ceil(math.sqrt(((b - a)**3 * max_f2) / (24 * erro_max)))
h = (b - a) / n
