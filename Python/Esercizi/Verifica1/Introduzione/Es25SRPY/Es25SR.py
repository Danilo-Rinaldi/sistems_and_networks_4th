#p 55 n 12

def main():
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    soglia = len(x) // 2
    x1 = []
    x2 = []

    x1, x2 = x [0 :  soglia + 1], x[soglia: ]

    print("Lista originale:", x)
    print("x1 contiene valori <= soglia:", x1)
    print("x2 contiene valori > soglia:", x2)

if __name__ == "__main__":
    main()

