class Loja:
    produtos = []
    admins = {}
    clientes = {}
    def __init__(self, nomeLoja, endereçoLoja, cnpj):
        self.nomeLoja = nomeLoja
        self.endereçoLoja = endereçoLoja
        self.cnpj = cnpj
        

    def getNomeLoja(self):
        return self.nomeLoja
    
    def getEndereçoLoja(self):
        return self.endereçoLoja
    
    def getCNPJ(self):
        return self.cnpj
    
    def getClientes(self):
        return self.clientes
    
############################################################################
    
    def InformaçõesCliente(self, cliente, id):
        dic2=Loja.clientes()
        if id not in dic2:
            dic2[id] = cliente
            print("Você foi cadastrado.")
        
        else:
            print("O usuário já está cadastrado")
    
    def InformaçõesAdmin(self, usuário, senha):
        dic1=Loja.admins()
        dic2=Loja.clientes()
        admin = Admin(usuário, senha)
        if usuário not in dic1:
            dic2[usuário] = admin
            print("Você foi cadastrado como administrador.")
        
        else:
            print("O administrador já está cadastrado")
    
########################################################################################################################
    
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

        def getNomeCad(self):
            return self.nome

        def getDatNasCad(self):
            return self.datnasc
    
        def getCPFCad(self):
            return self.cpf
    
        def getEndereçoCad(self):
            return self.endereço
    
        def getSenhaCad(self):
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
        self.append(produto_cadastrado)
        print("Produto adicionado!")

    def listar_produtos(self):
        lista=Loja.produtos()
        print("Produtos Disponíveis")
        contID = 0
        for produto in lista:
            contID += 1
            print(f"ID - {contID}\nNome: {produto.getNome()}\nDescrição: {produto.getDesc()}\nPreço: R${produto.getPreço()}\n")
    
    def excluir_produto_loja(self, id_produto):
        lista=Loja.produtos()
        lista.pop(id_produto - 1)
    
##########cadastro
    def cadastro_cliente(self, cliente, id):
            loja.InformaçõesCliente(cliente, id)

    def cadastro_admin(self, nome, usuário, senha):
        self.nome = nome
        self.usuário = usuário
        self.senha = senha
        # nome = Admin(usuário = input("Digite o usuário: "), senha = int(input("Digite a senha: ")))

###########login
    def login_cliente(self, cliente, id):
        dic2=Loja.clientes()
        for chave, valor in self.clientes.items():
            if chave == id and valor.senha == cliente:
                print("Login bem sucedido.")
                return True
        else:
            print("Nome de usuário ou senha incorretos.")
            return False
    
    def login_admin(self, usuário, senha):
        dic1=Loja.admins()
        for chave, valor in dic1.items():
            if chave == usuário and valor.senha == senha:
                print("Login bem sucedido.")
                return True
        else:
            print("Nome de usuário ou senha incorretos.")
            return False

    def getIDproduto(self, id_produto):
        lista=Loja.produtos
        return lista[id_produto - 1]

##############################################################################################

#Nestas últimas funções, temos o atributo "nome", que precisa ser passado para podermos confirmar que o produto adicionado no Carrinho de Compras seja o carrinho único de um cliente que o nome seja tal que está dentro da lista de clientes da Loja
    def adicionar_produto_carrinho(self, produto_cadastrado, nome):
        dic2=Loja.clientes()
        dic2[nome].getCarrinho_Compras().append(produto_cadastrado)
        print("O item foi adicionado ao carrinho!")

    def listar_carrinho(self, nome):
        dic2=Loja.clientes()
        contID = 0
        for produto in dic2[nome].getCarrinho_Compras():
            contID += 1
            print(f"{contID}.\nNome: {produto.getNome()}\nDescrição: {produto.getDesc()}\nPreço: R${produto.getPreço()}\n")
    
    def excluir_produto_carrinho(self, nome, id_produto):
        dic2=Loja.clientes()
        dic2[nome].getCarrinho_Compras().pop(id_produto - 1)
        print("Produto excluído.")
    
    def calcular_total(self, nome):
        dic2=Loja.clientes()
        total_produtos = 0
        contID = 0
        for produto in dic2[nome].getCarrinho_Compras():
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

# class Relatórios(Clientes, Produtos, Loja ):
    
#      def visualizarClientes():
#          pass
     
#      def visualizarProdutos():
#          pass
     
    