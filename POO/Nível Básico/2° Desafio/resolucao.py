class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def area(self):
        return self.largura * self.altura


c = Retangulo(5,9)
print(f"A área do retângulo é: {c.area()}")