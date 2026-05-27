#Mensagem inicial do programa
s1 = ("Bem-vindo(a) ao sistema de contatos comerciais, Isabelle Silva!")
print(s1)

#Lista que vai guardar os contatos
lista_contatos = []
#Coloque aqui o seu RU
id_global = 5000000

#Função para cadastrar um contato
def cadastrar_contato(id):
    print("\n--- Cadastro de Contato ---")
    nome = input("Nome: ")
    atividade = input("Atividade: ")
    telefone = input("Telefone: ")
    contato = {
        "id": id,
        "nome": nome,
        "atividade": atividade,
        "telefone": telefone
    }
    
    #Adicionar contato na lista
    lista_contatos.append(contato.copy())
    print("Contato cadastrado!\n")


#Aqui é as função para consultar os contatos
def consultar_contatos():
    while True:
        print("\n--- Consultar Contatos ---")
        print("1 - Ver todos")
        print("2 - Buscar por id")
        print("3 - Buscar por atividade")
        print("4 - Voltar")
        
        opcao = input("Escolha: ")
        if opcao == "1":
            for c in lista_contatos:
              print(c) 
        elif opcao == "2":
            try:
                busca = int(input("Digite o id: "))
                for c in lista_contatos:
                    if c["id"] == busca:
                      print(c)     
            except:
              print("Id inválido")
        elif opcao == "3":
            atividade = input("Digite a atividade: ")
            
            for c in lista_contatos:
                if c["atividade"] == atividade:
                  print(c)
        elif opcao == "4":
          return
        else:
          print("Opção inválida")

#Função para remover um contato da lista
def remover_contato():
    while True:
        try:
            busca = int(input("Digite o id para remover: "))
            
            for c in lista_contatos:
                if c["id"] == busca:
                  lista_contatos.remove(c)
                  print("Removido com sucesso!")
                  return
            
            print("Id não encontrado")
        
        except:
            print("Digite um número válido")

#Menu principal
while True:
    print("--- MENU ---")
    print("1 - Cadastrar")
    print("2 - Consultar")
    print("3 - Remover")
    print("4 - Sair")

    opcao = input("Escolha: ")
    if opcao == "1":
      cadastrar_contato(id_global)
      id_global += 1
    elif opcao == "2":
      consultar_contatos()
    elif opcao == "3":
      remover_contato()
    elif opcao == "4":
      print("Saindo...")
      break
    else:
      print("Opção inválida")
