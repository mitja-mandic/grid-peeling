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
