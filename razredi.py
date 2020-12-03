import random

class Tocka:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def kot_med_dvema(self, other):
        if self.x != other.x:
            return (self.y - other.y) / (self.x - other.x)
        else:
            return 90
    
    #če je vektorski produkt pozitiven je kot med vektorjema manjši od Pi
    #če je negativen je manjši od pi
    #če je 0 sta vektorja kolinearna

    def vektorski_produkt(self, other): 
        return self.x * other.y - self.y * other.x

    def razlika(self, other):
    	return Tocka(self.x - other.x, self.y - other.y)

    def razdalja(self, other):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __repr__(self):
        return 'T(' + str(self.x) + ', ' + str(self.y) + ')'


def smer_razlike(p,q,r):
    return p.razlika(q).vektorski_produkt(r.razlika(q))

def naredi_neenakomerno(st_tock, zgornja_meja):
    seznam = sorted(random.sample(range(zgornja_meja),st_tock))
    return [Tocka(i,j) for i in seznam for j in seznam]

def naredi_potencno(m, n):
    return [Tocka(2**i,2**j) for i in range(m) for j in range(n)]


#class Mreza:
#    def __init__(self, m, n):#, vrsta):
#        self.m = m 
#        self.n = n
#        self.vrsta = str(vrsta)
#    
#    def mreza(self):
#        return [Tocka(i,j) for i in range(self.m) for j in range(self.n)]