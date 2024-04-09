def fce(string):
    vstup = string.split()
    camelcaseString = ""
    for word in vstup:
        camelcaseString += word.capitalize()
    return camelcaseString


print(fce("tohle je nejaky camelcase string"))
