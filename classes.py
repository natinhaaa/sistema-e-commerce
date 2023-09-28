class Loja:
    def __init__(self, nome, cnpj, endereço):
        self.nome = nome
        self.cnpj = cnpj
        self.endereço = endereço

    def getNomeLoja(self):
        return self.nome
    
    def getCNPJ(self):
        return self.cnpj
    
    def getEndereçoLoja(self):
        return self.endereço

#Criamos a seguinte classe apenas para definirmos os atributos que um Produto deve ter neste sistema
class Produtos:
    def __init__(self, nome, desc, preço):
        self.nome = nome
        self.desc = desc
        self.preço = preço
    
#Os seguintes gets, servem para retornar o valor atual de cada atributo do objeto Produto, que é único para cada produto criado
    def getNome(self):
        return self.nome

    def getDesc(self):
        return self.desc

    def getPreço(self):
        return self.preço
    
#############################################################################################

#Criamos a seguinte classe apenas para definirmos os atributos que um Cliente deve ter nesse sistema
class Clientes:
    def __init__(self, nome, senha, datanasc, cpf, endereço, id):
        self.nome = nome
        self.senha = senha
        self.datanasc = datanasc
        self.cpf = cpf
        self.endereço = endereço
        self.id = id
        self.carrinho = []
	
    def getNome(self):
        return self.nome
    
    def getSenha(self):
        return self.senha
    
    def getDataNasc(self):
        return self.datanasc
    
    def getCPF(self):
        return self.cpf
    
    def getEndereço(self):
        return self.endereço
    
    def getID(self):
        return self.id
    
		#Vai retornar o valor que se encontra dentro do carrinho, que é único para cada Cliente
    def getCarrinho_Compras(self):
        return self.carrinho

#########################################################################################

#Nesta classe, encontra-se os métodos que o sistema tem a oferecer ao Cliente
class Admin:
    def __init__(self, usuário, senha):
        self.usuário = usuário
        self.senha = senha
        self.clientes = {}
        self.produtos = []
        self.admins = {}
        self.relatorios = {}
    
    def getUsuário(self):
        return self.usuário
    
    def getSenha(self):
        return self.senha
    
    def cadastrar_produtos(self, nome, desc, preço):
        produto_cadastrado = Produtos(nome, desc, preço)
        self.produtos.append(produto_cadastrado)
        print("Produto adicionado!")

    def listar_produtos(self):
        print("Produtos Disponíveis")
        contID = 0
        for produto in self.produtos:
            contID += 1
            print(f"ID - {contID}\nNome: {produto.getNome()}\nDescrição: {produto.getDesc()}\nPreço: R${produto.getPreço()}\n")
    
    def excluir_produto_loja(self, id_produto):
        self.produtos.pop(id_produto - 1)
    
    def cadastro_cliente(self, nome, senha, datanasc, cpf, endereço, id):
        cliente = Clientes(nome, senha, datanasc, cpf, endereço, id)
        if nome not in self.clientes:
            self.clientes[nome] = cliente
            print("Você foi cadastrado!")

        else:
            print("Nome de usuário já existe.")
    
    def cadastro_admin(self, usuário, senha):
        admin = Admin(usuário, senha)
        if usuário not in self.admins:
            self.admins[usuário] = admin
            print("Você foi cadastrado como admin!")
        
        else:
            print("Nome de usuário já existe.")
    
    def login_cliente(self, nome, senha):
        for chave, valor in self.clientes.items():
            if chave == nome and valor.senha == senha:
                print("Login bem sucedido.")
                return True
            
        else:
            print("Nome de usuário ou senha incorretos.")
            return False
    
    def login_admin(self, usuário, senha):
        for chave, valor in self.admins.items():
            if chave == usuário and valor.senha == senha:
                print("Login bem sucedido.")
                return True
                     
            else:
                print("Nome de usuário ou senha incorretos.")
                return False
    
    def listar_clientes(self):
        for cliente in self.clientes.values():
            print(f"ID - {cliente.getID()}\nNome: {cliente.getNome()}\nSenha: {cliente.getSenha()}\nData de Nascimento: {cliente.getDataNasc()}\nCPF: {cliente.getCPF()}\nEndereço: {cliente.getEndereço()}")

    def listar_admins(self):
        contID = 0
        for admin in self.admins.values():
            contID += 1
            print(f"ID - {contID}\nNome de usuário: {admin.getUsuário()}\nSenha: {admin.getSenha()}\n")

    def excluir_clientes(self, clienteex):
        if clienteex in self.clientes.keys():
            del self.clientes[clienteex]
            print("Cliente excluído.")
        
        else:
            print("O cliente não existe.")
    
    def excluir_admin(self, adminex):
        if adminex in self.admins.keys():
            del self.admins[adminex]
            print("Admin excluído.")
        
        else:
            print("O admin não existe.")

    def getIDproduto(self, id_produto):
        return self.produtos[id_produto - 1]

#Nestas últimas funções, temos o atributo "nome", que precisa ser passado para podermos confirmar que o produto adicionado no Carrinho de Compras seja o carrinho único de um cliente que o nome seja tal que está dentro da lista de clientes da Loja
    
    def adicionar_produto_carrinho(self, produto_cadastrado, nome):
        self.clientes[nome].getCarrinho_Compras().append(produto_cadastrado)
        print("O item foi adicionado ao carrinho!")

    def listar_carrinho(self, nome):
        contID = 0
        for produto in self.clientes[nome].getCarrinho_Compras():
            contID += 1
            print(f"{contID}.\nNome: {produto.getNome()}\nDescrição: {produto.getDesc()}\nPreço: R${produto.getPreço()}\n")
    
    def excluir_produto_carrinho(self, nome, id_produto):
        self.clientes[nome].getCarrinho_Compras().pop(id_produto - 1)
        print("Produto excluído.")
    
    def calcular_total(self, nome):
        total_produtos = 0
        contID = 0
        for produto in self.clientes[nome].getCarrinho_Compras():
            contID += 1
            print(f"ID - {contID}\nNome: {produto.getNome()}\nDescrição: {produto.getDesc()}\nPreço: R${produto.getPreço()}\n")
            total_produtos += produto.getPreço()
        print(f"TOTAL: {total_produtos}")
    
    def finalizar_compra(self, nome):
        total_produtos = 0
        for produto in self.clientes[nome].getCarrinho_Compras():
            total_produtos += produto.getPreço()
        print(f"Total da compra: {total_produtos}")

        confirm = input("Deseja confirmar a compra? Y/N\n➩  ").upper()

        if confirm == "Y":
            carrinho_cliente = self.clientes[nome].getCarrinho_Compras()
            relatorio_cliente = []
            for produto_comprado in carrinho_cliente:
                produtoinfo = (f"Produto Comprado: {produto_comprado.getNome()}, Preço: {produto_comprado.getPreço()}")
                relatorio_cliente.append(produtoinfo)
            self.relatorios[f"Cliente: {self.clientes[nome].getNome()}"] = relatorio_cliente
                
            print("Compra finalizada!")
            return False

        else:
            return True

    def historico_compras(self):
        print("Compras realizadas dentro da E-Shop:")
        print(self.relatorios)
    
    def vendas_loja(self):
        print("Vendas realizadas:")
        for produto in self.relatorios.values():
            print(produto)
    