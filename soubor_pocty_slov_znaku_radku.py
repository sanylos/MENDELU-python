def cetnosti(vstup):
    pocty = dict()
    while True:
        char = vstup.read(1)
        if not char:
            break
        for x in char:
            if x in pocty:
                pocty[x] += 1
            else:
                pocty[x] = 1
    return pocty

def cetnosti_slov(vstup):
    slova = dict()
    for line in vstup:
        for word in line.split():
            if word in slova:
                slova[word] += 1
            else:
                slova[word] = 1
    return slova

def pocet_radku(vstup):
    linecount = 0
    for line in vstup:
        linecount+=1
    return linecount


soubor = open("text.txt", "r")
print(cetnosti(soubor))
soubor.seek(0)
print(cetnosti_slov(soubor))
soubor.seek(0)
print(pocet_radku(soubor))
