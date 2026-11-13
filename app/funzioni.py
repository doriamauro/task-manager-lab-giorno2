#creare delle funzioni matematiche per le quattro operazioni fondamentali
def somma(a, b):
    return a + b

def sottrazione(a, b):
    return a - b

def moltiplicazione(a, b):
    return a * b

def divisione(a, b):
    if b == 0:
        raise ValueError("Impossibile dividere per zero.")
    return a / b

    