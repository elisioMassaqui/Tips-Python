#Crie uma classe Produto e uma classe
#  Carrinho De Compras para 
# gerenciar a adição e remoção 
# de produtos e calcular o total.

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []
    
    def adicionar_produtos(self, produto):
        self.produtos.append(produto)
    
    def calcular_total(self):
        return sum(p.preco for p in self.produtos)

p1 = Produto('Apple', 5)
p2 = Produto('Banana', 10)

carrinho = CarrinhoDeCompras()
carrinho.adicionar_produtos(p1)
carrinho.adicionar_produtos(p2)

print(f'Toral: {carrinho.calcular_total()}')
