from razredi import Tocka, naredi_neenakomerno, smer_razlike, naredi_potencno
import time
#class Point:
#    def __init__(self, x, y):
#        self.x = x
#        self.y = y
#
#    def subtract(self, p):
#    	return Point(self.x - p.x, self.y - p.y)
#
#    def __str__(self):
#        return '(' + str(self.x) + ', ' + str(self.y) + ')'
#
#def distance_sq(p1, p2):
#    return (p1.x - p2.x)**2 + (p1.y - p2.y)**2
# calculates the cross product of vector p1 and p2
# if p1 is clockwise from p2 wrt origin then it returns +ve value
# if p2 is anti-clockwise from p2 wrt origin then it returns -ve value
# if p1 p2 and origin are collinear then it returs 0
#
#def cross_product(p1, p2):
#	return p1.x * p2.y - p2.x * p1.y
#
#
#def direction(p1, p2, p3):
#	return  cross_product(p3.subtract(p1), p2.subtract(p1))
#
# returns the cross product of vector p1p3 and p1p2
# if p1p3 is clockwise from p1p2 it returns +ve value
# if p1p3 is anti-clockwise from p1p2 it returns -ve value
# if p1 p2 and p3 are collinear it returns 0
def jarvis_march(seznam):
    zacetna_tocka =  min(seznam, key = lambda tocka: tocka.x) #poiščemo najbolj levo točko
    indeks = seznam.index(zacetna_tocka)
    
    l = indeks

    rezultat = []
    rezultat.append(zacetna_tocka)

    while (True):

        q = (l + 1) % len(seznam)
        
        for i in range(len(seznam)):
            if i == l:
                continue
            
            d = smer_razlike(seznam[l], seznam[i], seznam[q])
            #d = seznam[i].smer_razlike(seznam[l],  seznam[q]) #poiščemo največji levi ovinek, v primeru kolinearnosti vključimo točko, ki je najdlje

            #print(d)
            if d > 0 or (d == 0 and seznam[i].razdalja(seznam[l]) > seznam[q].razdalja(seznam[l])):
                q = i
        l = q
        if l == indeks: #pridemo nazaj na začetek
            break 
    
        rezultat.append(seznam[q])

    return rezultat

def grid_peel_jarvis_enakomerna(m, n):
    start = time.time()
    mreza = [Tocka(i,j) for i in range(m) for j in range(n)]

    ovojnice = {}
    i = 0
    while mreza or len(mreza)>1:

        ch = jarvis_march(mreza)
        
        #print(ch)
        nova = [x for x in mreza if x not in ch]
        mreza = nova
        ovojnice[i] = ch
        i += 1
    
    casovna_zahtevnost = time.time() - start
    return i, ovojnice, casovna_zahtevnost

def grid_peel_jarvis_potencna(m, n):
    start = time.time()
    mreza = naredi_potencno(m, n)

    ovojnice = {}
    i = 0
    while mreza or len(mreza)>1:

        ch = jarvis_march(mreza)
        
        #print(ch)
        nova = [x for x in mreza if x not in ch]
        mreza = nova
        ovojnice[i] = ch
        i += 1
    casovna_zahtevnost = time.time() - start        
    return i, ovojnice, casovna_zahtevnost


#def grid_peel_jarvis_neenakomerna(stevilo_tock):
#    mreza  = naredi_neenakomerno(stevilo_tock)
#    
#    ovojnice = {}
#    i = 0
#    while mreza:
#        ch = jarvis_march(mreza)
#        
#        nova = list(set(mreza) - set(ch))
#        mreza = nova
#
#        ovojnice[i] = ch
#        i += 1
#    return i, ovojnice

#print(grid_peel_jarvis_enakomerna(50,50))