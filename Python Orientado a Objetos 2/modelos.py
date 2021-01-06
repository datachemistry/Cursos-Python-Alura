class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome
        
    def __str__(self):
        return f'Nome: {self.nome} Likes: {self.likes}'
    

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    
    def __str__(self):
        return f'Nome: {self.nome} - {self.duracao} min - Likes: {self.likes}'
        
    
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)           
        self.temporadas = temporadas
    
    def __str__(self):
        return f'Nome: {self.nome} - {self.temporadas} temporadas - Likes: {self.likes}'
       

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
lor = Filme('o senhor dos aneis', 2001, 200)

atlanta.dar_likes()
atlanta.dar_likes()
lor.dar_likes()
lor.dar_likes()
lor.dar_likes()
lor.dar_likes()
lor.dar_likes()

filmes_e_series = [vingadores, atlanta, lor]
    
for programa in filmes_e_series:
    print(programa)