#p55 n 1

def main():

    list = [int (3), "ciao", float(3.14), False]

    for element in list:
        print(f"{type(element)}= {element} ")


    a = int (3)
    b = "ciao"
    c = float(3.14)
    d = False

    print(f"{type(a)}= {a} ")
    print(f"{type(b)}= {b} ")
    print(f"{type(c)}= {c} ")
    print(f"{type(d)}= {d} ")



if __name__ == "__main__":
    main()