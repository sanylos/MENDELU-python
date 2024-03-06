def vygenerujMatici(radky = 3, sloupce = 3):
    matice = list()
    for i in range(radky):
        radek = list()
        for j in range(sloupce):
            if i == j:
                radek.append(1)
            else:
                radek.append(0)
        matice.append(radek)
    return matice

def vypisMatici(matice):
    for radek in matice:
        for sloupec in radek:
            print(sloupec, end=" ")
        print()
print(vypisMatici(vygenerujMatici(5,5)))