#dizionario

#il dizionario è una collezione di coppie (chiave: valore) 

#il dizionario non ha indici ma si indicizza per chiave 

#vincolo: la chiave deve essere di un solo tipo
def main():
   
    file = open("rubrica.txt", "r")

    righe = file.readlines()

    file.close()


    print (righe)

    rubrica_mia = {}
    rubrica_prof = {}

# I thought this:
    for riga in righe:
        #restituisce i campi
        campi = riga.split(", ")
        #print (campi[1].replace("\n", ""))
        rubrica_mia[campi[0]] = int (campi[1])

        print(rubrica_mia)


    pass#questo comando non fa niente



    
    

#teacher did this:

    for riga in righe:
        #restituisce i campi
        campi = riga.split(", ")
        #print (campi[1].replace("\n", ""))
        numeroTelefonico = int (campi[1].replace("\n", ""))
        nome = campi[0]
        rubrica_prof[numeroTelefonico] = nome


    print (rubrica_prof)





if __name__ == "__main__":
    main()
