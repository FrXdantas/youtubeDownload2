from pathlib import Path 
from pytube import YouTube 
from time import sleep

caminhoLista = (Path.home()/'Documentos'/'lista.txt')

with open (caminhoLista,'r') as listaLer:

    lista = listaLer.readlines()

def Download (link):
    print(f'baixando aquivo: {link}')
    youtubeObjeto = YouTube(link)
    youtubeObjeto = youtubeObjeto.streams.get_highest_resolution()
    youtubeObjeto = youtubeObjeto
    caminho_video = (Path.home() / 'Downloads')
    sleep(2)

    try:
        youtubeObjeto.download(caminho_video)
    except:
        print('Erro ao baixar video')
    print('Download do Video do Youtube Completo')
    print(f'Salvo em : {caminho_video}\n')
i=0
x = len(lista)
print(f'O software ira realizar o download de {x-1} arquivos\n')

while (i < x):
    link = lista[i]
    Download(link)
    i+=1

print('\nFim da lista de downloads')