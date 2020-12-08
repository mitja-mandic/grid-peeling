from razredi import Tocka, enakomerna_mreza, smer_razlike, naredi_potencno, kvazi_cantor_mreza
import time

def jarvis_march(seznam):
    """Najde konveksno ovojnico danega seznama (seznam objektov razreda točka) in vrne njegovo konveksno ovojnico"""
    zacetna_tocka =  min(seznam, key = lambda tocka: tocka.x) #poiščemo najbolj levo točko
    indeks = seznam.index(zacetna_tocka) 
    l = indeks
    rezultat = []
    rezultat.append(zacetna_tocka)
    while (True):
        #S tako izbiro q nikoli nimamo težav z indeksiranjem - celoštevilsko deljenje nam zagotavlja da ostanemo v rangu velikosti seznama.
        q = (l + 1) % len(seznam)      
        for i in range(len(seznam)):
            if i == l:
                continue
            #Na vsakem koraku preverimo, če "zavijamo v levo". Če so točke kolinearne, vzamemo tisto, ki je najdlje stran.
            d = smer_razlike(seznam[l], seznam[i], seznam[q])
            if d > 0 or (d == 0 and seznam[i].razdalja(seznam[l]) > seznam[q].razdalja(seznam[l])):
                q = i
        l = q
        if l == indeks: #pridemo nazaj na začetek
            break    
        rezultat.append(seznam[q])
    return rezultat

def grid_peel_jarvis(mreza):
    """Izvede postopek grid-peelinga. Kot argument sprejme mrežo - seznam objektov razreda točka."""
    start = time.time()
    ovojnice = {}
    i = 0
    while mreza or len(mreza)>1:
        ch = jarvis_march(mreza)
        nova = [x for x in mreza if x not in ch]
        mreza = nova
        ovojnice[i] = ch
        i += 1
    casovna_zahtevnost = time.time() - start
    return i, ovojnice, casovna_zahtevnost

print(6 % 5)

