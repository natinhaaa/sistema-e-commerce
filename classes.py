#Criamos a seguinte classe apenas para definirmos os atributos que um Cliente deve ter nesse sistema
class Clientes:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
        self.carrinho = []
	  
	#Vai retornar o valor que se encontra dentro do carrinho, que é único para cada Cliente
    def getCarrinho_Compras(self):
        return self.carrinho

######################################################################

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

######################################################################

#Nesta classe, encontra-se os métodos que o sistema tem a oferecer ao Cliente
class Loja:
    def __init__(self):
        self.clientes = {}
        self.produtos = []
    
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
    
    def cadastro_cliente(self, nome, senha):
        cliente = Clientes(nome, senha)
        if nome not in self.clientes:
            self.clientes[nome] = cliente
            print("Você foi cadastrado!")

        else:
            print("Nome de usuário já existe.")
    
    def login(self, nome, senha):
        for chave, valor in self.clientes.items():
            if chave == nome and valor.senha == senha:
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

class Admin:
    def __init__(self, usuário, senha):
        self.usuário = usuário
        self.senha = senha