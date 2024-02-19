def main ():
    file = open("covid-19_gen1.txt", "r")
    righe = file.readlines()
    file.close()

    testo = ""

    contatori = {"A": 0, "C": 0, "G": 0, "T": 0}

    for riga in righe:

        testo = testo + riga

    posizione = int (0)

    for carattere in testo:
        posizione += 1
        if (carattere == "A"):
            contatori["A"] += 1
        elif (carattere == "C"):
            contatori["C"] += 1
        elif (carattere == "G"):
            contatori["G"] += 1
        elif (carattere == "T"):
            contatori["T"] += 1
        stringa = testo[posizione - 1 : posizione + 11]
        if (stringa == "ATGTTTGTTTTT"):

            print(f"I found Spikes in {posizione}")

    print(contatori)


if __name__ == "__main__":
    main()