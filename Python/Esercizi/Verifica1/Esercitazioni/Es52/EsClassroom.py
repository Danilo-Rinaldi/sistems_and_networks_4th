import turtle
import csv
import random

"""
def move_turtle(t, direction):
    if direction == 1:
        t.setheading(90)  #nord
    elif direction == 2:
        t.setheading(270)  #sud
    elif direction == 3:
        t.setheading(0)  #est
    elif direction == 4:
        t.setheading(180)  #ovest
    t.forward(10)

def main():
    
   
    bob = turtle.Turtle()

    screen = turtle.Screen()
   
    height=600
    width=600
    screen.setup(width, height)

    coordinate = [(0, 0)]#lista di tuple

    old = [(0, 0)]#lista di tuple

    minuti = int(60)

    for _ in range(minuti):

        direction = random.randint(1, 4)

        move_turtle(bob, direction)

        x = bob.getx()
        y = bob.gety()

        if (x, y) in old:
            print("sei gia stato qui")
        else:
            old.append((x, y))
        coordinate.append((x, y))

    bob.hideturtle()
    screen.update()

    
    print(coordinate)

    print("\n\n")

    print(old)

    turtle.done()

"""

class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def move (bob, direction):

    bob.setheading(direction * 90)

    bob.forward(10)

def main():

    """
    Coord = Punto(3, 5)

    print(Coord.x)

    """

    bob = turtle.Turtle()

    screen = turtle.Screen()
   
    height=600
    width=600
    screen.setup(width, height)

    path = {0: Punto(0, 0)} #dizionario con chiave il tempo in minuti

    minuti = int(60)

    for minuto in range(minuti):

        #dobbiamo
        #simulare movimenti casuali/
        #disegnare il percorso con turtle/

        dir = random.randint(1, 4)

        move(bob, dir)

        x, y= bob.pos()

        path[minuto] = Punto(x, y)


        #BONUS controllo passaggio punto già visitato

        for passati in range(0, minuto):

            if (path[passati].x == path[minuto].x and path[passati].y == path[minuto].y):
                print(f"sono già stato qui: {path[minuto].x} {path[minuto].y}")



    

    #quando finito il ciclo dobbiamo
    #scrivere su file il percorso
    #struttura:
    #COLONNE: minuto X, Y

    print("controllo")

    with open("Path.csv", "w") as file: #creo un oggetto chiamato open e solo dopo posso scriverci

        #file.write("")

        #proviamo a fare il cilo sul dizionario percorso

        file.write("Minuto, X, y\n")

        for minuto in path:
            file.write(f"{minuto}, {int(path[minuto].x)}, {int(path[minuto].y)}\n")


    bob.hideturtle()
    screen.update()






        

if __name__ == "__main__":
    main()