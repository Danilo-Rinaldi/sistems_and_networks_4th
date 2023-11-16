#es 15

#Permettere all'utente di inserire il suo nome e stampare il nome in cui tutti i caratteri tranne il primo
#sono sostituiti con un *

def main():
    nome = input("Inserisci il nome: ")

    for i in range(1, len(nome)):
        nome = nome[0] + '*' * i

    print(f"Nome finale: {nome}")


if __name__ == "__main__":
    main()