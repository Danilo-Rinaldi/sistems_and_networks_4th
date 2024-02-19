
def main():

    pass

    num = 0

    while num % 2 == 0: 

        print("dimmi un numero dispari: ")

        num = int(input())

    space = " "

    car = "*"

    meta = 0

    for volte in range (0, (num // 2) + 1):

        print(f"{space * ((num // 2) - volte)}{car * (volte * 2 + 1)}")

        meta = volte

    for k in range(0, (num // 2)):
        print(f"{space * (k + 1)}{car * (num - 2 * (k + 1))}")






        

    





if __name__ == "__main__":
    main()