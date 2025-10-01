import csv
import os

print(os.getcwd())

with open(r"C:\Users\filiz\Downloads\bokutlån.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    forlenget = 0

    for row in reader:
        if row:
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
            if row:
                sjanger = row[3]  # yazı ("Fantasy", "Krim", ...)
                # sayacı arttır
                sjanger_count[sjanger] = sjanger_count.get(sjanger, 0) + 1

    return sjanger_count


print(howMuch())


 #oppgave5.3
import csv

with open(r"C:\Users\filiz\Downloads\bokutlån.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # başlık satırını atla
    total = 0
    count =0
    for row in reader:
        if row:
            total += int(row[5])
            count += 1
    average = total / count
print(total)
print(average)


#oppgave 5.4
import csv

def ikkelevert():
    total = 0

    with open(r"C:\Users\filiz\Downloads\bokutlån.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            if len(row) > 7 and row[7].strip().lower() == "nei":
                total += 1
    return total

print(ikkelevert())

#oppgave 5.5
import csv

def flestGanger():
    count = 0
    title = ""

    with open(r"C:\Users\filiz\Downloads\bokutlån.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            if row:
                title = row[3]
                count += 1

    return title, count
print(flestGanger())
