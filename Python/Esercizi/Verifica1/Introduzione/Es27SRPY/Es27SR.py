#list comprension
#p 73 n 17
import math

def main():

    num = int(input("Inserisci un numero: "))  # Converto l'input in un intero

    power = [pow(2, i) for i in range(int (math.log2(num)) + 1)]

    print(power)


if __name__ == "__main__":
    main()

