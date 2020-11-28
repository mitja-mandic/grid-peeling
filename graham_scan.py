from razredi import Tocka

#sez = [Tocka(i,j) for i in range(4) for j in range(4)]

#def kot_med_tockama(tocka1, tocka2):
#    if tocka1[1] == tocka2[1]:
#        return 0.0
#    elif tocka1[0] == tocka2[0]:
#        return 90
#    else:
#        return (tocka2[1] - tocka1[1])/(tocka2[0] - tocka1[0])

def uredi_po_kotu(seznam):
    prvi = seznam[0]
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
    ovojnica = [] #stack v katerega dodajamo točke

    for tocka in urejene_tocke:
        

        while len(ovojnica) > 1 and ovojnica[-1].smer_razlike(ovojnica[-2], tocka) <= 0:
            
            ovojnica.pop()


        ovojnica.append(tocka)

    return ovojnica

def grid_peel_graham(m, n):
    mreza = [Tocka(i,j) for i in range(m) for j in range(n)]


    ovojnice = {}
    i = 0
    while mreza:
        ch = graham_scan(mreza)
        
        nova = list(set(mreza) - set(ch))
        mreza = nova

        ovojnice[i] = ch
        i += 1
    return i, ovojnice
