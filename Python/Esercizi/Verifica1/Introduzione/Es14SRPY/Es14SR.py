#SLICING

def main():

    #SLICING OF STRING

    s = "hello World"
    #    01234
    #   -4-3-2-1

    print(f"the first letter is {s[0]}")#I can take the first letter without knowing the lenght of the string
    print(f"the last letter is {s[4]}")
    print(f"the last letter is {s[-1]}")#I can take the last letter without knowing which is the lenght of the string
    print(f"the last letter is {s[len(s) - 1]}")#it works but I must not use it

    print(s[0:-1])#I can print from the letter number 0 to the letter number -1 excluding
    print(s[1:])#I can print from the letter number 1 excluding to the end
    print(s[:-1])#I can print from the start to the letter number -1 excluding
    print(s)#I can print all
    print(s[::-1])#I can print the revrsed string

    





if __name__ == "__main__":
    main()