totalReprovados = 0
totalAprovados = 0
while True:
    estado = str(input("digite o estado da peça (r ou a) "))
    if estado == "r":
        totalReprovados = totalReprovados+1
        
    elif estado == "a":
        totalAprovados = totalAprovados+1
        
    continua = str(input("deseja continuar? "))
    if continua == "nao":
       print(totalReprovados, "reprovados e ", totalAprovados, "aprovados ")