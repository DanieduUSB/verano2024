n = 101
a = 1
d = 0

import time
import math

if n == 1:
    print(f"El número {n} tiene 1 divisor y no es primo")
    exit
elif n != math.floor(n) or n < 1:
    print("El número elegido debe ser un entero mayor o igual que 1")
    exit
else:
    while a <= n:
        if n % a == 0:
            d = d + 1
            print(f"{n} es divisible entre {a}")
        else:
            pass
        a = a + 1

    if d == 2:
        print(f"El número {n} tiene {d} divisores enteros y es primo")
    else:
        print(f"El número {n} tiene {d} divisores enteros y no es primo")