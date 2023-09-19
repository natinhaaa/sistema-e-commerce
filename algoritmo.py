from classes import *
import os

def Main():
    admin = Sistema()
    sair = False
    while sair == False:
        try:
            os.system("cls")
            print("LOJA DE ELETRÔNICOS")
            print("Qual função deseja realizar?\n")
            print("[1] Login\n[2] Cadastrar\n[3] Loja\n[4] Sair")
            menu = int(input("➩  "))
            os.system("cls")

            match menu:
                case 1:
                    os.system("cls")
                    print("LOGIN")
                    nome = input("Nome\n➩  ")
                    senha = int(input("Senha\n➩  "))

#################################################################################################################################################################

                    match admin.login(nome, senha):
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
                                        os.system("pause")
                                        sair2 = True
                                        sair = True
                                        return sair2 and sair
                                    
                                    case 7:
                                        sair2 = True
                                    
                                    case _:
                                        print("Opção inválida.")
                                        os.system("pause")

                        
                        case False:
                            os.system("pause")
                            os.system("cls")


##############################################################################################################################################################

                case 2:
                    print("Cadastre-se")
                    nomeCad = input("Nome de usuário\n➩  ")
                    senhaCad = int(input("Senha\n➩  "))
                    admin.cadastro_cliente(nomeCad, senhaCad)
                    os.system("pause")

#############################################################################################################################################################

                case 3:
                    print("Para acessar essa área é necessário a senha de administrador.")
                    senhaAdm = int(input("➩  "))

                    if senhaAdm == 1234:
                        print("Acessado com sucesso!")
                        os.system("pause")
                        os.system("cls")
                        sair3 = False
                        while sair3 == False:
                            print("Área da loja")
                            print("[1] Cadastrar produtos\n[2] Excluir produtos\n[3] Voltar")
                            loja = int(input("➩  "))

                            match loja:
                                case 1:
                                    os.system("cls")
                                    print("Cadastrar produtos")
                                    nomeprod = input("Nome do produto\n➩  ")
                                    descprod = input("Descrição do produto\n➩  ")
                                    preçoprod = float(input("Valor do produto\n➩  R$ "))
                                    admin.cadastrar_produtos(nomeprod, descprod, preçoprod)
                                    os.system("pause")
                                    os.system("cls")
                                
                                case 2:
                                    os.system("cls")
                                    print("Excluir produtos")
                                    admin.listar_produtos()
                                    id_produto = int(input("Digite o ID do produto que deseja excluir\n➩  "))
                                    admin.excluir_produto_loja(id_produto)
                                    os.system("pause")
                                    os.system("cls")

                                case 3:
                                    sair3 = True
                                
                                case _:
                                    print("Opção inválida.")
                                    os.system("pause")

                    else:
                        print("Senha incorreta.")
                        os.system("pause")
                
#############################################################################################################################################################

                case 4:
                    sair = True

                case _:
                    print("Opção inválida.")
                
        except Exception as erro:
            print("Ops, algo deu errado. Tente novamente.")
            print(erro.__class__.__name__)