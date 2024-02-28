def dej_seznam_celych_cisel(text="",oddelovac=" "):
    vstup = input(text)
    seznam = list()
    min,max = 999999, -999999
    for x in vstup.split(oddelovac):
        try:
            seznam.append(int(x))
            if(x < min): min=x
            if(x > max): max=x
        except:
            continue
    return seznam

def kde_je_max(seznam):
    poz_max = 0
    for index, hodnota in enumerate(seznam):
        if(hodnota > seznam[poz_max]):
            poz_max = index
    return poz_max

s = dej_seznam_celych_cisel()
print(s)
print(kde_je_max(s))