def cetnosti(vstup):
    pocty = dict()
    for x in vstup:
        if x in pocty:
            pocty[x]+=1
        else:
            pocty[x]=1
    return pocty

print(cetnosti("neco neco"))