agenda = []

def cadastrar_contato():
    pessoa = []
    nome = input("Digite o nome da pessoa: ")
    telefone = input("Digite o telefone da pessoa: ")
    email = input("Digite o e-mail da pessoa: ")
    pessoa.append(nome)
    pessoa.append(telefone)
    pessoa.append(email)
    agenda.append(pessoa)
def listar_todos_contatos():
    print("Lista de contatos:")
    for i, contato in enumerate(agenda, 1):
        print(f"Nome: {contato[0]}, Telefone: {contato[1]}, E-mail: {contato[2]}")
def consultar_contato_por_nome():
    nome_procurado = input("Digite o nome da pessoa que deseja buscar: ")
    for contato in agenda:
        if contato[0].lower() == nome_procurado.lower():
            print("achei")
            print("Nome:", contato[0])
            print("Telefone:", contato[1])
            print("E-mail:", contato[2])
                       
cadastrar_contato()
listar_todos_contatos()
consultar_contato_por_nome()