import json
import xmlrpc.client
s = xmlrpc.client.ServerProxy('http://localhost:8080',allow_none=True)
def mostrar():
    my_list = s.show()
    if len(my_list) == 0:
        print ("Banco de dados Vazio")
    else:
        for x in range(len(my_list)):
            print (my_list[x])
def adicionar(x,y,z):
    return s.add(x,y,z)
def procurar(y):
    my_list = s.get(y)
    if len(my_list) == 0:
        print ("Nome não consta no banco de dados!")
    else:
        for x in range(len(my_list)):
            print (my_list[x])
def deletar(y):
    return s.delete(y)

while True:
    opt = 1
    print("Bem vindo ao menu do banco de dados!")
    print("Se você está aqui significa que a conexao foi feita com sucesso!")
    while opt == 1:
        print("-----MENU-----")
        print("1 - Mostrar 2 - Adcionar 3 - Procurar 4 - Deletar 0 - Sair")
        opcao = input("Digite aqui: ")
        if opcao == "1":
            print("Mostrando o Banco de dados")
            mostrar()
            input("Pressione a tecla Enter para continuar")
        if opcao == "2":
            print ("Adicionando um registro")
            nome = input("Digite o nome: ")
            curso = input("Digite o Curso: ")
            ano = input("Digite o Periodo: ")
            adicionar(nome,curso,ano)
            input("Pressione a tecla Enter para continuar")
        if opcao == "3":
            print("Procurando um registro pelo Nome")
            nome = input("Digite o nome a ser procurado: ")
            procurar(nome)
            input("Pressione a tecla Enter para continuar")
        if opcao == "4":
            print("Deletando um aluno pelo Nome")
            nome = input("Digite o nome a ser procurado: ")
            deletar(nome)
            input("Pressione a tecla Enter para continuar")
        if opcao == "0":
            break
    break
