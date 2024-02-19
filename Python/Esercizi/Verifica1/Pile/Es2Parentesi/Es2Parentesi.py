#Dato in input un indirizzo ipv4 e la sua relativa subnet mask 
#controllare se è un indirizzo privato oppure di loopback
#se indirizzo rete? se è valido? stampare tutti gli indirizzi ip disponibili

def push(pila, elemento):
    pila.append(elemento)

def pop(pila):
    if len(pila) == 0:
        x = None 
    else:
        x = pila.pop()
    return x

def main():
    parentesi_aperte = ["{", "[", "("]
    parentesi_chiuse = ["}", "]", ")"]
    dizionario = {"{": "}", "[": "]", "(": ")"}

    string = "{()}"

    pila = []
    errore = False

    posErrore = None

    for poscarattere, carattere in enumerate(string):
        if carattere in parentesi_aperte:
            push(pila, carattere)
        elif carattere in parentesi_chiuse:
            parentesi = pop(pila)
            if parentesi is not None and dizionario[parentesi] != carattere:
                errore = True

                posErrore = poscarattere

                break
            elif parentesi is None:
                errore = True

    if errore or len(pila) > 0:
        print(f"Errore: parentesi non chiuse correttamente qui: {posErrore}")
    else:
        print("Parentesi chiuse correttamente")

if __name__ == "__main__":
    main()
