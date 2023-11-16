#dizionario

#il dizionario è una collezione di coppie (chiave: valore) 

#il dizionario non ha indici ma si indicizza per chiave 

#vincolo: la chiave deve essere di un solo tipo
def Prodotto(a, b):
    return a * b

def Somma(a, b):
    return a + b

def Sottrazione(a, b):
    return a - b

def Divisione(a, b):
    return a / b

def main():

    dizionario = {"+": Somma, "*": Prodotto, "-": Sottrazione, "/": Divisione}

    operazione = input("inserisci una operazione tra + per la somma e * per il prodotto - pr la sottrazione e / per la divisione")

    a = float (input ("inserisci il primo numero"))

    b = float (input ("inserisi il secondo numero"))


    print(dizionario[operazione](a, b))  #io prendo la chiave con le quadre e gli posso passare dei parametri con le tonde

    #dizionario di operazione è di tipo funzione quindi è come se scrivessi "funzione"
    # poi io gli passo (a, b) e quindi esce "funzione" (a, b)  





if __name__ == "__main__":
    main()
