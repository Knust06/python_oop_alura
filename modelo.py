class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title() #_Programa__nome
        self.ano = ano
        self._likes = 0

    def dar_like(self):
        self._likes += 1
    
    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()
class Filme(Programa): #Herança seria criar uma classe que herda de outra que no caso a classe filme está herdando da classe Programa.
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

vingadores = Filme('vingadores - ultimato',2018, 160)

chosen = Serie('the chosen', 2020, 3)

vingadores.dar_like()

chosen.dar_like()

chosen.dar_like()

print(f"{vingadores.nome} - {vingadores.ano} - {vingadores.duracao} - {vingadores.likes}")
print(f"{chosen.nome} - {chosen.ano} - {chosen.temporadas} - {chosen.likes}")

filmes_e_series = [vingadores, chosen]

for programa in filmes_e_series:
    detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
    print(f"{programa.nome} - {detalhes} - {programa.likes}")