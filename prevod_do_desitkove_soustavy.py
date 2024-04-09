def preved_na_desitkove(vstup, soustava):
    s=0
    for x in vstup:
        if x >= "0" and x <= "9":
            s = s * soustava + ord(x) - ord("0")
        else:
            s = s * soustava + ord(x) - ord("a") + 10
    return s

print(preved_na_desitkove("100", 16))