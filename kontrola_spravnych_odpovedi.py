spravne_odpovedi = {
    "popis postupu": 4,
    "činnosti":1,
    "činnost":1,
    "aktivity":1,
    "informace":1,
    "posloupnost příkazů":3
}

def zjisti_pocet_bodu(vstup,kontrola,max):
    s = 0
    for slovo,body in kontrola.items():
        if slovo in vstup:
            s=s+body
    return s

print(zjisti_pocet_bodu("Algoritmus je přesný popis postupu činnosti",spravne_odpovedi,5))