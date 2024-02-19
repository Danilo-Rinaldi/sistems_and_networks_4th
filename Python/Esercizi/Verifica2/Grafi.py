#creare il disegno del grafo a partire dalla matrice di addiacenza con networkX
import networkx as nx
import matplotlib.pyplot as plt

def disegna_grafo_da_matrice_adiacenza(matrice_adiacenza):
    # Creazione del grafo da matrice di adiacenza
    G = nx.from_numpy_matrix(matrice_adiacenza)

    # Disegno del grafo
    nx.draw(G, with_labels=True, font_weight='bold')

    # Mostra il disegno del grafo
    plt.show()

def fromMatriceToDizionario(matrice):    
    return {i: [j for j, n in enumerate(matrice[i]) if n != 0] for i in range(len(matrice))}

# per inizializzare un parametro in caso di assenza nella chiamata della funzione
def prettyPrint(matrice, separatore="\t"):
    for riga in matrice:
        # convertiamo la lista di numeri in lista di stringhe
        riga_str = [str(x) for x in riga]
        print(separatore.join(riga_str))

def main():
    """Questa è la prima versione"""
    print("\n\n PRIMA VERSIONE \n\n")

    collegamenti = {0: [2, 3], 1: [2, 4], 2: [0, 1, 3], 3: [0, 2, 4], 4: [1, 3]}

    n = len(collegamenti)
    matrice = [[0] * n for _ in range(n)]

    # ciclo su dizionario su chiave e su valore in parallelo
    for k, v in collegamenti.items():
        for h in v:
            matrice[k][h] = 1

    # disegna_grafo_da_matrice_adiacenza(matrice)

    # prettyPrint(matrice, " ")

    print(fromMatriceToDizionario(matrice))



    exit()

    print(f"\t", end="")

    for host in collegamenti:
        print(f"{host}\t", end="")

    print(f"\n", end="")

    for host in collegamenti:
        
        print(f"\n\n{host}", end = "")

        n = 0

        for n in range(0, len(collegamenti)):

            if n in collegamenti[host]:
                print("\t1", end="")
            else:
                print("\t0", end="")


    

    

    

    #Questa è la seconda versione

    print("\n\n SECONDA VERIONE \n\n")

    collegamenti = {0: [2, 3], 1: [0, 2, 3, 4], 2: [0, 1, 3], 3 : [0, 2, 4], 4 : [1, 3]}

    print(f"\t", end="")

    for host in collegamenti:
        print(f"{host}\t", end="")

    print(f"\n", end="")

    k = 0

    for host in collegamenti:
        
        print(f"\n\n{host}", end = "")

        n = 0

        k += 1

        for n in range(0, len(collegamenti)):



            if n + 1 == k:
                print("\t*", end="")
            elif n in collegamenti[host]:
                print("\t1", end="")
            elif n not in collegamenti[host]:
                print("\t0", end="")

    



    #Questa è la terza versione
                
    print("\n\n TERZA VERIONE \n\n")

    collegamenti = {0: [2, 3], 1: [2, 4], 2: [0, 1, 3], 3 : [0, 2, 4], 4 : [1, 3]}

    print(f"\t", end="")

    for host in collegamenti:
        print(f"{host}\t", end="")

    print(f"\n", end="")

    k = 0

    for host in collegamenti:
        
        print(f"\n\n{host}", end = "")

        n = 0

        k += 1

        for n in range(0, len(collegamenti)):



            if n + 1 <= k:
                print("\t*", end="")
            elif n in collegamenti[host]:
                print("\t1", end="")
            elif n not in collegamenti[host]:
                print("\t0", end="")

                
        



if __name__ == "__main__":

    main()