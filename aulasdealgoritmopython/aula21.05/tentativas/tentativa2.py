placa = str(input("digite a placa "))
caractere = [char for char in placa]
for i in len(placa):
    if caractere[i] == i:
        print("placa numerica")