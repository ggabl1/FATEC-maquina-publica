pesquisa = []
def avaliar ():
    for i in range(2):
        pessoa = []
        sexo = str(input("digite o sexo"))
        avaliacao = str(input("o produto atendeu suas necessidades com qualidade?"))
        pessoa.append(sexo)
        pessoa.append(avaliacao)
    print("pesquisa:")             
    for i in pesquisa(0,5):
        return pesquisa[i]
        
avaliar()