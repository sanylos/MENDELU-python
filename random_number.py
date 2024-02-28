def seznam_nahodnych_cisel(pocet, start, konec):
    import random
    return [random.randint(start, konec) for x in range(pocet)]

print(seznam_nahodnych_cisel(50, -5, 5))