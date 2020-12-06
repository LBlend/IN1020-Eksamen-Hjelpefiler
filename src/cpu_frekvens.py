"""
Gitt en portforsinkelse på 5 ps for enhver port, 
hvilken frekvens vil en 1-bits halvadder kunne operere på?
"""

"""
En portforsinkelse på 5 ps trenger en klokkeperiode på 10ps (forutsatt 50%-50%
klokkesignal).
En klokkeperiode på 10ps gir 100 GHz i frekvens
"""

def frekvens(klokkefrekvens_picosekunder):
    # Antar 50% duty cycle
    klokkeperiode = klokkefrekvens_picosekunder * 2
    frekvens_GHz = 1000 / klokkeperiode
    return f'{frekvens_GHz} GHz'


print(frekvens(5))
