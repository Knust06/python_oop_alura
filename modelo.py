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
    
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} likes'
class Filme(Programa): #Herança seria criar uma classe que herda de outra que no caso a classe filme está herdando da classe Programa.
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} likes'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} likes'

class Playlist: #Não usamos herança, mas sim composição, pois a playlist não é um tipo de programa, ela tem uma lista de programas.
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
    def __getitem__(self, item):
        return self._programas[item]
    def __len__(self):
        return len(self._programas)

vingadores = Filme('vingadores - ultimato',2018, 160)
chosen = Serie('the chosen', 2020, 3)
tmep = Filme('Todo mundo em panico', 1999, 100)
drive = Filme('Drive', 2011, 95)
demolidor = Serie('Demolidor', 2016, 2)

tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
drive.dar_like()
vingadores.dar_like()
chosen.dar_like()
chosen.dar_like()

filmes_e_series = [vingadores, chosen, tmep, drive, demolidor]
fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho da playlist: {len(fim_de_semana)}')

for programa in fim_de_semana:
    print(programa) 


#Abstract Base Classes - ABC - São classes que não podem ser instanciadas, são classes que servem para serem herdadas. E com isso podemos garantir que as classes filhas tenham os métodos que queremos que elas tenham.
#MRO - Method Resolution Order - É a ordem que o python vai procurar os métodos que estamos chamando. O python vai procurar primeiro na classe que estamos instanciando, depois na classe mãe e assim por diante.
#Good Head - Grandmother, Mother, Daughter - É uma forma de lembrar a ordem que o python vai procurar os métodos.
#Mixin - É uma classe que não é a principal, mas sim uma classe que tem um comportamento específico que pode ser usado em outras classes. Exemplo: Uma classe que tem um método de autenticação, essa classe pode ser usada em outras classes que precisam de autenticação.
#Duck Typing - É um conceito que diz que se um objeto se comporta como um pato, então ele é um pato. Ou seja, se um objeto tem um método que se comporta como um método de um pato, então ele é um pato.