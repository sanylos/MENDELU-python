def cetnosti(vstup):
    pocty = dict()
    for x in vstup:
        if x in pocty:
            pocty[x]+=1
        else:
            pocty[x]=1
    return pocty

def serazene(slovnik):
    serazenyList = sorted(slovnik.items(), key=lambda x:x[1], reverse=True)
    return serazenyList

print(serazene(cetnosti("dasd fdsfsd")))