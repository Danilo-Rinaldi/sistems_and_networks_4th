#Dato in input un indirizzo ipv4 e la sua relativa subnet mask 
#controllare se è un indirizzo privato oppure di loopback
#se indirizzo rete? se è valido? stampare tutti gli indirizzi ip disponibili

def push(pila, elemento):
    pila.append(elemento)

def pop (pila):
    x = pila.pop()
    return x

def main():

    pila = [1, 2, 3, 4]

    push(pila, 10)

    print(pila)

    x = pop(pila)

    print(x)

    print(pila)

    



if __name__ == "__main__":
    main()