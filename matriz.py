def maxMatriz(n):

    premax = []

    for column in range(0, len(n)):
        premax.append(n[column][0])
    
    for column in range(0,len(n)):
        for number in range(1,len(n[column])):
            if n[column][number] > premax[column]:
                premax[column] = n[column][number]
    
    maxnumber = premax[0]

    for element in range(1,len(premax)):
        if premax[element] > maxnumber:
            maxnumber = premax[element]

    return maxnumber

print(f"Número mayor: {maxMatriz([[20154,1,500,6],[457.25,105,12,6],[2,-485.52,32001,6],[7,92,5,96],[23,8,5,1001]])}")

