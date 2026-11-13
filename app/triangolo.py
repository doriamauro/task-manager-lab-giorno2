#funzione che calcola il perimetro di unq triangolo dato i tre lati usando il modulo funzioni.py 
#che contiene la funzione somma e le altre funzioni matematiche di base
from funzioni import somma

def perimetro_triangolo(lato1, lato2, lato3):
    return somma(somma(lato1, lato2), lato3)

