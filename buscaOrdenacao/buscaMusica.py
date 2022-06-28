class Song: ##Classe principal com metodo que da atributos a musica.
    def __init__(self, titulo, artista, album):
        self.titulo = titulo
        self.artista = artista
        self.album = album


class Search: # Metodo que procura a musica.
    def search_title(self, playlist, titulo):
        for i in range(len(playlist)):
            if playlist[i].titulo == titulo:
                return i
        return -1

    def finding(self):
        playlist = [Song("Music For a Sushi Restaurant", "Harry Styles", "Harry's House"),
                    Song("Marooned", "Pink Floyd", "The Division Bell"),
                    Song("Running Up That Hill", "Car Seat Headrest", "Covers")]
        nome = input("Digite o nome: ")

        found = self.search_title(playlist, nome)
        if found == -1:
            print("Nao tem")
        else:
            fav = playlist[found]
            print(f'{fav.titulo} by {fav.artista}, {fav.album}')


s = Search()
s.finding()
