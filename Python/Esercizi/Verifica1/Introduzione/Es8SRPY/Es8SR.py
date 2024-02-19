#crea

def main():

    num = int (input ("give me the first number of the operation: "))
    num1 = int (input ("give me the second number of the operation: "))
    type = input ("give me the operation: ")

    if type == '+':
        result = num + num1
    elif type == '-':
        result = num - num1
    elif type == '*':
        result = num * num1
    elif type == '/':
        result = num / num1
    else:
        print ("there is something wrong")
    
    print(f"result {result}")
    


if __name__ == "__main__":
    main()