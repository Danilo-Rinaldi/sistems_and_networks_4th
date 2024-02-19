# Variabili e Tipi di Dati
nome = "Guido"
eta = 30

# Controllo del Flusso
def esempio_controllo_flusso(condizione):
    if condizione:
        return "La condizione è vera"
    else:
        return "La condizione è falsa"

# Funzioni
def saluta(nome):
    return "Ciao, " + nome + "!"

# Liste
lista_numeri = [1, 2, 3, 4, 5]

def esempio_liste():
    lista_numeri.append(6)
    lista_numeri.remove(3)
    return lista_numeri

# Tuple
tupla_colori = ("rosso", "verde", "blu")

# Stringhe
testo = "Python è fantastico"

def manipola_stringhe(testo):
    return testo.upper(), testo.split()

# Set
insieme_numeri = {1, 2, 3, 4, 5}

# Dizionari
dizionario_persona = {"nome": "Mario", "eta": 25, "città": "Roma"}

def esempio_dizionari():
    dizionario_persona["professione"] = "Programmatore"
    del dizionario_persona["eta"]
    return dizionario_persona

# Gestione dei File
def scrivi_su_file(testo, nome_file):
    with open(nome_file, 'w') as file:
        file.write(testo)

def leggi_da_file(nome_file):
    with open(nome_file, 'r') as file:
        contenuto = file.read()
    return contenuto


# Esempi di utilizzo delle funzioni
print("Variabili e Tipi di Dati:", nome, eta)
print("Controllo del Flusso:", esempio_controllo_flusso(True))
print("Funzioni:", saluta("Guido"))
print("Liste:", esempio_liste())
print("Tuple:", tupla_colori)
print("Stringhe:", manipola_stringhe(testo))
print("Set:", insieme_numeri)
print("Dizionari:", esempio_dizionari())

# Esempi di utilizzo della gestione dei file
testo_da_scrivere = "Questo è un testo da scrivere su file."
nome_file = "esempio_file.txt"
scrivi_su_file(testo_da_scrivere, nome_file)
contenuto_file = leggi_da_file(nome_file)
print(f"Contenuto del file '{nome_file}': {contenuto_file}")
