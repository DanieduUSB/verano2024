def array(n):

    ordenado = True

    for i in range(0,len(n)):
        for j in range(i + 1, len(n)):
            if n[i] > n[j]:
                ordenado == False
                print("El array no esta ordenado")
                return
    
    print("El array esta ordenado")

array([2,3,7,6,8])

"""cadn = "21"

for i in range(0,2):
    print(f"i: {i}")
    for j in range(i + 1, 2):
        print(f"j: {j}")
        if cadn[i] > cadn[j]:
            print("no ordenado")"""
