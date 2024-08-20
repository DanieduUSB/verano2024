n = 1
a = 1
d = 0

if n < 1:
    print("El número elegido no puede ser menor que 1")
    exit

if n != abs(n):
    print("El número elegido debe ser entero")
    exit

while a <= n:
    if n % a == 0:
        d = d + 1
    else:
        pass
    a = a + 1

if n == 1:
    print(f"El número {n} tiene 1 divisor y no es primo")
if d == 2:
    print(f"El número {n} tiene {d} divisores y es primo")
else:
    print(f"El número {n} tiene {d} divisores y no es primo")