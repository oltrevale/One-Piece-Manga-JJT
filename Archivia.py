import shutil
import os


def archivia_rinomina(Capitolo):
    path = f"C:\\Users\\K\\Desktop\\{Capitolo}"
    shutil.make_archive(path, "zip", path)
    print(f"il capitolo {Capitolo} è stato compresso")
    os.rename(f"{path}.zip", f"{path}.CBZ")
    print(f"il capitolo {Capitolo} è stato rinominato in .CBZ")


if __name__ == "__main__":
    import ScaricaPagina
    import random

    Capitolo = str(random.randint(911, 971))
    ScaricaPagina.ScaricaCapitolo(Capitolo)
    archivia_rinomina(Capitolo)
