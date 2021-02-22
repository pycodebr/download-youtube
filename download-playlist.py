from pytube import Playlist

playlist = Playlist(input('Digite o link da playlist que deseja baixar: '))
path = input('Destino do download: ')

print(f'Iniciando o download dos vídeos da playlist: {playlist.title}\n')

for indice, video in enumerate(playlist.videos):
    print(f'Baixando vídeo {indice + 1}/{len(playlist)}')
    video.streams.first().download(path)
    
print('Todos os vídeos foram baixados!')