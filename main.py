from pathlib import Path 
from pytube import YouTube 

caminhoLista = (Path.home()/'Documentos'/'lista.txt')

with open (caminhoLista,'r') as listaLer:

    lista = listaLer.readlines()

def Download (link):
    youtubeObjeto = YouTube(link)
    youtubeObjeto = youtubeObjeto.streams.get_highest_resolution()
    youtubeObjeto = youtubeObjeto
    caminho_video = (Path.home() / 'Downloads')

    try:
        youtubeObjeto.download(caminho_video)
    except:
        print('Erro ao baixar video')
    print('Download do Video do Youtube Completo')
    print(f'Salvo em : {caminho_video}')


for x in range(len(lista)):
    link = lista[x]
    print(f'{x+1} - {link}')
    Download(link)
print('\nFim da lista de downloads')
