from razredi import Tocka

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

            d = seznam[i].smer_razlike(seznam[l],  seznam[q]) #poiščemo največji levi ovinek, v primeru kolinearnosti vključimo točko, ki je najdlje
            if d > 0 or (d == 0 and seznam[i].razdalja(seznam[l]) > seznam[q].razdalja(seznam[l])):
                q = i
        l = q
        if l == indeks: #pridemo nazaj na začetek
            break 
    
        rezultat.append(seznam[q])

    return rezultat

def grid_peel_jarvis(m, n):
    mreza = [Tocka(i,j) for i in range(m) for j in range(n)]

    ovojnice = {}
    i = 0
    while mreza:
        ch = jarvis_march(mreza)
        
        nova = list(set(mreza) - set(ch))
        mreza = nova

        ovojnice[i] = ch
        i += 1
    return i, ovojnice

#test = grid_peel_jarvis(3,3)
