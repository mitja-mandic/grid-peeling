from razredi import Tocka, naredi_neenakomerno, smer_razlike, naredi_potencno
import time

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
        nova = [x for x in mreza if x not in ch]
        mreza = nova
        ovojnice[i] = ch
        i += 1
    casovna_zahtevnost = time.time() - start        
    return i, ovojnice, casovna_zahtevnost