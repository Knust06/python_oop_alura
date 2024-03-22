class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    def dar_like(self):
        self.__likes += 1
    
    @property
    def likes(self):
        return self.__likes

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()
class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0
    
    def dar_like(self):
        self.__likes += 1
    
    @property
    def likes(self):
        return self.__likes

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

vingadores = Filme('vingadores - ultimato',2018, 160)

chosen = Serie('the chosen', 2020, 3)

vingadores.dar_like()

chosen.dar_like()

chosen.dar_like()

print(f"Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - Likes: {vingadores.likes}")
print(f"Nome: {chosen.nome} - Ano: {chosen.ano} - Temporadas: {chosen.temporadas} - Likes: {chosen.likes}")