import os
from PIL import Image
import requests
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO, filename='came.log')
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/39.0.2171.95 Safari/537.36'}
path = "C:\\Users\\K\\Desktop"


def recupera_link(capitolo, pagina):
    capitolo = str(capitolo)
    pagina = str(pagina)

    link = f"https://www.juinjutsureader.ovh/read/one-piece/it/0/{capitolo}/page/{pagina}"
    risposta = requests.get(link, headers=headers)
    soup = BeautifulSoup(risposta.text, "html.parser")
    immagine = soup.find(class_="open open_image")
    link = immagine["src"]
    link = link.replace(" ", "")
    print(link)
    return link


def scarica_capitolo(capitolo):
    indice = 1
    try:
        os.mkdir(f"{path}\\{capitolo}")
    except OSError:
        pass
    lista = []
    try:
        for pagina in range(1, 23):
            link = recupera_link(capitolo, pagina)
            if link in lista:
                pass
            else:
                lista.append(link)
    except:
        pass
    for link in lista:
        with open(f"{path}\\{capitolo}\\{indice}.png", "wb") as f:
            richiesta = requests.get(link, headers=headers)
            f.write(richiesta.content)
            indice += 1
    return len(lista)


def rimuovi_immagini_inutili(capitolo, numero_pagine):
    # TODO bisogna costruirlo da zeo
    indice = 1
    for pagina in range(1, numero_pagine + 1):
        image = Image.open(f'{path}//{capitolo}//{pagina}.png')
        image = image.convert('RGB')
        if image.size:
            os.rename(f'{path}//{capitolo}//{pagina}.png', f'{path}//{capitolo}//{indice}.png')
        else:
            os.rename(f'{path}//{capitolo}//{pagina}.png', f'{path}//{capitolo}// prova.png')

        # devi eliminare file inutile e devi rinominare file successivi affinché si continui con numerazione giusta
        # in piu devi tener conto di quanti immagini utili ci sono


if __name__ == "__main__":
    scarica_capitolo(912)
