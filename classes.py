class Produtos:
    def __init__(self, nome, desc, preço):
        self.nome = nome
        self.desc = desc
        self.preço = preço
    
    def getNome(self):
        return self.nome

    def getDesc(self):
        return self.nome

    def getPreço(self):
        return self.nome
    
class Admin:
    def __init__(self):
        self.clientes = {}
        self.produtos = []
    
    def cadastrar_produtos(self, nome, desc, preço:int, id:int):
        self.nome = nome
        self.desc = desc
        self.preço = preço
        self.id = id

        self.produto = [nome, desc, preço, id]
        self.produtos.append(self.produto)

        print(f"Produto adicionado\nID - {self.getID()}\nNome: {self.getNome()}\nDescrição: {self.getDesc()}\nPreço: R${self.getPreço()}")

    def listar_produtos(self):
        print("PRODUTOS DISPONÍVEIS")
        for produto in self.produtos:
            print("______________________________________________________")
            print (f"ID - {produto[3]}\nNome: {produto[0]}\nDescrição: {produto[1]}\nValor: {produto[2]}")

    def getNome(self):
        return self.nome
    
    def getDesc(self):
        return self.desc
    
    def getPreço(self):
        return self.preço
    
    def getID(self):
        return self.id
    
    def excluir(self, produto_excluir):
        self.produtos.pop(produto_excluir - 1)
        print (f"PRODUTOS DISPONÍVEIS\n")
        for produto in self.produtos:
            print("______________________________________________________")
            print(f"ID - {produto[3]}\nNome: {produto[0]}\nDescrição: {produto[1]}\nValor: {produto[2]}")
            
###############################################################################################################

class Clientes_Loja(Admin):
    def __init__(self):
        self.nomeCad = None
        self.senhaCad = None
        self.cliente = {}
        self.carrinho = []

    def cadastro(self, nomeCad, senhaCad):
        if nomeCad not in self.cliente:
            self.cliente[nomeCad] = senhaCad
            print("Você foi cadastrado")

        else:
            print("Nome de usuário já existe.")

    def login(self, nome, senha):
        if nome in self.cliente and self.cliente[nome] == senha:
            print("Login bem-sucedido!")
            return True
            
        else:
            print("Nome de usuário ou senha incorretos.")
            return False
            
    def adicionar_produto_carrinho(self, produto_add):
        self.carrinho.append(produto_add)
        print("Produto adicionado ao carrinho")
    
    def listar_carrinho(self):
        print("PRODUTOS NO CARRINHO")
        for produto in self.carrinho:
            print("______________________________________________________")
            print (f"ID - {produto[3]}\nNome: {produto[0]}\nDescrição: {produto[1]}\nValor: {produto[2]}")

            
    def excluir_produto(self, produto):
        self.produto.dell(produto)

        print("______________________________________________________")
        print(f"Produto excluido\nNome: {self.getNome()}\nDescrição: {self.getDesc()}\nPreço: R${self.getPreço()}\nID: {self.getID()}")
        print("______________________________________________________")
    
    def calcular_total(self):
        total = 0 
        for produto in self.produtos:
            total += produto.valor
        return total
    
    def finalizar_compra(self):
        print(f"Total da compra: {self.calcular_total()}")
        print("Compra finalizada")
        self.carrinho = []

    def excluir_carrinho(self):
        self.carrinho = []
        print("Carrinho excluido")
