#Permettere all'utente di inserire due numeri qualsiasi, creare un dizionario dove ci si salva la media
#matematica e la media geometrica dei due numeri. Stampa poi il dizionario

def main():
    numero1 = float(input("Inserisci il primo numero: "))
    numero2 = float(input("Inserisci il secondo numero: "))

    media_matematica = (numero1 + numero2) / 2
    if numero1 < 0 or numero2 < 0:
        print("La media geometrica ha bisongo di numeri non negativi")
    else:
        media_geometrica = (numero1 * numero2)**0.5

    risultati = {"Media Matematica": media_matematica, "Media Geometrica": media_geometrica}

    print("Dizionario:", risultati)

if __name__ == "__main__":
    main()