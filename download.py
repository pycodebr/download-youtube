from pytube import YouTube

# Digite o link do vídeo e o local que deseja salvar o video #
link = input("Digite o link do vídeo que deseja baixar:  ")
path = input("Digite o diretório que deseja salvar o vídeo:  ")
yt = YouTube(link)

# Mostra os detalhes do video #
print("Título: ", yt.title)
print("Número de views: ", yt.views)
print("Tamanho do vídeo: ", yt.length, "segundos")
print("Avaliação do vídeo: ", yt.rating)

# Usa a maior resolucao #
ys = yt.streams.get_highest_resolution()

# Começa o Download do vídeo #
print("Baixando...")
ys.download(path)
print("Download completo!")