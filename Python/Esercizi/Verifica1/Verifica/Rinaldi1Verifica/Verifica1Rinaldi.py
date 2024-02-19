class Testo():

    def __init__(self, testo):
        self.testo = testo
    
    def calcola_numero_char(self):

        """Funzione che calcola il numero di caratteri nella stringa"""
        """
        Corretto: return len(self.testo)
        """
        k = 0
        for carattere in self.testo:
            k = k + 1
        return k
    
    def parole_in_lista(self):

        """F. che ritorna una lista con le parole nel 'testo' """

        """
        corretto: self.testo.split(" ")
        """

        lista = []

        lista = self.testo.split() #uso la split per dividere le parole

        return lista

    def lista_con_lunghezza_numeri(self):
        
        """
        
        corretto:

        lista = self.parole_in_lista()

        return [len(parola) for parola in lista]
        
        """
        
        lista = []
        for k in range (0, len(self.testo)):

            lista.append(k)
        return lista

    def ricerca_parola(self, word):

        """
        
        return parola in self.parole_in_lista()

        """

        tro = False
        parole = []
        parole = self.parole_in_lista()
        if word in parole:
            tro = True
        return tro
    
    def salvataggio(self):

        """corretto"""

        with open("Testo.txt", "w") as file: #creo un oggetto chiamato open e solo dopo posso scriverci

            file.write(self.testo)

    """
    
    Parte facoltativa:

    def frequenze_parole (self):
    
        frequenze = {}

        for parola in self.parole_in_lista():
        
            if parola in frequenze:
            
                frequenze di parola += 1
                
            else:
            
                frequenze[parola] = 1

        return frequenze
    
    """
    




def main():

    str = Testo ("Stringa giorgiaaa")

    print(str.calcola_numero_char())
    print(str.parole_in_lista())
    print(str.lista_con_lunghezza_numeri())
    if (str.ricerca_parola("giorgiaaa")):
        print("trovato")
    else:
        print("non trovato")
    str.salvataggio()

    

    

if __name__ == "__main__":
    main()