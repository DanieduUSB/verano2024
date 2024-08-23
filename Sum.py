# Fórmula matemática:

def Sum1(n):
    if n < 1 or n != int(n):
        return
    else:
        i = int(n * (n + 1) / 2)
        return i
    
print(Sum1(100))

# Recurrencia:

def Sum2(n):
    if n < 1 or n != int(n):
        return
    elif n == 1:
        return 1
    else:
        return Sum2(n-1) + n

print(Sum2(100))
