"""
o così
def somma(a, b):
    return a + b
"""

"""
o così
somma = lambda x, y = x + y
"""

somma = lambda a, b : a + b

isPositivo = lambda a : a > 0


def main():

    #lambda function 

    a, b = 10, 5

    print(somma(a, b))

    print(isPositivo(a))

    lista = [10, 4]

    print(somma[0], somma[1])

    print(somma(*lista))#spacchettiamo al lista sui parametri, deve avere n elementi pari a n parametri, ed è più coinciso



if __name__ == "__main__":
    main()