osoby = []

def pridej_osobu(jmeno, vek, kategorie):
    osoby.append({"jmeno": jmeno, "vek": vek, "kategorie": kategorie})
    print(f"Osoba {jmeno} byla pridana.")

def odeber_osobu(jmeno):
    for osoba in osoby:
        if osoba["jmeno"] == jmeno:
            osoby.remove(osoba)
            print(f"Osoba {jmeno} byla odebrana.")
            return
    print(f"Osoba {jmeno} nebyla nalezena.")

def vypis_osoby():
    print("Seznam osob:")
    for osoba in osoby:
        print(f"{osoba['jmeno']}, Vek: {osoba['vek']}, Kategorie: {osoba['kategorie']}")

def vyfiltruj_osoby(kategorie):
    filtrovane_osoby = [osoba for osoba in osoby if osoba["kategorie"] == kategorie]
    if filtrovane_osoby:
        print(f"Osoby ve vybrane kategorii '{kategorie}':")
        for osoba in filtrovane_osoby:
            print(f"{osoba['jmeno']}, Vek: {osoba['vek']}, Kategorie: {osoba['kategorie']}")
    else:
        print(f"V kategorii '{kategorie}' nejsou zadne osoby.")

def zpracuj_vyber(vyber):
    if vyber == 0:
        vypis_osoby()
    elif vyber == 1:
        jmeno = input("Zadejte jméno osoby: ")
        vek = int(input("Zadejte věk osoby: "))
        kategorie = input("Zadejte kategorii osoby: ")
        pridej_osobu(jmeno, vek, kategorie)
    elif vyber == 2:
        jmeno = input("Zadejte jméno osoby k odstranění: ")
        odeber_osobu(jmeno)
    elif vyber == 3:
        kategorie = input("Zadejte kategorii pro filtrování osob: ")
        vyfiltruj_osoby(kategorie)
    else:
        print("Neplatný výběr.")

while True:
    print("\nNabídka:")
    print("0...Výpis osob")
    print("1...Přidání osoby")
    print("2...Odebrání osoby")
    print("3...Filtrování osob")
    print("4...Ukončení programu")
    vyber = int(input("Výběr: "))
    if vyber == 4:
        print("Ukončení programu.")
        break
    else:
        zpracuj_vyber(vyber)
