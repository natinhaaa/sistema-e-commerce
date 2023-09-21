class Loja:
    def __init__(self, nomeLoja, endereçoLoja, cnpj):
        self.nomeLoja = nomeLoja
        self.endereçoLoja = endereçoLoja
        self.cnpj = cnpj
        self.produtos = []
        self.admins = {}
        self.clientes = {}

    def getNomeLoja(self):
        return self.nomeLoja
    
    def getEndereçoLoja(self):
        return self.endereçoLoja
    
    def getCNPJ(self):
        return self.cnpj
    
    def InformaçõesCliente(self, nome, senha, datnasc, cpf, endereço, id):
        cliente = Clientes(nome, senha, datnasc, cpf, endereço, id)
        if id not in self.clientes:
            self.clientes[id] = cliente
            print("Você foi cadastrado.")
        
        else:
            print("O usuário já está cadastrado")
    
    def InformaçõesAdmin(self, usuário, senha):
        admin = Admin(usuário, senha)
        if usuário not in self.admins:
            self.clientes[usuário] = admin
            print("Você foi cadastrado como administrador.")
        
        else:
            print("O administrador já está cadastrado")
    
#Criamos a seguinte classe apenas para definirmos os atributos que um Cliente deve ter nesse sistema
class Clientes(Loja):
    def __init__(self, nome, senha, datnasc, cpf, endereço, id):
        self.nome = nome
        self.datnasc = datnasc
        self.cpf = cpf
        self.endereço = endereço
        self.senha = senha
        self.id = id

        self.carrinho = []

    def getNome(self):
        return self.nome

    def getDatNasc(self):
        return self.datnasc
    
    def getCPF(self):
        return self.cpf
    
    def getEndereço(self):
        return self.endereço
    
    def getSenha(self):
        return self.senha
    
	#Vai retornar o valor que se encontra dentro do carrinho, que é único para cada Cliente
    def getCarrinho_Compras(self):
        return self.carrinho

#######################################################################################################

#Criamos a seguinte classe apenas para definirmos os atributos que um Produto deve ter neste sistema
class Produtos(Loja):
    def __init__(self, nomeProd, desc, preço):
        self.nomeProd = nomeProd
        self.desc = desc
        self.preço = preço
    
#Os seguintes gets, servem para retornar o valor atual de cada atributo do objeto Produto, que é único para cada produto criado
    def getNomeProd(self):
        return self.nomeProd

    def getDesc(self):
        return self.desc

    def getPreço(self):
        return self.preço

#####################################################################################################

class Admin(Clientes, Produtos, Loja):
    def __init__(self, usuário, senhaAdm):
        self.__usuário = usuário
        self.__senhaAdm = senhaAdm

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
    
    def cadastro_cliente(self, nome, senha, datnasc, cpf, endereço, id):
        loja.InformaçõesCliente(nome, senha, datnasc, cpf, endereço, id)
    
    def cadastro_admin(self, usuário, senha):
        loja.InformaçõesAdmin(usuário, senha)

    def login_cliente(self, nome, senha):
        for chave, valor in self.clientes:
            if chave.nome in self.clientes and valor.senha in self.clientes:
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
        print(f"TOTAL: R$ {total_produtos}")
    
    def finalizar_compra(self, nome):
        total_produtos = 0
        for produto in self.clientes[nome].getCarrinho_Compras():
            total_produtos += produto.getPreço()
        print(f"Total da compra: R$ {total_produtos}")

        confirm = input("Deseja confirmar a compra? Y/N\n➩  ").upper()

        if confirm == "Y":
            print("Compra finalizada!")
            return False

        else:
            return True

loja = Loja("E-Shop", "Avenida 9 de Julho", "35.463.434/0001-02")
###################################################################################################

class Relatórios(Clientes, Produtos, Loja ):
    pass