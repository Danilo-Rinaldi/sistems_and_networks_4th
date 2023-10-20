#p55 n 10

def main():

    voti = [10, 8, 6, 7, 8, 7, 6, 8, 9, 10]

    print(f"{voti[1 : -1]}")

    voti[3] = 10

    print(f"{voti[0 : 3]}")


if __name__ == "__main__":
    main()