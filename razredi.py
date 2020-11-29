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

    def smer_razlike(self, other, another):
        
        vekt_p = Tocka(self.x - other.x, self.y - other.y).vektorski_produkt(Tocka(another.x - other.x, another.y - other.y))
        
        if vekt_p > 0:
            return 1
        elif vekt_p < 0:
            return -1
        else:
            return 0
    
    def razdalja(self, other):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'


#p = Tocka(0,0)
#q = Tocka(1,0)
#r = Tocka(2,1)
#
#print(q.smer_razlike(p,r))

#nevem če ta razred zares rabimo
#class Mreza:
#    def __init__(self, m, n):#, vrsta):
#        self.m = m 
#        self.n = n
#    #    self.vrsta = str(vrsta)
#    
#    def mreza(self):
#        return [Tocka(i,j) for i in range(self.m) for j in range(self.n)]

#grid = Mreza(2,2)
#
#print(grid.mreza())