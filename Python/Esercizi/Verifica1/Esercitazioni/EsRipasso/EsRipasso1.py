def main():

    #join

    #prende quello che c'è nella parentesi e lo unisce con il carattere separatore

    str1 = "prima"

    str2 = "seconda"

    str3 = "terza"

    str4 = "quarta"

    str = [str1, str2, str3, str4]

    str1 = "".join(str)

    print(str1)

    #output: primasecondaterzaquarta

    str1 = " ".join(str)

    print(str1)

    #output: prima seconda terza quarta

    #--------------------------------------------------------------------------


    #split 

    # Stringa di esempio
    frase = "Questo è un esempio di split in Python"

    # Dividi la stringa utilizzando lo spazio come delimitatore
    lista_parole = frase.split()

    # Stampa la lista risultante
    print(lista_parole)

    #output: ['Questo', 'è', 'un', 'esempio', 'di', 'split', 'in', 'Python']


    #-----------------------------------------------------------------------------

    # Creazione di un dizionario
    dizionario = {'chiave1': 'valore1', 'chiave2': 'valore2', 'chiave3': 'valore3'}

    # Accesso ai valori tramite la chiave
    valore1 = dizionario['chiave1']
    print("Valore associato a chiave1:", valore1)

    # Aggiunta di una nuova coppia chiave-valore
    dizionario['chiave4'] = 'valore4'

    # Modifica di un valore esistente
    dizionario['chiave2'] = 'nuovo_valore2'

    # Verifica dell'esistenza di una chiave
    if 'chiave3' in dizionario:
        print("La chiave 'chiave3' esiste nel dizionario.")

    # Rimozione di una coppia chiave-valore
    valore_rimosso = dizionario.pop('chiave1')
    print("Valore rimosso associato a chiave1:", valore_rimosso)

    # Iterazione su chiavi e valori
    print("Iterazione su chiavi e valori:")
    for chiave, valore in dizionario.items():
        print(f"Chiave: {chiave}, Valore: {valore}")

    # Ottenere una lista di chiavi e valori
    chiavi = list(dizionario.keys())
    valori = list(dizionario.values())

    # Lunghezza del dizionario (numero di coppie chiave-valore)
    lunghezza_dizionario = len(dizionario)

    # Pulizia del dizionario
    dizionario.clear()

    print("Dizionario dopo le operazioni:", dizionario)

    #-------------------------------------------------------------------

    def scrivi_testo_su_file(nome_file, testo):
        with open(nome_file, 'w') as file:
            file.write(testo)

    def leggi_testo_da_file(nome_file):
        with open(nome_file, 'r') as file:
            testo_letto = file.read()
            return testo_letto

    def scrivi_lista_su_file(nome_file, lista):
        with open(nome_file, 'w') as file:
            for elemento in lista:
                file.write(str(elemento) + '\n')

    def leggi_lista_da_file(nome_file):
        with open(nome_file, 'r') as file:
            lista_letta = [line.strip() for line in file]
            return lista_letta

    def scrivi_dizionario_su_file(nome_file, dizionario):
        with open(nome_file, 'w') as file:
            for chiave, valore in dizionario.items():
                file.write(f"{chiave}: {valore}\n")

    def leggi_dizionario_da_file(nome_file):
        with open(nome_file, 'r') as file:
            dizionario_letto = {}
            for line in file:
                chiave, valore = line.strip().split(': ')
                dizionario_letto[chiave] = valore
            return dizionario_letto

    # Esempio di utilizzo
    with open('testo.txt', 'w') as f:
        scrivi_testo_su_file('testo.txt', 'Questo è un esempio di scrittura di testo su file.')

    with open('testo.txt', 'r') as f:
        testo_letto = leggi_testo_da_file('testo.txt')
        print("Testo letto da file:", testo_letto)

    lista_da_scrivere = ['Elemento 1', 'Elemento 2', 'Elemento 3']
    with open('lista.txt', 'w') as f:
        scrivi_lista_su_file('lista.txt', lista_da_scrivere)

    with open('lista.txt', 'r') as f:
        lista_letta = leggi_lista_da_file('lista.txt')
        print("Lista letta da file:", lista_letta)

    dizionario_da_scrivere = {'chiave1': 'valore1', 'chiave2': 'valore2', 'chiave3': 'valore3'}
    with open('dizionario.txt', 'w') as f:
        scrivi_dizionario_su_file('dizionario.txt', dizionario_da_scrivere)

    with open('dizionario.txt', 'r') as f:
        dizionario_letto = leggi_dizionario_da_file('dizionario.txt')
        print("Dizionario letto da file:", dizionario_letto)





if __name__ == "__main__":

    main()