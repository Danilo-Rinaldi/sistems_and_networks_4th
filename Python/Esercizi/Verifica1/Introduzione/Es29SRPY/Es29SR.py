#list comprension
#p 73 n 20

def main():

    max = 10

    power = [[k * i for i in range (1, max + 1)] for k in range (1, max + 1)]

    
    for k, tabellina in enumerate(power):
        #tabellina == lista 
        #power == lista di liste
        #enumerate = funzione che numera le liste e ritorna indice e elemento

        print (f"Tabellina del {k + 1}: {tabellina}")

    file = open("Data.txt", "w")

    for tabellina in power:
        file.write(f"{tabellina}\n")

    file.close()


if __name__ == "__main__":
    main()

