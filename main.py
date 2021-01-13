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
        scarica_pagina.scarica_pagina(pagina, capitolo)
        print(f"La pagina numero {pagina} del capitolo numero {capitolo} è stata scaricata")
        menu()
    if immissione == 2:
        # TODO: permeettere di aggiungere capitolo a volume .pdf
        capitolo = input("Numero del capitolo?")
        lunghezza_lista = scarica_pagina.scarica_capitolo(capitolo)
        archivia.crea_pdf_capitolo(lunghezza_lista, capitolo)
        print(f"Capitolo numero {capitolo} scaricato")
        menu()
    if immissione == 3:
        # TODO aggiungi opzione per non aggiungere capitoli ad unico pdf
        dizionario = {}
        capitolo_inizio = int(input("Estremo range da cui iniziare a scaricare?"))
        capitolo_fine = int(input("Estremo range in cui terminare?"))
        capitolo_fine = capitolo_fine + 1  # per il range
        for capitolo in range(capitolo_inizio, capitolo_fine):
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
