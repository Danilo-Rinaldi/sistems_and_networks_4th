#fai un programma che dica se un numero è divisibile per 3

def main():

    num = int(input ("give me the number: "))
    divisibility = 0

    if num % 2 == 0:
        print (f"the number {num} is divisibility for 2")
        divisibility = 1
    if num % 3 == 0:
        print (f"the number {num} is divisibility for 3")
        divisibility = 1
    if num % 5 == 0:
        print (f"the number {num} is divisibility for 5")
        divisibility = 1
    if divisibility == 0:
        print (f"the number {num} is not disibility for 2 or 3 or 5")



if __name__ == "__main__":
    main()