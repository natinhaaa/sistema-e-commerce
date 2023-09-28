from classes import *
import os
import random
import string

def gerar_numero_aleatorio(length):
    caracteres = string.ascii_uppercase + string.digits
    return "".join(random.choice(caracteres) for _ in range(length))

def gerar_numero_pedido():
    numero_pedido = f"#{gerar_numero_aleatorio(2)}{gerar_numero_aleatorio(2)}{gerar_numero_aleatorio(2)}{gerar_numero_aleatorio(2)}{gerar_numero_aleatorio(3)}"
    return numero_pedido

def Main():
    admin = Admin("admin", 1234)

    contID = 0

    sair = False
    while sair == False:

        loja = Loja("E-Shop", "35.463.434/0001-02", "Avenida 9 de Julho")
        
        try:
            os.system("cls")
            print(f"Bem-vindo à {loja.getNomeLoja()}. Você pode nos visitar no endereço {loja.getEndereçoLoja()}, aberto 24h.\nCNPJ: {loja.getCNPJ()}")
            print("Qual função deseja realizar?\n")
            print("[1] Login Cliente\n[2] Login Admin\n[3] Sair")
            menu = int(input("➩  "))
            os.system("cls")

            match menu:
                case 1:
                    os.system("cls")
                    print("LOGIN CLIENTE")
                    nome = input("Nome\n➩  ")
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
                                        admin.finalizar_compra(nome)
                                        print(gerar_numero_pedido())
                                        os.system("pause")
                                        sair2 = True
                                    
                                    case 7:
                                        sair2 = True
                                    
                                    case _:
                                        print("Opção inválida.")
                                        os.system("pause")

                        
                        case False:
                            os.system("pause")
                            os.system("cls")


#############################################################################################################################################################

                case 2:
                    os.system("cls")
                    print("LOGIN ADMIN")
                    usuário = input("Usuário\n➩  ")
                    senha = int(input("Senha\n➩  "))

                    match admin.login_admin(usuário, senha) or usuário == "admin" and senha == 1234: 
                        case True:
                            sair3 = False
                            while sair3 == False:
                                os.system("cls")
                                print("ÁREA ADMIN")
                                print("Escolha alguma das opções abaixo.\n")
                                print("[1] Cadastrar Clientes\n[2] Cadastrar Admins\n[3] Cadastrar Produtos\n[4] Listar Clientes\n[5] Listar Admins\n[6] Listar Produtos\n[7] Excluir Clientes\n[8] Excluir Admins\n[9] Excluir Produtos\n[10]Relatório\n[0] Voltar")
                                loja = int(input("➩  "))

                                match loja:
                                    case 1:
                                        print("Cadastrar Clientes")
                                        nomeCad = input("Nome de usuário\n➩  ")
                                        datanasc = input("Data de Nascimento (formato: dd/mm/AAAA)\n➩  ")
                                        cpf = int(input("CPF\n➩  "))
                                        endereço = input("Endereço\n➩  ")
                                        senhaCad = int(input("Senha\n➩  "))
                                        contID += 1
                                        id = contID
                                        admin.cadastro_cliente(nomeCad, senhaCad, datanasc, cpf, endereço, id)
                                        os.system("pause")
                                        break
                                    
                                    case 2:
                                        os.system("cls")
                                        print("Cadastrar Admins")
                                        usuário = input("Nome de usuário\n➩  ")
                                        senha = int(input("Senha\n➩  "))
                                        admin.cadastro_admin(usuário, senha)
                                        os.system("pause")
                                        os.system("cls")
                                        break

                                    case 3:
                                        os.system("cls")
                                        print("Cadastrar produtos")
                                        nomeprod = input("Nome do produto\n➩  ")
                                        descprod = input("Descrição do produto\n➩  ")
                                        preçoprod = float(input("Valor do produto\n➩  R$ "))
                                        admin.cadastrar_produtos(nomeprod, descprod, preçoprod)
                                        os.system("pause")
                                        os.system("cls")
                                        break

                                    case 4:
                                        os.system("cls")
                                        print("Listar Clientes")
                                        admin.listar_clientes()
                                        os.system("pause")
                                        os.system("cls")
                                        break

                                    case 5:
                                        os.system("cls")
                                        print("Listar Admins")
                                        admin.listar_clientes()
                                        os.system("pause")
                                        os.system("cls")
                                        break
                                    
                                    case 6:
                                        os.system("cls")
                                        print("Listar Produtos")
                                        admin.listar_clientes()
                                        os.system("pause")
                                        os.system("cls")
                                        break

                                    case 7:
                                        os.system("cls")
                                        print("Excluir Clientes")
                                        id_clienteex = int(input("Insira o ID do cliente que deseja excluir: "))
                                        admin.excluir_clientes(id_clienteex)
                                        os.system("pause")
                                        os.system("cls")
                                        break
                                    
                                    case 8:
                                        os.system("cls")
                                        print("Excluir Admins")
                                        us_adminex = int(input("Insira o nome de usuário do admin que deseja excluir: "))
                                        os.system("pause")
                                        os.system("cls")
                                        break

                                    case 9:
                                        os.system("cls")
                                        print("Excluir produtos")
                                        admin.listar_produtos()
                                        id_produto = int(input("Digite o ID do produto que deseja excluir\n➩  "))
                                        admin.excluir_produto_loja(id_produto)
                                        os.system("pause")
                                        os.system("cls")
                                        break
                                    
                                    case 10:
                                        os.system('cls')
                                        print("Que relatório você gostaria de ver?")
                                        print("[1] Histórico de compras\n[2] Histórico de vendas\n")
                                        ver=int(input("➩  "))
                                        if ver == 1:
                                            relatorio = Relatório()
                                            relatorio.historico_compras()
                                        elif ver == 2:
                                            relatorio = Relatório()
                                            relatorio.vendas_loja()
                                        else:
                                            print("Opção inválida.")
                                        break
                                            
                                    case 0:
                                        sair3 = True
                                        break
                                                                            
                                    case _:
                                        print("Opção inválida.")
                                        os.system("pause")
                                        break

                        case False:
                            os.system("pause")
                            os.system("cls")
                            break
                            
                
#############################################################################################################################################################

                case 3:
                    sair = True
                    break
                case _:
                    print("Opção inválida.")
                    break
                
        except Exception as erro:
            print("Ops, algo deu errado. Tente novamente.")
            print(erro.__class__.__name__)
            break