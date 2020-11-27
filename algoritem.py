#class Tocka:
#
#    def __init__(self, x, y):
#        self.x = x
#        self.y = y
#    
#    def get_x(self):
#        return self.x
#    
#    def get_y(self):
#        return self.y
#    
#    def __eq__(self, other):
#        return self.x == other.x and self.y == other.y
#
#    def __str__(self):
#        return str(self.x) +','+ str(self.y)


def mreza(m,n):
    """
    Vrne seznam vozlišč za mrežo z m-vrsticami in n stolpci.
    Začne v (0,0), točka desno zgoraj je (m-1,n-1)
    """
    return [(i,j) for i in range(m) for j in range(n)]

def kot_med_tockama(tocka1, tocka2):

    if tocka1[1] == tocka2[1]:
        return 0.0
    elif tocka1[0] == tocka2[0]:
        return 90
    else:
        return (tocka2[1] - tocka1[1])/(tocka2[0] - tocka1[0])


def uredi_po_kotu(seznam):
    """
    sprejme seznam točk, ga uredi po kotu glede na x-os.
    """
    prvi = seznam[0]
    return [prvi] + sorted(seznam[1:], key=lambda x: kot_med_tockama(prvi,x))


#LEVO, DESNO, KOLINEARNE = 1,-1,0

def graham_scan(seznam):

    #def cmp(a, b):
    #    return (a > b) - (a < b)

    def ovinek(p, q, r):
        return (q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1])
    
    urejene_tocke = uredi_po_kotu(seznam)
    ovojnica = [] #stack v katerega dodajamo točke

    for tocka in urejene_tocke:

        while len(ovojnica) > 1 and ovinek(ovojnica[-2],ovojnica[-1],tocka) <= 0:
            
            ovojnica.pop()


        ovojnica.append(tocka)

    return ovojnica


mreza = mreza(4,4)
##[print(x) for x in mreza]
#print(uredi_po_kotu(mreza))

#nova_mreza = list(set(mreza) - set(graham_scan(mreza)))

#print(graham_scan(nova_mreza))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def subtract(self, p):
    	return Point(self.x - p.x, self.y - p.y)

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'
    
def distance_sq(p1, p2):
    return (p1.x - p2.x)**2 + (p1.y - p2.y)**2
# calculates the cross product of vector p1 and p2
# if p1 is clockwise from p2 wrt origin then it returns +ve value
# if p2 is anti-clockwise from p2 wrt origin then it returns -ve value
# if p1 p2 and origin are collinear then it returs 0
def cross_product(p1, p2):
	return p1.x * p2.y - p2.x * p1.y
# returns the cross product of vector p1p3 and p1p2
# if p1p3 is clockwise from p1p2 it returns +ve value
# if p1p3 is anti-clockwise from p1p2 it returns -ve value
# if p1 p2 and p3 are collinear it returns 0
def direction(p1, p2, p3):
	return  cross_product(p3.subtract(p1), p2.subtract(p1))


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
            d = direction(seznam[l], seznam[i], seznam[q]) #poiščemo največji levi ovinek, v primeru kolinearnosti vključimo točko, ki je najdlje
            if d > 0 or (d == 0 and distance_sq(seznam[i], seznam[l]) > distance_sq(seznam[q], seznam[l])):
                q = i
        l = q
        if l == indeks: #pridemo nazaj na začetek
            break 
        rezultat.append(seznam[q])

    return rezultat

#print(jarvis_march(mreza))

#tuki sm probu spremenit da se ne navezuje na class Point

def distance_sq(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def cross_product(p1, p2):
	return p1[0] * p2[1] - p2[0] * p1[1]

def direction(p1, p2, p3):
    return cross_product(p3[0]-p1[0], p3[1]-p1[1])

def jarvis_march(seznam):
    zacetna_tocka =  min(seznam, key = lambda tocka: tocka[0]) #poiščemo najbolj levo točko
    indeks = seznam.index(zacetna_tocka)
    
    l = indeks
    rezultat = []
    rezultat.append(zacetna_tocka)
    while (True):
        q = (l + 1) % len(seznam)
        for i in range(len(seznam)):
            if i == l:
                continue
            d = direction(seznam[l], seznam[i], seznam[q]) #poiščemo največji levi ovinek, v primeru kolinearnosti vključimo točko, ki je najdlje
            if d > 0 or (d == 0 and distance_sq(seznam[i], seznam[l]) > distance_sq(seznam[q], seznam[l])):
                q = i
        l = q
        if l == indeks: #pridemo nazaj na začetek
            break 
        rezultat.append(seznam[q])

    return rezultat