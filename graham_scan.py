from razredi import Tocka, enakomerna_mreza, smer_razlike, naredi_potencno, kvazi_cantor_mreza
import time
from mpl_toolkits.mplot3d import Axes3D

def uredi_po_kotu(seznam):
    """Seznam uredi po naraščajočem kotu med točkama, glede na x-os. Sprejme seznam objektov razreda Tocka
    """

    prvi = min(seznam, key = lambda tocka: (tocka.x, tocka.y))
    return [prvi] + sorted(seznam[1:], key=lambda x: prvi.kot_med_dvema(x))

def graham_scan(seznam):
    """Najde konveksno ovojnico dane množice (seznam objektov razreda Tocka)."""
    urejene_tocke = uredi_po_kotu(seznam) #najprej točke uredimo po kotu.
    ovojnica = [] #stack v katerega dodajamo točke

    for tocka in urejene_tocke:
        """če je v ovojnici več kot ena točka, vzamemo zadnji dve točki v ovojnici in prvo iz urejenega seznama. Preverimo kot med njimi.
        Če zavijamo v desno (vektorski produkt vektorjev, ki imajo začetek v zadnji točki ovojnice in konec v predzadnji točki ovojnice oz. prvi točki seznama je nenegativen)
        točko izločimo. Sicer jo dodamo v ovojnico. Ko pregledamo vse urejene točke, smo zaključili.
        """
        while len(ovojnica) > 1 and smer_razlike(ovojnica[-2], ovojnica[-1], tocka) >= 0:           
            ovojnica.pop()
        ovojnica.append(tocka)
    return ovojnica

def grid_peel_graham(mreza):
    """Izvede grid-peeling na seznamu objektov razreda Tocka"""
    start = time.time()
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
