def SonAmigos(x, y):
    
    divisoresx = []

    for i in range(1,x+1):
        if x % i == 0:
            divisoresx.append(i)

    divisoresy = []

    for i in range(1,y+1):
        if y % i == 0:
            divisoresy.append(i)

    if sum(divisoresx) == sum(divisoresy):
        return True
    else:
        return False

print(SonAmigos(1184, 1210))