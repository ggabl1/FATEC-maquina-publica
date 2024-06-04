n1 = int(input("insira numero 1: "))
n2 = int(input("insira numero 2: "))
n3 = int(input("insira numero 3: "))

maiornum = 0
menornum = 0
if 0 > n1 or 0 > n2 or 0 > n3:
    print("numero invalido")
    
if n1 > n2 and n1 > n3:
    maiornum = n1

if n2 > n1 and n2 > n3:
    maiornum = n2
    
if n3 > n2 and n3 > n1:
    maiornum = n3
    
    
if n1 < n2 and n1 < n3:
    menornum = n1

if n2 < n1 and n2 < n3:
    menornum = n2
    
if n3 < n2 and n3 < n1:
    menornum = n3
    
media = (n1 + n2 + n3)/3

print("o maior numero é ", maiornum, "o menor é ", menornum, "e a media é ", media)

