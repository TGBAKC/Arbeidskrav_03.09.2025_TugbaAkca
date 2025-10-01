# oppgave 1.1


tall : int  = int(input ("Skriv inn et tall :"))
if tall<1:
    print("Feil: tallet må være positivt (>= 1).")
else:
   total =0
   for i in range (1,tall +1):
       total = total + i
   print (total)




# oppgave 1.2


a = input("Skriv inn en setning :")
b = input("Skriv inn en setning :")
len_a = len(a)
len_b = len(b)
if len_a > len_b:
     print( f"Første setning er lengst  ({len_a} tegn).")
elif len_a <  len_b :
     print(f"Andre setning er lengst ({len_b} tegn).")
else :
     print(f"Setningene er like lange ({len_a} tegn).")



# oppgave 1.3

n : int = int(input ("Skriv inn et tall :"))

for i in range (1,11):

    print(f" {n} * {i} = {n*i} ")



#oppgave 1.4

i : int = int(input("Skriv inn indeks :"))
j : int = int(input("Skriv inn indeks :"))


fruits = ["eple", "banan", "appelsin", "drue", "kiwi"]

if 0 <= i < len(fruits) and 0<= j <len(fruits):

   fruits [i] , fruits[j] = fruits [j], fruits[i]
   print("Oppdatert liste:" ,fruits)
else:
    print("ugyldig indeks")






#oppgave 1.5


m = int(input("Skriv inn et tall (m): "))
n = int(input("Skriv inn et tall (n): "))

if m > n:
    m, n = n, m

#
header = "| " + " | ".join(str(j) for j in range(m, n+1)) + " |"
print(header)


separator = "|" + "---|" * (n-m+1)
print(separator)


for i in range(m, n+1):
    row_values = [str(i * j) for j in range(m, n+1)]
    row = "| " + " | ".join(row_values) + " |"
    print(row)














