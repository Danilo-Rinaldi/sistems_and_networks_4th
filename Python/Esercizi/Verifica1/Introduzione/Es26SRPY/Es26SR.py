#list comprension
#lista con i primi 5 quadrati perfetti

import random

def main():
    quadrati = [i*i for i in range (1, 6)]
    print(quadrati)

    numeri_interi =[i for i in range(1, 10 + 1)]
    print(numeri_interi)

    stringhe = ["computer", "camomilla", "facile"]

    stringhe_c = [parola for parola in stringhe if parola[0] == "c"]

    print(stringhe)
    print(stringhe_c)

    voti = [random.randint(2, 10) for _ in range(1, 10 + 1)]#I can use the underscore if we use a variable that we actually don't use
    voti = [random.randint(2, 10) for i in range(1, 10 + 1)]
    print(voti)

    voti_insufficienti = [voto for voto in voti if voto< 6]
    print(voti_insufficienti)



if __name__ == "__main__":
    main()

