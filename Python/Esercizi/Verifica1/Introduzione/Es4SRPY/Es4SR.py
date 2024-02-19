#fai u programma che chiede all'utente due numeri il programma deve stampare una stringa con dentro i due numeri decrescenti 
#dovete usare una sola print in tutto il codice

def main():

    a = input ("give me the first number")
    b = input ("give me the second number")

    #a, b  = 4, 5 multiple asignament

    if b > a:
        a, b= b, a

    print (f"{a} {b}")



if __name__ == "__main__":
    main()