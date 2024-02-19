#fai u programma che chiede all'utente due numeri il programma deve stampare una stringa con dentro i due numeri decrescenti 
#dovete usare una sola print in tutto il codice

def main():

    list = [4, 100, 3, 5, "ciao", print]#list

    #cicle for C-style

    for i in range (0, len(list)):
        print(f"the element {i} of the list is {list[i]} ")

    #                 /\
    # we can't use it II

    print("\n")
    
    #cicle for python-style

    for i in list:
        print(f"Element: {i}")


if __name__ == "__main__":
    main()