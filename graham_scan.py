from razredi import Tocka, naredi_neenakomerno, smer_razlike, naredi_potencno, kvazi_cantor_mreza
import time
from mpl_toolkits.mplot3d import Axes3D



def uredi_po_kotu(seznam):
    prvi = min(seznam, key = lambda tocka: (tocka.x, tocka.y))
    return [prvi] + sorted(seznam[1:], key=lambda x: prvi.kot_med_dvema(x))

def graham_scan(seznam):   
    urejene_tocke = uredi_po_kotu(seznam)
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
        nova = [x for x in mreza if x not in ch]
        mreza = nova
        ovojnice[i] = ch
        i += 1
    casovna_zahtevnost = time.time() - start 
    return i, ovojnice, casovna_zahtevnost

def grid_peel_graham_potencna(m, n):
    start = time.time()
    mreza = naredi_potencno(m, n)
    ovojnice = {}
    i = 0
    while mreza or len(mreza) > 1:
        ch = graham_scan(mreza)
        nova = [x for x in mreza if x not in ch]
        mreza = nova
        ovojnice[i] = ch
        i += 1
    casovna_zahtevnost = time.time() - start 
    return i, ovojnice, casovna_zahtevnost

def tabela_graham_enakomerna(m,n):
    return [grid_peel_graham_enakomerna(i,j)[2] for i in range(m) for j in range(n)]

def grid_peel_graham_cantor(n):
    start = time.time()
    mreza = kvazi_cantor_mreza(n)
    ovojnice = {}
    i = 0
    while mreza or len(mreza) > 1:
        ch = graham_scan(mreza)
        nova = [x for x in mreza if x not in ch]
        mreza = nova
        ovojnice[i] = ch
        i += 1
    casovna_zahtevnost = time.time() - start 
    return i, ovojnice, casovna_zahtevnost