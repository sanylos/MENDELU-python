def seznam_nahodnych_cisel(pocet, start, konec):
    import random
    return [random.randint(start, konec) for x in range(pocet)]

def dej_cetnosti(seznam):
    cetnosti = dict()
    for x in seznam:
        if x in cetnosti:
            cetnosti[x] += 1
        else:
            cetnosti[x] = 1
    return cetnosti


def vypis_slovnik(slovnik):
    for klic, hodnota in slovnik.items():
        print(f" {klic} : {hodnota}")


vypis_slovnik(dej_cetnosti(seznam_nahodnych_cisel(100, -10, 10)))