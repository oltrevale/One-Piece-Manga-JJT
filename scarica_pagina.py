import os
from PIL import Image
import requests
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO, filename='came.log')
lista = []
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/39.0.2171.95 Safari/537.36'}


def recupera_link(capitolo, pagina):
    capitolo = str(capitolo)
    pagina = str(pagina)

    link = f"https://www.juinjutsureader.ovh/read/one-piece/it/0/{capitolo}/page/{pagina}"
    risposta = requests.get(link, headers=headers)
    soup = BeautifulSoup(risposta.text, "html.parser")
    immagine = soup.find(class_="open open_image")
    link = immagine["src"]
    link = link.replace(" ", "")
    return link


def scarica_capitolo(capitolo):
    indice = 1
    try:
        os.mkdir(f"C:\\Users\\K\\Desktop\\{capitolo}")
    except OSError:
        pass
    dizionario = {}
    for pagina in range(1, 23):
        link = recupera_link(capitolo, pagina)
        if link in dizionario.keys():
            pass
        else:
            dizionario[link] = pagina
    print(dizionario.values)
    for link in dizionario.keys():
        with open(f"C:\\Users\\K\\Desktop\\{capitolo}\\prova.png", "wb") as f:
            f.write(requests.get(link, headers=headers).content)
        image = Image.open(f'C:\\Users\\K\\Desktop\\{capitolo}\\prova.png')
        image = image.convert('RGB')
        if image.size == (3385, 2560) or image.size == (1390, 2100):
            image.close()
            os.rename(f"C:\\Users\\K\\Desktop\\{capitolo}\\prova.png",
                      f"C:\\Users\\K\\Desktop\\{capitolo}\\{indice}.png")
            indice += 1
            logging.info(indice)
            logging.info('\n')

        else:
            pass
    return indice


if __name__ == "__main__":
    scarica_capitolo(912)
