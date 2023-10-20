#p55 n 3

def main():

    prima = int (13)
    seconda = int (31)

    print(f"prima = {prima} \nseconda = {seconda}")

    prima, seconda = seconda , prima

    print(f"prima = {prima} \nseconda = {seconda}")

if __name__ == "__main__":
    main()