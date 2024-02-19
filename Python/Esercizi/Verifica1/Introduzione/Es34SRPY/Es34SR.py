#dizionario

#il dizionario è una collezione di coppie (chiave: valore) 

#il dizionario non ha indici ma si indicizza per chiave 

#vincolo: la chiave deve essere di un solo tipo
def main():
   
    dizionario = {"nome": "Mario", "cognome": "Rossi"}

    lista = ["Mario", "Rossi"] #praticamente io creo una lista ma alla quale dico il nome della posizione quindi al posto di 1 2 3 potrò dire io come si chiamano quindi nome cognome datanascita

    print(dizionario["nome"])
    print(dizionario["cognome"])

    #è un assegnamento quindi se non è presente data nascita allora crea un elemento nuovo 
    dizionario["data nascita"] = "01/01/1900"
    dizionario["nome"] = "Luca"

    dizionario ["età"] = 123

    print(dizionario)

    #ciclo for su dizionari

    for chiave in dizionario:
        print (f"Chiave: {chiave} valore: {dizionario[chiave]}")

    rubrica = {27982392: "Mario Rossi", 343434839: "Alice Verdi", 39204920: "Simone Gialli", 239284238429: "Marco azzurri"}

    for chiave in rubrica:
        print()#...



if __name__ == "__main__":
    main()
