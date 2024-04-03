from zvire import Zvire

class Kocka(Zvire):
    def __init__(self, jmeno):
        super().__init__(jmeno)
        self.drbani = 0
    
    def je_nakrmeno(self):
        return self.krmeni>=2

    def play_with_yarn(self):
        self.pridat_spokojenost(1)
