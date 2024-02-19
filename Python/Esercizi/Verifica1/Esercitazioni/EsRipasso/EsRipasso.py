def main():

    pass #ripassare come si scrive su file

    dizNumLet = {}

    dizLetNum = {}

    letters = "abcdefghijklmnopqrstuvwxyz "
    #print(len(letters))
    for posizione, lettera in enumerate(letters):
        #print(f"{posizione}: {lettera}")
        dizNumLet[posizione] = lettera
        dizLetNum[lettera] = posizione

    #print(dizLetNum)
    #print(dizNumLet)


    testo_chiaro = "parola parola marte"
    chiave = "iti s fus jgbdm fi jd"
    testo_criptato = ""

    for lettera_testo, lettera_chiave in zip(testo_chiaro, chiave):
        #print(f"{dizLetNum[lettera_testo]}: {dizLetNum[lettera_chiave]}")

        numero = (dizLetNum[lettera_chiave] + dizLetNum[lettera_testo])% len(dizLetNum)

        testo_criptato = testo_criptato + dizNumLet[numero]


    print(testo_criptato)

    testo_tradotto = ""

    print(f"il testo '{testo_chiaro}' è diventato grazie a '{chiave}': '{testo_criptato}'")

    for lettera_cripta, lettera_chiave in zip(testo_criptato, chiave):
        #print(f"{dizLetNum[lettera_testo]}: {dizLetNum[lettera_chiave]}")

        numero = (dizLetNum[lettera_cripta] - dizLetNum[lettera_chiave])% len(dizLetNum)

        testo_tradotto = testo_tradotto + dizNumLet[numero]

    print(testo_tradotto)
    print(f"il testo '{testo_criptato}' è diventato grazie a '{chiave}': '{testo_tradotto}'")


        
#ripassate join split funzioni che non abbiamo mai usato che ci inserirà nel testo
    
    #tutto sulle classi i dizionari ecc funzioni main ecc sfrittura lettura file 

        


if __name__ == "__main__":

    main()