class Pessoa:
    def __init__(self, nome, idade) -> str:
        self.nome = nome 
        self.idade = idade

    def saudacao(self):
        return f"Olá {self.nome}, é um prazer ter você aqui! \n Bora codar e desbravar o mundo."

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


p = Pessoa("Leonardo", "25")
s = p.saudacao()
print(s)
