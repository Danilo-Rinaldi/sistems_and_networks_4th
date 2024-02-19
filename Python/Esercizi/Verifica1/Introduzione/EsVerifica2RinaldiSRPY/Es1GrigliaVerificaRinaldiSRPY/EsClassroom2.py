#Un braccio robotico industriale libero di muoversi avanti e indietro lungo una rotaia è impazzito. 
#Ogni secondo si muove scegliendo a caso tra due possibili movimenti: 1 cm in avanti, oppure 1 cm indietro. 
#Non è possibile togliere corrente al robot senza bloccare tutto lo stabilimento, 
#quindi bisogna attendere lo spegnimento che si effettua tutti i fine settimana e oggi purtroppo è lunedì! 
#Il tuo responsabile ti chiede di creare un programma in Python per simulare lo spostamento totale 
#che il robot avrà effettuato dopo 5 interi giorni di pazzia.
#Definisci una funzione che restituisca uno spostamento casuale (+1 o -1).
#Utilizza una list comprehension per creare la  lista contenente tutta la sequenza degli spostamenti casuali.
#Infine calcola la somma degli spostamenti casuali per ottenere lo spostamento complessivo accumulato in 5 giorni.

#random randomchoice gli passo una list e lui pesca dalla lista

import random

def main():

    #giorni = 5

    #sec_in_giorno = 24 * 60 * 60

    #spostamenti = giorni * sec_in_giorno

    spostamenti = 5 * 24 * 60 * 60

    possibili_spostamenti = [-1, 1]

    movimenti = 0

    lista_spostamenti = [random.choice(possibili_spostamenti) for _ in range(spostamenti) ] 

    for mossa in lista_spostamenti:
        movimenti = movimenti + mossa

    print (movimenti)
    
if __name__ == "__main__":
    main()
