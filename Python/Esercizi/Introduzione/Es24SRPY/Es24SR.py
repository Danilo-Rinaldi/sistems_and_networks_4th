#p 55 n 11

def main():
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    soglia = len(x) // 2
    x1 = []
    x2 = []

    for i in x:
        if i <= soglia:
            x1.append(i)
        else:    
            x2.append(i)

    x1.append(5)

    print("Lista originale:", x)
    print("x1 contiene valori <= soglia:", x1)
    print("x2 contiene valori > soglia:", x2)

if __name__ == "__main__":
    main()