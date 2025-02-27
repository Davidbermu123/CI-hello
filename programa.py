def es_primo(n):
    """Devuelve True si n es un número primo, de lo contrario False."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Entrada de usuario
try:
    num = int(input("Ingrese un número: "))
    if es_primo(num):
        print(f"{num} es un número primo.")
    else:
        print(f"{num} no es un número primo.")
except ValueError:
    print("Por favor, ingrese un número entero válido.")
