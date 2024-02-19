class Coda:

    def __init__(self):
        self.lista = []

    def is_empty(self):
        if (len(self.lista) == 0):
            return True
        else:
            return False
        
    def enqueue(self, x):
        self.lista.append(x)

    def dequeue(self):
        if (self.is_empty()):
            print("coda vuota")
            return None
        else:
            return self.lista.pop(0)

    def stampa(self):
        print(self.lista)

def main():

    coda = Coda()

    coda.stampa()

    coda.enqueue(1)
    
    coda.stampa()

    coda.enqueue(2)

    coda.stampa()

    coda.enqueue(3)

    coda.stampa()

    coda.dequeue()
    
    coda.stampa()

    coda.dequeue()

    coda.stampa()


if __name__ == "__main__":
    main()

