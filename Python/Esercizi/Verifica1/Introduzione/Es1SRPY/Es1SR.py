def main(): #this is how I define a function
    #I ask with a massege an input
    name = input("what's your name?\n")
    age = input ("How old are you?\n")
    year = int(input ("Witch year are we?"))

    #I print a massage with the variable that I saved
    print(f"Hi {name} I know that you are {age} year")
    print(f"we are in the year number {year}")

    #I print the type of the variable called age
    print(type(age))

#_ under / __ duoble under / __ dounder

if __name__ == "__main__":
    main()