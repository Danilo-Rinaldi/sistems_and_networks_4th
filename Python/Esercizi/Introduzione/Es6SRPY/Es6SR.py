#fai un programma che dica se un numero è divisibile per 3

def main():

    num = int(input ("give me the number"))
    rest = num % 3

    if num % 3 == 0:
        print (f"the number {num} is divisibility for 3 and there is no rest")
    else:
        print (f"the number {num} is NOT divisibility for 3 and the rest is {rest}")


if __name__ == "__main__":
    main()