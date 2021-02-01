from PIL import Image
import os


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
    image = lista[0]
    image.save(f'C:\\Users\\K\\Desktop\\{capitolo_inizio}-{capitolo_fine}.pdf', save_all=True, append_images=lista[1:])


def aggiungi_capitolo_pdf(capitolo, lunghezza_lista, pdf, capitolo_inizio):
    # TODO estrai capitolo inizio da nome pdf tramite regix
    image0 = Image.open(f'C:\\Users\\K\\Desktop\\{capitolo}\\1.png')
    image0 = image0.convert('RGB')
    lista = []
    for pagina in range(2, lunghezza_lista):
        image = Image.open(f'C:\\Users\\K\\Desktop\\{capitolo}\\{pagina}.png')
        image = image.convert('RGB')
        lista.append(image)
    image0.save(f'C:\\Users\\K\\Desktop\\{pdf}.pdf', save_all=True, append_images=lista)
    os.rename(f'C:\\Users\\K\\Desktop\\{pdf}.pdf', f'C:\\Users\\K\\Desktop\\{capitolo_inizio}-{capitolo}.pdf')
