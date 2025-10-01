import csv
import os

print(os.getcwd())

with open(r"C:\Users\filiz\Downloads\bokutlån.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    forlenget = 0

    for row in reader:
        if len(row)>6:
            try:
                forlenget += int(row[6])
            except ValueError:
                pass

    print(forlenget)





#oppgave 5.2


def howMuch():
    sjanger_count = {}  # her sjanger için sayaç

    with open(r"C:\Users\filiz\Downloads\bokutlån.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)

        for row in reader:
            if len(row) >3  and row[3].strip():
                sjanger = row[3].strip()
                sjanger_count[sjanger] = sjanger_count.get(sjanger, 0) + 1

    return sjanger_count


print(howMuch())


 #oppgave5.3
import csv

with open(r"C:\Users\filiz\Downloads\bokutlån.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    total = 0
    count = 0
    for row in reader:
        if len(row) > 6:
            try:
                periode = int(row[5])          # låneperiode
                forlenget = int(row[6])        # forlengelse
            except ValueError:
                continue  # sayı değilse satırı atla

            total += (periode + forlenget)     # her iki gün ekleniyor
            count += 1

    average = total / count if count > 0 else 0
    average_hele_dager = round(average)
print(total)
print(average_hele_dager)



#oppgave 5.4
import csv

def ikkelevert():
    ikke_levert = []

    with open(r"C:\Users\filiz\Downloads\bokutlån.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            if len(row) > 7 and row[7].strip().lower() == "nei":
                fornavn = row[0].strip()
                etternavn = row[1].strip()
                boktittel = row[2].strip()
                ikke_levert.append((fornavn, etternavn, boktittel))
    return ikke_levert
for fn, en, bok in ikkelevert():
    print(f"{fn} {en} har ikke levert tilbake: {bok}")


#oppgave 5.5
import csv

def flestGanger():
    counts = {}

    with open(r"C:\Users\filiz\Downloads\bokutlån.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # header atla
        for row in reader:
            if len(row) > 2 and row[2].strip():
                title = row[2].strip()
                counts[title] = counts.get(title, 0) + 1

    if not counts:
        return []

    max_count = max(counts.values())  # en yüksek sayı
    topp = [(t, c) for t, c in counts.items() if c == max_count]
    topp.sort(key=lambda x: x[0])  # alfabetik sırala
    return topp

print(flestGanger())
