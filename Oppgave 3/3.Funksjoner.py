

#oppgave 3.1

def gyldig_ipv4(streng):
    parts = streng.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        num = int(part)
        if not 0 <= num <= 255:
            return False
    return True

#oppgave 3.2


from datetime import datetime
def dager_mellom(d1: str, d2: str) -> int:

    date1 = datetime.strptime(d1, "%d/%m/%Y")
    date2 = datetime.strptime(d2, "%d/%m/%Y")

    return abs((date2 - date1).days)



#oppagev 3.3


def rgb_to_hex(r: int, g: int, b: int) -> str:
    if not (0 <= r <=255 and 0<= g <=255 and 0 <= b <=255):
       return ("Feilmelding")

    HEX_code = "#{:02x}{:02x}{:02x}".format(r, g, b)
    return HEX_code




#oppgave 3.4

def forventer (func,expected,  *args, **kwargs):
    return func( *args, **kwargs)  == expected


print(forventer(gyldig_ipv4, True , "192.168.0.1"))
print(forventer(gyldig_ipv4, False,  "256.100.50.0"))
print(forventer(gyldig_ipv4, True,  "256.100.50.0"))


