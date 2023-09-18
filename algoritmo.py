from classes import *
import os
#login usuario, cadastrar produtos, listar produtos, excluir produtos, comprar produtos, visualizar carrinho
def Main():
    cliente = Clientes_Loja()
    admin = Admin()

    contID = 0

    sair = False
    while sair == False:
        try:
            os.system("cls")
            print("LOJA DE ELETRÔNICOS")
            print("Qual função deseja realizar?")
            print("[1] LOGIN\n[2] CADASTRAR\n[3] LOJA\n[4] SAIR")
            menu = int(input("-> "))

            match menu:
                case 1:
                    os.system("cls")
                    print("LOGIN")
                    nome = input("Nome\n-> ")
                    senha = int(input("Senha\n-> "))
                    os.system("pause")

#############################################################################################################

                    match cliente.login(nome,senha):
                        case True:
                            sair2 = False
                            while sair2 == False:
                                print("[1] Listar produtos\n[2] Adicionar produtos ao carrinho\n[3] Visualizar carrinho\n[4] Excluir produtos do carrinho\n[5] Voltar")
                                função = int(input("-> "))
                                match função:
                                    case 1:
                                        os.system("cls")
                                        print("Lista de produtos da loja")
                                        admin.listar_produtos()
                                        os.system("pause")
                                    
                                    case 2:
                                        print("Adicionar produtos ao carrinho")
                                        admin.listar_produtos()
                                        print("\nQual o ID do item você deseja adicionar ao carrinho?")
                                        produto_add = int(input("> "))
                                        cliente.adicionar_produto_carrinho(produto_add)
                                        os.system("pause")
                                    
                                    case 3:
                                        print("Visualizar o carrinho")
                                        print("ESSES SÃO OS PRODUTOS DENTRO DO SEU CARRINHO:")
                                        cliente.listar_carrinho()
                                        os.system("pause")
                                        
                                    
                                    case 4:
                                        os.system("cls")
                                        print("Excluir produtos do carrinho")
                                        cliente.visualizar_carrinho()
                                        print("\nQual o ID do item você deseja excluir do carrinho?")
                                        produto_excluir = int(input("-> "))
                                        cliente.excluir_produto(produto_excluir)
                                        os.system("pause")
                                    
                                    case 5:
                                        sair2 = True
                                    
                                    case _:
                                        print("Opção inválida.")
                                        os.system("pause")

                        
                        case False:
                            os.system("pause")
                            os.system("cls")


########################################################################################################

                case 2:
                    print("Cadastrar")
                    nomeCad = input("Nome\n-> ")
                    senhaCad = int(input("Senha\n-> "))
                    cliente.cadastro(nomeCad, senhaCad)
                    os.system("pause")

                case 3:
                    print("Para acessar essa área é necessário a senha de administrador.")
                    senhaAdm = int(input("-> "))

                    if senhaAdm == 999:
                        print("Acessado com sucesso!")
                        os.system("pause")
                        print("Área da loja")
                        print("[1] Cadastrar\n[2] Excluir produtos")
                        loja = int(input("-> "))

                        match loja:
                            case 1:
                                os.system("cls")
                                print("Cadastrar produtos")
                                contID += 1
                                id = contID
                                nome = input("Nome do produto: ")
                                desc = input("Descrição do produto: ")
                                preço = int(input("Valor do produto: R$ "))
                                admin.cadastrar_produtos(nome, desc, preço, id)
                                os.system("pause")
                            
                            case 2:
                                os.system("cls")
                                print("Excluir produtos")
                                admin.listar_produtos()
                                produto_excluir = int(input("Digite o ID do produto que deseja excluir: "))
                                admin.excluir(produto_excluir)
                                os.system("pause")
                            
                            case _:
                                print("Opção inválida.")
                                os.system("pause")

                    else:
                        print("Senha incorreta.")
                        os.system("pause")
                
##############################################################################################################

                case 4:
                    sair = True

                case _:
                    print("Opção inválida.")
                
        except Exception as erro:
            print("Ops, algo deu errado. Tente novamente.")
            print(erro.__class__.__name__)