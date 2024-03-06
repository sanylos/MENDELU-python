def nactiDesetinnaCisla(text="Zadej",oddelovac=" "):
    return [float(x) for x in input(text).split(oddelovac)]

def nejblizePrumeru(seznam):
    pr = sum(seznam)/len(seznam)
    min = seznam[0]
    for x in seznam:
        if abs(pr-x)<abs(pr-min):
            min = x
    return min

seznam = nactiDesetinnaCisla()
print(nejblizePrumeru(seznam))