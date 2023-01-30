#importação de bibliotecas para /caminhos de sistema / YouTube / Controle de tempo
from pathlib import Path 
from pytube import YouTube 
from time import sleep

#Caminho no sistema do arquivo TXT, 
caminhoLista = (Path.home()/'Documentos'/'lista.txt')

#abrir arquivo Lista em modo leitura e leitura das linhas
with open (caminhoLista,'r') as listaLer:

    lista = listaLer.readlines()

#função de Download dos links lidos do TXT
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

#Ler tamanho da lista e passagem da linha para a variavel link    
i=0
x = len(lista)
print(f'O software ira realizar o download de {x-1} arquivos\n')

while (i < x):
    link = lista[i]
    Download(link)
    i+=1

#fim do programa
print('\nFim da lista de downloads')