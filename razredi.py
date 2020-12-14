import math

class Tocka:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def kot_med_dvema(self, other):
        """Kot med dvema točkama v radianih"""        
        if self.x != other.x:
            return math.atan((self.y - other.y) / (self.x - other.x))
        else:
            return math.pi/2
    
    #če je vektorski produkt pozitiven je kot med vektorjema manjši od Pi
    #če je negativen je manjši od pi
    #če je 0 sta vektorja kolinearna

    def vektorski_produkt(self, other): 
        """Vektorski produkt, kjer je tretja komponenta obeh vektorjev enaka nič (smo v ravnini)"""
        return self.x * other.y - self.y * other.x

    def razlika(self, other):
        """Razlika dveh točk"""
        return Tocka(self.x - other.x, self.y - other.y)

    def razdalja(self, other):
        """Kvadrat klasične razdalje med točkama"""
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2
    def kot_atan(self, other):
        return math.atan2(self.y-other.y,self.x-other.x)

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __repr__(self):
        return 'T(' + str(self.x) + ', ' + str(self.y) + ')'


def smer_razlike(p,q,r):
    return p.razlika(q).vektorski_produkt(r.razlika(q))


def enakomerna_mreza(m,n):
    """Vrne mxn mrežo z enakomernimi razmiki
    """
    return [Tocka(i,j) for i in range(m) for j in range(n)]

def naredi_potencno(m, n):
    """Mreža mxn, kjer se razmiki povečujejo eksponentno z osnovo 2.
    """
    return [Tocka(2**i,2**j) for i in range(m) for j in range(n)]

def kvazi_cantor_mreza(n):
    """Mreža po vzoru literature. Vsaka naslednja ovojnica je dolžine 3 ** i, argument je največja potenca 3.
    (vsaka stranica je točno trikrat daljša od prejšnje, zato Cantorjeva).
    Na vsaki stranici imamo na koncu 2n točk, vseh vozlišč je torej 4 n ** 2.
    """
    
    sez = [0,3]
    for i in range(1,n):
        nasl_dol = sez[0] - 3 ** i
        nasl_gor = sez[-1] + 3 ** i
        sez.append(nasl_gor)
        sez = [nasl_dol] + sez
    return [Tocka(i,j) for i in sez for j in sez]