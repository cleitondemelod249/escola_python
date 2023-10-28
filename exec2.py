def isPar(numero):
    if(numero % 2 == 0):
        return True
    else:
        return False
    
def isPositivo(numero):
    if(numero > 0):
        return True
    else:
        return False

numero = int(input("Digite um numero qualquer diferente: "))
if(isPar(numero) and isPositivo(numero)):
    print("O numero é par, e positivo")
elif(not isPar(numero) and isPositivo(numero)):
    print("O numero é Positivo, mas nao par")
elif(not isPositivo(numero) and isPar(numero)):
    print("O numero é par, mas nao e positivo")
else:
    print("o numero nao é par, nem positivo")