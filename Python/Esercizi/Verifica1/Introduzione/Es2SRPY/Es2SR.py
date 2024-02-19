def main():

    a = float(input("Tell me a number: "))
    print(f"the type of 'a' is {type(a)}")
    if a > 5:
        print("'a' is bigger to 5")
    elif (a <= 5) and (a>=0):
        print("'a' is bigger or equal than 0 or smaller or equal than 5")
    else:
        print("'a' is smaller or equal to 5")
    



if __name__ == "__main__":
    main()