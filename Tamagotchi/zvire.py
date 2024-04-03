class Zvire:
    def __init__(self, jmeno):
        self.spokojenost = 0
        self.jmeno = jmeno
        self.krmeni = 0

    def nakrmit(self):
        self.krmeni+=1

    def pridat_spokojenost(self, hodnota):
        self.spokojenost += hodnota
