with open('Roba.txt', 'r') as file:
    
    lista = []

    for riga in file:

        mini = riga.split()
        for parola in mini:

            lista.append(parola)

    print(lista)
        

    
    