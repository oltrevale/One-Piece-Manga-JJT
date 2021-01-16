from PIL import Image
import logging

logging.basicConfig(filename='ciao.log', level=logging.INFO)


def crea_pdf_capitolo(lunghezza_lista, capitolo):
    lista = []
    for pagina in range(1, lunghezza_lista):
        image = Image.open(f'C:\\Users\\K\\Desktop\\{capitolo}\\{pagina}.png')
        image = image.convert('RGB')
        lista.append(image)
    image.save(f'C:\\Users\\K\\Desktop\\{capitolo}.pdf', save_all=True, append_images=lista)


def crea_pdf_capitoli(capitolo_inizio, capitolo_fine, dizionario):
    lista = []
    for capitolo in range(capitolo_inizio, capitolo_fine + 1):
        for pagina in range(1, dizionario[capitolo]):
            image = Image.open(f'c:\\Users\\K\\Desktop\\{capitolo}\\{pagina}.png')
            image = image.convert('RGB')
            lista.append(image)
    logging.info(len(lista))
    for elemento in lista:
        logging.info(elemento)
        logging.info('\n')
    image = lista[0]
    image.save(f'C:\\Users\\K\\Desktop\\{capitolo_inizio}-{capitolo_fine}.pdf', save_all=True, append_images=lista[1:])
