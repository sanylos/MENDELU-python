def seznam_nahodnych_cisel(pocet, start, konec):
    import random
    return [random.randint(start, konec) for x in range(pocet)]

seznam = seznam_nahodnych_cisel(50, -5, 5)
print(seznam)
seznam = list(set(seznam))
print(seznam)