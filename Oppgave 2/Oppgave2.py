from datetime import datetime

date =input("Skriv inn en dato ")
try:
   date_object = datetime.strptime (date,"%d/%m/%Y")
   print(date_object)

except ValueError:
    print("Feil: ugyldig dato!")




#oppgave 2.2

lister = ["Cecilie" , 28, "Bjørn" , 30,"Tor", 24, "Anna" , 25]
navnene = []
alder = []
for l in lister :

  if type(l) == str :

    navnene.append (l)

  else :
    alder.append(l)

print(  navnene,  alder)



#oppgave 2.3


lister = ["Cecilie" , 28, "Bjorn" , 30, "Tor", 24, "Anna" , 25]

navn = lister [::2]
alder = lister [1::2]

personer = dict(zip(navn,alder))

for n,a in personer.items():
    print (f"{n} er {a} år")


#oppgaev 2.4
lister = ["Cecilie" , 28, "Bjørn" , 30, "Tor", 24, "Anna" , 25]

navn = lister [::2]
alder = lister [1::2]

personer = dict(zip(navn,alder))
sortert = dict(sorted(personer.items(), key= lambda x:x[1], reverse=True))
for n,a in sortert.items():
    print(f"{n} er {a} år")


#oppgave 2.5
lister = ["Cecilie" , 28, "Bjørn", 30, "Tor", 24, "Anna" , 25]

navn = lister [::2]
alder = lister [1::2]

personer = dict(zip(navn,alder))
sortert = dict(sorted(personer.items(), key= lambda x:x[0] ))


ny_liste = []
for n,a in sortert.items():
    ny_liste.extend([n,a])
print(ny_liste)

#oppgvae 2.6

lister = ["Cecilie" , 28, "Bjørn" , 30, "Tor", 24, "Anna" , 25]
liste_av_dicts = []

for i in range(0, len(lister), 2):
    entry = {"navn": lister[i], "alder": lister[i+1]}
    liste_av_dicts.append(entry)

print(liste_av_dicts)








    