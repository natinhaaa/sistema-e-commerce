from classes2 import *
import os

def Main():
    loja = Loja("E-Shop", "Avenida 9 de Julho", "35.463.434/0001-02")
    admin = Admin("Administrador Loja", 1234)

    contID = 0

    sair = False
    while sair == False:
        try: #oi
            os.system("cls")
            print(f"Bem-vindo à {loja.getNomeLoja()}. Você pode nos visitar no endereço {loja.getEndereçoLoja()}, estamos abertos 24h.\nCNPJ: {loja.getCNPJ()}")
            print("Qual função deseja realizar?\n")
            print("[1] CLIENTE\n[2] ADMIN\n[3] SAIR")
            menu = int(input("➩  "))
            os.system("cls")
            match menu:
                case 1:
                    os.system("cls")
                    print("CLIENTE")
                    nome = input("Nome de usuário\n➩  ")
                    senha = int(input("Senha\n➩  "))

    #################################################################################################################################################################

                    match admin.login_cliente(nome, senha):
                        case True:
                            sair2 = False
                            while sair2 == False:
                                os.system("cls")
                                print("Escolha alguma das opções abaixo.\n")
                                print("[1] Listar produtos\n[2] Adicionar produtos ao carrinho\n[3] Visualizar carrinho\n[4] Excluir produtos do carrinho\n[5] Total Carrinho\n[6] Prosseguir para a compra\n[7] Voltar")
                                função = int(input("➩  "))
                                match função:
                                    case 1:
                                        os.system("cls")
                                        print("Lista de produtos da Loja")
                                        admin.listar_produtos()
                                        os.system("pause")
                                        os.system("cls")

                                    case 2:
                                        print("Adicionar produtos ao Carrinho")
                                        admin.listar_produtos()
                                        print("\nQual o ID do item você deseja adicionar ao carrinho?")
                                        id_produto = int(input("➩  "))
                                        admin.adicionar_produto_carrinho(admin.getIDproduto(id_produto), nome)
                                        os.system("pause")
                                        os.system("cls")
                                
                                    case 3:
                                        print("Visualizar o carrinho\n")
                                        print("Esses são os produtos dentro do seu carrinho:\n")
                                        admin.listar_carrinho(nome)
                                        os.system("pause")                                        
                                        os.system("cls")
                                
                                    case 4:
                                        os.system("cls")
                                        print("Excluir produtos do carrinho")
                                        admin.listar_carrinho(nome)
                                        print("\nQual o índice do item que você deseja excluir do carrinho?")
                                        id_produto = int(input("➩  "))
                                        admin.excluir_produto_carrinho(nome, id_produto)
                                        os.system("pause")
                                        os.system("cls")
                                
                                    case 5:
                                        os.system("cls")
                                        print("Total da Compra\n")
                                        admin.calcular_total(nome)
                                        os.system("pause")
                                        os.system("cls")
                                
                                    case 6:
                                        os.system("cls")
                                        print("Finalizar Compra\n")

                                        if admin.finalizar_compra(nome) == False:
                                            sair2 = True
                                            sair = True
                                            return sair2 and sair
                                        
                                        else:
                                            break
                                    
                                    case 7:
                                        sair2 = True
                                    
                                    case _:
                                        print("Opção inválida.")
                                        os.system("pause")

##########################################################################################################################
                        
                case 2:
                    print("ADMIN")
                    print("Para acessar essa área é necessário a senha de administrador.")
                    senhaAdm = int(input("➩  "))

                    if senhaAdm == 1234:
                        print("Acessado com sucesso!")
                        os.system("pause")
                        os.system("cls")

                        sair3 = False
                        while sair3 == False:
                            
                            print("[1] Cadastrar Cliente\n[2] Cadastrar Admin\n[3] Cadastrar Produtos\n[4] Excluir Produtos\n[5] Excluir Clientes\n[6] Listar Clientes\n[7] Listar Produtos\n[8] Voltar")
                            função2 = int(input("➩  "))

                            match função2:
                                case 1:
                                    cliente = Clientes (nomeCad = input("Nome de usuário\n➩  "), senhaCad = int(input("Senha\n➩  ")), datnascCad = input("Data de Nascimento (formato: dd/mm/AAAA)\n➩  "), cpfCad = int(input("CPF\n➩  ")), endereçoCad = input("Endereço\n➩  "), id = 0)
                                    print("Cadastrar Clientes")
                                    contID += 1
                                    id = contID
                                    admin.cadastro_cliente(cliente, id)
                                    os.system("pause")
                                
                                case 2:
                                    print("Cadastrar Administrador")
                                    admin.cadastro_admin(nome = input("Nome de usuário\n➩  "), senha = int(input("Senha\n➩  ")))
                                    os.system("pause")

                                case 3:
                                    print("Cadastrar produtos")
                                    produto = Produtos (nome = input("Digite o nome do produto: "), desc = input("Digite a descrição do produto: "), preço = input("Digite"))
                                    admin.cadastrar_produtos(produto)
                                    os.system("pause")

                                case 4:
                                    os.system("cls")
                                    print("Excluir produtos")
                                    admin.listar_produtos()
                                    id_produto = int(input("Digite p-o ID do produto que deseja excluir\n➩  "))
                                    admin.excluir_produto_loja(id_produto)
                                    os.system("pause")
                                    os.system("cls")
                                
                                case 5:
                                    os.system("cls")
                                    print("Excluir Clientes")
                                    os.system("pause")
                                    os.system("cls")
                                
                                case 6:
                                    os.system("cls")
                                    print("Listar Clientes")
                                    os.system("pause")
                                    os.system("cls")
                                
                                case 7:
                                    os.system("cls")
                                    print("Listar Produtos")
                                    os.system("pause")
                                    os.system("cls")
                                
                                case 8:
                                    sair3 = True
                                    
                                case _:
                                    print("Opção inválida")
                                    os.system("pause")
                    else:
                        print("Senha incorreta.")

                case 3:
                    sair = True

                case _:
                    print("Valor inválido.")
         
        except Exception as erro:
            print("Ops, algo deu errado. Tente novamente.")
            print(erro.__class__.__name__)