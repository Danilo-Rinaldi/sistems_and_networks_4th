
def CercaContatto(nome, rubrica):
    for numtel in rubrica:
        if rubrica[numtel] == nome:
            return numtel
    return None

def CercaNumTell(num, rubrica):
    if num in rubrica:
        return rubrica[num]
    else:
        return None

def main():
    file = open("rubrica.csv", "r")
    righe = file.readlines()
    file.close()
    rubrica = {}

    for riga in righe:
        #restituisce i campi
        campi = riga.split(", ")

        #sostiuisco il carattere \n con uno a scelta
        numTell = int(campi[1].replace("\n", ""))
        nome = campi[0]

        #uso numTell come chiave
        rubrica[numTell] = nome
    print(rubrica)

if __name__ == "__main__":
    main()