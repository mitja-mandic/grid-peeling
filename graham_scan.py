from razredi import Tocka, naredi_neenakomerno, smer_razlike, naredi_potencno
import time

#sez = [Tocka(i,j) for i in range(4) for j in range(4)]

#def kot_med_tockama(tocka1, tocka2):
#    if tocka1[1] == tocka2[1]:
#        return 0.0
#    elif tocka1[0] == tocka2[0]:
#        return 90
#    else:
#        return (tocka2[1] - tocka1[1])/(tocka2[0] - tocka1[0])

def uredi_po_kotu(seznam):
    prvi = min(seznam, key = lambda tocka: (tocka.x, tocka.y))
    return [prvi] + sorted(seznam[1:], key=lambda x: prvi.kot_med_dvema(x))

#[print(x) for x in uredi_po_kotu_classi(sez)]


#def uredi_po_kotu(seznam):
#    """
#    sprejme seznam točk, ga uredi po kotu glede na x-os.
#    """
#    prvi = seznam[0]
#    return [prvi] + sorted(seznam[1:], key=lambda x: kot_med_tockama(prvi,x))


#LEVO, DESNO, KOLINEARNE = 1,-1,0

def graham_scan(seznam):

    #def cmp(a, b):
    #    return (a > b) - (a < b)

    #def ovinek(p, q, r):
    #    return (q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1])
    
    urejene_tocke = uredi_po_kotu(seznam)
    #print(urejene_tocke)

    ovojnica = [] #stack v katerega dodajamo točke

    for tocka in urejene_tocke:

        while len(ovojnica) > 1 and smer_razlike(ovojnica[-2], ovojnica[-1], tocka) >= 0:
            
            ovojnica.pop()

        ovojnica.append(tocka)

    return ovojnica

def grid_peel_graham_enakomerna(m, n):
    start = time.time()
    mreza = [Tocka(i,j) for i in range(m) for j in range(n)]

    ovojnice = {}
    i = 0
    while mreza or len(mreza) > 1:
        ch = graham_scan(mreza)
        #print(ch)
        nova = [x for x in mreza if x not in ch]
        mreza = nova
        i += 1
        ovojnice[i] = ch
    casovna_zahtevnost = time.time() - start 
    return i, ovojnice, casovna_zahtevnost

def grid_peel_graham_potencna(m, n):
    start = time.time()
    mreza = naredi_potencno(m, n)

    ovojnice = {}
    i = 0
    while mreza or len(mreza) > 1:
        ch = graham_scan(mreza)
        #print(ch)
        nova = [x for x in mreza if x not in ch]
        mreza = nova
        i += 1
        ovojnice[i] = ch
    casovna_zahtevnost = time.time() - start 
    return i, ovojnice, casovna_zahtevnost

#print(grid_peel_graham_enakomerna(50, 50))
def tabela_graham_enakomerna(m,n):
    return [grid_peel_graham_enakomerna(i,j)[2] for i in range(m) for j in range(n)]

#print(tabela(20,20))
