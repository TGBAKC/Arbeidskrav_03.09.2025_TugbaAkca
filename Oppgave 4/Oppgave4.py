import os
import random
import shutil
from os.path import exists

from venv import create


#oppgave 4.1
def lag_filer():
    os.makedirs("Files" ,exist_ok=True)
    typer =  [".txt", ".csv", ".log"]
    basseng = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    for i in range (30):
        lengde = random.randint(5,10)
        navn = "".join(random.choice(basseng)  for _ in range(lengde))
        ext = random.choice(typer)
        full_path = os.path.join("Files", navn + ext)
        open(full_path, "w").close()

lag_filer()

  #oppgave 4.2



def sorter_filer():
    base = "SortedFiles"
    os.makedirs(os.path.join(base, "txt-files"), exist_ok=True)
    os.makedirs(os.path.join(base, "csv-files"), exist_ok=True)
    os.makedirs(os.path.join(base, "log-files"), exist_ok=True)

    for file in os.listdir("Files"):
        src = os.path.join("Files", file)
        if file.endswith(".txt"):
            shutil.move(src, os.path.join(base, "txt-files", file))
            print(file, "→ flyttet til txt-files mappen")
        elif file.endswith(".csv"):
            shutil.move(src, os.path.join(base, "csv-files", file))
            print(file, "→ flyttet til csv-files mappen")
        elif file.endswith(".log"):
            shutil.move(src, os.path.join(base, "log-files", file))
            print(file, "→ flyttet til log-files mappen")
sorter_filer()