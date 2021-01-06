import requests
from bs4 import BeautifulSoup
import os
import time
from PIL import Image

lista = []
def ScaricaPagina(Pagina, Capitolo):
    Pagina = str(Pagina)
    Capitolo = str(Capitolo)
    try:
        os.mkdir(f"C:\\Users\\Kappa\\Desktop\\{Capitolo}")
    except OSError:
        pass
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    link = f"https://www.juinjutsureader.ovh/read/one-piece/it/0/{Capitolo}/page/{Pagina}"
    risposta = requests.get(link, headers=headers)
    soup = BeautifulSoup(risposta.text, "html.parser")
    immagine = soup.find( class_="open open_image")
    link = immagine["src"]
    link = link.replace(" ", "")
    with open(f"C:\\Users\\Kappa\\Desktop\\{Capitolo}\\{Pagina}.png", "wb") as f:
        f.write(requests.get(link).content)
    image = Image.open(f'C:\\Users\\Kappa\\Desktop\\{Capitolo}\\{Pagina}.png')
    image = image.convert('RGB')
    lista.append(image)
    print(f"la pagina numero {Pagina} del capitolo numero {Capitolo} è stata scaricata")
    print(link)
    return image


def ScaricaCapitolo(Capitolo):
    for Pagina in range(1, 23):
        image = ScaricaPagina(Pagina, Capitolo)
        time.sleep(3)
    image.save(f'C:\\Users\\Kappa\\Desktop\\{Capitolo}.pdf',save_all=True, append_images=lista)

if __name__ == "__main__":
    ScaricaCapitolo(912)
