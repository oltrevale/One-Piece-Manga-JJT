# TODO  inserisci log
# TODO migliorare visualizzazione pdf
# TODO aggiungere bookmarks
# TODO trova modo per eliminare immagini dupplicate
# TODO inserisci commenti
# FIXME passa a inglese
from PIL import Image


def crea_pdf_capitolo(lunghezza_lista, capitolo):
    lista = []
    for pagina in range(1, lunghezza_lista + 1):
        image = Image.open(f'C:\\Users\\K\\Desktop\\{capitolo}\\{pagina}.png')
        image = image.convert('RGB')
        lista.append(image)
    image.save(f'C:\\Users\\K\\Desktop\\{capitolo}.pdf', save_all=True, append_images=lista)


def crea_pdf_capitoli(capitolo_inizio, capitolo_fine, dizionario):
    # FIXME utima pagina diventa prima nel pdf
    lista = []
    for capitolo in range(capitolo_inizio, capitolo_fine):
        for pagina in range(1, dizionario[capitolo]):
            image = Image.open(f'c:\\Users\\K\\Desktop\\{capitolo}\\{pagina}.png')
            image2 = image.convert('RGB')
            lista.append(image2)
    image2.save(f'C:\\Users\\K\\Desktop\\{capitolo_inizio}-{capitolo_fine}.pdf', save_all=True, append_images=lista)
