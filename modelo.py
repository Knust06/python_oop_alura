class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao


class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas


vingadores = Filme('Vingadores - Ultimato',2018, 160)


chosen = Serie('The Chosen', 2020, 3)

print(f"Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao}")
print(f"Nome: {chosen.nome} - Ano: {chosen.ano} - Temporadas: {chosen.temporadas}")