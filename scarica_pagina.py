import os

import requests
from bs4 import BeautifulSoup

lista = []


def scarica_pagina(pagina, capitolo):
    pagina = str(pagina)
    capitolo = str(capitolo)
    try:
        os.mkdir(f"C:\\Users\\K\\Desktop\\{capitolo}")
    except OSError:
        pass
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/39.0.2171.95 Safari/537.36'}
    link = f"https://www.juinjutsureader.ovh/read/one-piece/it/0/{capitolo}/page/{pagina}"
    risposta = requests.get(link, headers=headers)
    soup = BeautifulSoup(risposta.text, "html.parser")
    immagine = soup.find(class_="open open_image")
    link = immagine["src"]
    link = link.replace(" ", "")
    with open(f"C:\\Users\\K\\Desktop\\{capitolo}\\{pagina}.png", "wb") as f:
        f.write(requests.get(link).content)
    print(f"la pagina numero {pagina} del capitolo numero {capitolo} è stata scaricata")
    print(link)
    return link


def scarica_capitolo(capitolo):
    lista_link = []
    for pagina in range(1, 23):
        link = scarica_pagina(pagina, capitolo)
        if link in lista_link:
            pass
        else:
            lista_link.append(link)
    return len(lista_link)


if __name__ == "__main__":
    scarica_capitolo(912)
