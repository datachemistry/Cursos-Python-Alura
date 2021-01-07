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
      
class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
        
    def __getitem__(self, item):
        return self._programas[item]
    
    def __len__(self):
        return len(self._programas)
    
        

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
lor = Filme('o senhor dos aneis', 2001, 200)
harry_potter_1 = Filme('Harry Potter e a Pedra Filosofal', 2000, 180)
atlanta = Serie('atlanta', 2018, 2)
got = Serie('Game of Thrones', 2017, 7)
breaking_bad = Serie('breaking bad', 2015, 8)

atlanta.dar_likes()
atlanta.dar_likes()
lor.dar_likes()
lor.dar_likes()
lor.dar_likes()
lor.dar_likes()
lor.dar_likes()
breaking_bad.dar_likes()
breaking_bad.dar_likes()
breaking_bad.dar_likes()
got.dar_likes()
got.dar_likes()



filmes_e_series = [vingadores, atlanta, lor, got, breaking_bad, harry_potter_1]

playlist_fds = Playlist('fim de semana', filmes_e_series)
   
for programa in playlist_fds:
    print(programa)

print(f'Tamanho da playlist:{len(playlist_fds)}')

print(playlist_fds[0])