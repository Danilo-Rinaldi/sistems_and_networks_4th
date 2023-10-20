# Lists

def print_list(l):
    for element in l:
        print(element, end = " ")#at the end he doesn't get to the point and he write end
    print("\n")
    #print("hey I got to the point")

def main():

    l = [1, 2, 3.14, 4, 5, "Hello"]
    
    l1 = ["I am", "doing", "sistem and networks"];

    #print (l)

    #print(l [-1])

    #print(l[::-1])

    #print_list (l)

    #print_list(l[::-1])

    #print_list(l1 + l)

    #print_list(3*l1[::-1])

    #we want to permit at the user to charge a list
    num = 1
    list = []
    while num > 0:
        num = int (input ("Dimmi un numero: (-1 per interrompere)"))
        #everything is an object soo everything have some attributes like
        if num > 0:
           list.append(num)

    print("\n")
    print_list (list)




if __name__ == "__main__":
    main()