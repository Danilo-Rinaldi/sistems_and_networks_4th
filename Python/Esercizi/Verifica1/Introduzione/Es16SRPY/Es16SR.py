#turtle and lists
import turtle

    
    


def main():

    num = 'F'
    list = []
    possible_commands = ['F', 'R', 'L']
    print("Give me some command")
    while num in possible_commands:
        num = input ("F: forward(100) R: right(90) L: left(90) Stop: S ")
        #everything is an object soo everything have some attributes like
        if num in possible_commands:
           list.append(num)

    print("\n")

    window = turtle.Screen()#make a window
    victor = turtle.Turtle()#make a window 

    color = "red"

    for element in list:
        if (element == 'F'):
            victor.forward(100)
        elif(element == 'R'):
            victor.right(90)
        elif(element == 'L'):
            victor.left(90)

    window.mainloop()#keep it open




if __name__ == "__main__":
    main()