"""

Creare una classe Contatto:

La classe dovrebbe avere attributi come nome, cognome, numero di telefono, e-mail, ecc.
Implementare un metodo __str__ per rappresentare il contatto come una stringa leggibile.
Creare una classe GestoreContatti:

La classe dovrebbe avere una lista di oggetti Contatto.
Implementare metodi per aggiungere un nuovo contatto, visualizzare tutti i contatti e cercare un contatto per nome o cognome.
Scrittura e lettura da un file:

Implementare metodi nella classe GestoreContatti per salvare tutti i contatti su un file e caricare i contatti da un file. Utilizza il formato di file che preferisci (ad esempio, CSV, JSON, ecc.).
Esercizio principale:

Creare un programma principale che istanzia la classe GestoreContatti, aggiunge alcuni contatti, salva i contatti su un file, carica i contatti da un file, e infine stampa tutti i contatti.

"""

class Contatto():

    def __init__(self, nome, cognome, telefono):

        self.nome = nome
        self.cognome = cognome
        self.telefono = telefono

    def print_contatto(self):

        return ("\n" + self.nome + " " +  self.cognome + ":\n" +  str(self.telefono) + "\n")
    

class GestoreContatti():

    def __init__(self):
        self.lista = []
    
    def addContatto(self, contatto):
        
        self.lista.append(contatto)

    def printContatti(self):

        cnt = ""

        for contatto in self.lista:

            cnt = cnt + contatto.print_contatto()

        return cnt

    def look_by_name(self, nominativo):

        for contatto in self.lista:

            if nominativo in contatto.nome:

                return contatto
            
    def carica_in_file(self, file):

        with open(file, 'w') as file:
            
            file.write(self.printContatti())
            
    def look_by_surname(self, nominativo):

        for contatto in self.lista:

            if nominativo in contatto.cognome:

                return contatto

def main():

    gestore = GestoreContatti()

    c1 = Contatto("Danilo", "Rinaldi", 3703763583)
    c2 = Contatto("Eleonora", "Siddi", 3496144758)
    c3 = Contatto("Thomas", "Turbato", 2322074990)

    print(c1.print_contatto())
    print(c2.print_contatto())
    print(c3.print_contatto())

    print("----------------------------------------------")

    gestore.addContatto(c1)
    gestore.addContatto(c2)
    gestore.addContatto(c3)

    print(gestore.printContatti())

    print("--------------------------------------------")

    contatto_da_trovare = gestore.look_by_name("Danilo")

    print(contatto_da_trovare.print_contatto())

    print("--------------------------------------------------------")

    gestore.carica_in_file("contatti.txt")




    

if __name__ == "__main__":

    main()