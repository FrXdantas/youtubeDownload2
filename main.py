from pathlib import Path 
caminhoLista = (Path.home()/'Documentos'/'lista.txt')

with open (caminhoLista,'r') as listaLer:

    lista = listaLer.read()

    
print (lista)