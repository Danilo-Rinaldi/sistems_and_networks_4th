def main():


    for numero in range (1, 999 + 1):
        
        string = str(numero)

        somma = 0

        for car in string:
            somma = somma + (int(car) * int(car) * int(car))

        if (somma == numero):
            print(f"il numero {numero} è narcisista")


    """for numero in range (1, 1000):
            if (sum([int(cifra)**3 for cifra in str(numero)]) == numero ):
                print(f"Il numero {numero} è narcisista")    
        
    """
    

if __name__ == "__main__":
    main()