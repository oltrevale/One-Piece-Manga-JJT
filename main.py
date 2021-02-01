import scarica_pagina
import archivia


def menu():
    print("Inserisci 1 per scaricare una pagina di un Capitolo")
    print("Inserisci 2 per scaricare un Capitolo")
    print("Inserisci 3 per scaricare in un range di Capitoli")
    immissione = int(input())
    if immissione == 1:
        pagina = input("pagina del Capitolo?")
        capitolo = input("Numero del Capitolo?")
        scarica_pagina.recupera_link(pagina, capitolo)
        print(f"La pagina numero {pagina} del capitolo numero {capitolo} è stata scaricata")
        menu()
    if immissione == 2:
        print('1 per aggiungere capitolo a pdf')
        print('quasiasi altro per non aggiungerlo')
        immissione = int(input())
        if immissione == 1:
            capitolo = input("Numero del capitolo da scaricare")
            pdf = input('Numero pdf da aggiungere')
            capitolo_inizio = input('Primo capitolo de pdf')
            lunghezza_lista = scarica_pagina.scarica_capitolo(capitolo)
            archivia.aggiungi_capitolo_pdf(capitolo, lunghezza_lista, pdf, capitolo_inizio)
            print(f"Capitolo numero {capitolo} scaricato")
        else:
            capitolo = input('Numero del capitolo da scaricare')
            lunghezza_lista = scarica_pagina.scarica_capitolo(capitolo)
            # archivia.crea_pdf_capitolo(lunghezza_lista, capitolo)
        menu()
    if immissione == 3:
        # TODO aggiungi opzione per non aggiungere capitoli ad unico pdf
        dizionario = {}
        capitolo_inizio = int(input("Estremo range da cui iniziare a scaricare?"))
        capitolo_fine = int(input("Estremo range in cui terminare?"))
        for capitolo in range(capitolo_inizio, capitolo_fine + 1):
            lunghezza_lista = scarica_pagina.scarica_capitolo(capitolo)
            dizionario[capitolo] = lunghezza_lista
            print(f"Capitolo numero {capitolo} scaricato")
        archivia.crea_pdf_capitoli(capitolo_inizio, capitolo_fine, dizionario)
        print("Tutti i capitoli sono stati scaricati")
        menu()
    else:
        print("Inserito un numero non corretto")
        menu()


if __name__ == "__main__":
    menu()
