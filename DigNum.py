def DigNum(n):

    n == abs(n)
    chars = 0

    if n == 0:
        print(f"El número tiene 1 dígito")
    
    else:
        if n != int(n):
            nd = n
            while nd != int(nd):
                chars += 1
                nd = nd*10

        n = int(n)
        i = 1
        j = n / i

        while j >= 1:
            chars += 1
            i = i*10
            j = n / i
    
    if chars == 1:
        print(f"El número tiene 1 dígito")
    else:
        print(f"El número tiene {chars} dígitos")

    return

DigNum(10.325)

# Función que "DEBERÍA" calcular solo la cantidad de dígitos decimales
"""def Dec(n):
    dec = 0
    if n != int(n):
        nd = n
        while nd != int(nd):
            dec += 1
            nd = nd*10
            print(nd)
    print(dec)
    return
Dec(523560.152)"""

# Función que calcula la cantidad de dígitos si n es un entero distinto de 0
"""def DigNum(n):
    if n < 0:
        n = abs(n)
    i = 1
    chars = 0
    j = n / i
    while j > 1:
        chars += 1
        i = i*10
        j = n / i
    print(f"El número tiene {chars} dígitos")
    return

DigNum(-16.12)"""
