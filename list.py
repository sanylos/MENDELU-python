def dej_seznam_celych_cisel(text="",oddelovac=" "):
    vstup = input(text)
    seznam = list()
    for x in vstup.split(oddelovac):
        try:
            seznam.append(int(x))
        except:
            continue
    return seznam

print(dej_seznam_celych_cisel())