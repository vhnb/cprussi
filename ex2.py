ladoA = float(input ("Digite o valor do primeiro lado do triângulo: "))
ladoB = float(input ("Digite o valor do segundo lado do triângulo: "))
ladoC = float(input ("Digite o valor do terceiro lado do triângulo: "))
 
lados = sorted([ladoA, ladoB, ladoC], reverse=True)
ladoA = lados[0]
ladoB = lados[1]
ladoC = lados[2]
 
def triangEqu (ladoA, ladoB, ladoC):
    return ladoA == ladoB == ladoC
 
def triangIso (ladoA, ladoB, ladoC):
    return ladoA == ladoB or ladoB == ladoC or ladoC == ladoA
 
def triangRet (ladoA, ladoB, ladoC):
    return ladoA ** 2 == ladoB ** 2 + ladoC ** 2
 
def triangObt (ladoA, ladoB, ladoC):
    return ladoA ** 2 > ladoB ** 2 + ladoC ** 2
 
if ladoA >= ladoB + ladoC:
    print("NAO FORMA TRIANGULO")
 
elif triangEqu(ladoA, ladoB, ladoC):   # 1º — mais específico
    print("TRIANGULO EQUILATERO")
 
elif triangIso(ladoA, ladoB, ladoC):   # 2º — ainda específico
    print("TRIANGULO ISOSCELES")
 
elif triangRet(ladoA, ladoB, ladoC):   # 3º — ângulo
    print("TRIANGULO RETANGULO")
 
elif triangObt(ladoA, ladoB, ladoC):   # 4º — ângulo
    print("TRIANGULO OBTUSANGULO")
 
else:
    print("TRIANGULO ACUTANGULO")      # 5º — único restante
