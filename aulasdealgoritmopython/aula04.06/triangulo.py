import math
while True:
    c1 = float(input("informe cateto oposto: "))
    c2 = float(input("informe cateto adjacente: "))
    if c1 == 0 and c2 == 0:
        break
    H = math.sqrt(c1 * c1 + c2 * c2)
    print("a hipotenusa é", H)