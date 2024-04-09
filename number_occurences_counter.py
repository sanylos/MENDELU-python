def fce(seznam):
    cetnosti = dict()
    for klic in seznam:
        if klic in cetnosti:
            cetnosti[klic] += 1
        else:
            cetnosti[klic] = 1
    return cetnosti


print(fce([1, 2, 3, 4, 5, 2, 2]))
