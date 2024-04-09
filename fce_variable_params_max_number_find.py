def fce(*args, **kwargs):
    max = -99999
    for i, x in enumerate(args):
        if x > max:
            max = x
            vystup = i+1
    for klic, hodnota in kwargs.items():
        if hodnota > max:
            max = hodnota
            vystup = klic
    return vystup


# Vypise pozici nejvyssiho cisla nebo klic nejvyssi hodnoty klice
print(fce(1, 7, 4, 5, a=2, c=6))
