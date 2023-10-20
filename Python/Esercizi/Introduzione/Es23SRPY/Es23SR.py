#p55 n 10

def main():

    voti = [10, 8, 6, 7, 8, 7, 6, 8, 9, 10]

    print(f"{voti[1 : -1]}")

    voti[3] = 10

    print(f"{voti[0 : 3]}")

    #oppure

    lista = []
    k = 0

    while True:
        voto = int(input("inserisci un voto (almeno 6) o -1 per interrompere"))
        if (voto < 0 and k >= 6):
            k = k - 1
            break
        elif(voto >= 0):
            lista.append(voto)
        k = k + 1
    
    print(f"{lista[1 : -1]}")


if __name__ == "__main__":
    main()