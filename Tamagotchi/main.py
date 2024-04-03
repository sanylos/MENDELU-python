from pes import Pes
from kocka import Kocka
from ptak import Ptak

pes = Pes('cokl')
kocka = Kocka('kocka')
ptak = Ptak('ftak')

pes.play_fetch()
kocka.play_with_yarn()
ptak.sing()

print("Pes:", pes.spokojenost)
print("Kocka:", kocka.spokojenost)
print("Ptak:", ptak.spokojenost)
