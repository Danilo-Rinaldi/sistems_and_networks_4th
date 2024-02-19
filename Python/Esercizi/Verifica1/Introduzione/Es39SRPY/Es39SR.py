#es18
#Scrivi un programma python che permetta all'utente di inserire due numeri. 
#Crea una lista contenente: La somma dei quadrati dei due numeri, il quadrato della somma dei numeri, 
#la differenza tra i quadrati dei due numeri, il quadrato della differenza tra i due numeri. 
#Stampa poi  la lista ottenuta


def main():
    numero1 = float(input("Inserisci il primo numero: "))
    numero2 = float(input("Inserisci il secondo numero: "))

    somma_quadrati = numero1*2 + numero2 #* vuol dire potenza
    quadrato_somma = (numero1 + numero2)**2
    differenza_quadrati = numero1*2 - numero2*2
    quadrato_differenza = (numero1 - numero2)**2

    risultati = [somma_quadrati, quadrato_somma, differenza_quadrati, quadrato_differenza]

    print(f"Lista ottenuta: {risultati}")

if __name__ == "__main__":
    main()