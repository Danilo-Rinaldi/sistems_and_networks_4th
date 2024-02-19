#p55 n 6

def main():

    parola = "supercalifragiliestichespiralidoso"

    print(parola[1::2])#I say where I have to start and (how many letter I have to ignore) + 1

def main():

    parola = "supercalifragiliestichespiralidoso"
    for i in range(len(parola)):
        if i % 2 != 0:
            print(f"{parola[i]}", end = " ")

if __name__ == "__main__":
    main()