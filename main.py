import ScaricaPagina
import Archivia


def menu():
    print("Inserisci 1 per scaricare una Pagina di un Capitolo")
    print("Inserisci 2 per scaricare un Capitolo")
    print("Inserisci 3 per scaricare in un range di Capitoli")
    immissione = int(input())
    if immissione == 1:
        Pagina = input("Pagina del Capitolo?")
        Capitolo = input("Numero del Capitolo?")
        ScaricaPagina.ScaricaPagina(Pagina, Capitolo)
        print(f"La pagina numero {Pagina} del capitolo numero {Capitolo} è stata scaricata")
        menu()
    if immissione == 2:
        Capitolo = input("Numero del capitolo?")
        ScaricaPagina.ScaricaCapitolo(Capitolo)
        Archivia.archivia_rinomina(Capitolo)
        print(f"Capitolo numero {Capitolo} scaricato")
        menu()
    if immissione == 3:
        CapitoloInizio = int(input("Estremo range da cui iniziare a scaricare?"))
        CapitoloFine = int(input("Estremo range in cui terminare?"))
        CapitoloFine = CapitoloFine+1  # per il range
        for Capitolo in range(CapitoloInizio, CapitoloFine):
            ScaricaPagina.ScaricaCapitolo(Capitolo)
            Archivia.archivia_rinomina(Capitolo)
            print(f"Capitolo numero {Capitolo} scaricato")
        print("Tutti i capitoli sono stati scaricati")
        menu()
    else:
        print("Inserito un numero non corretto")
        menu()


if __name__ == "__main__":
    menu()
