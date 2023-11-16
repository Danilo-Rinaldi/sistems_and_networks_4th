#turtle e dizionari

#con i dizionari devo mandarla di 100 pixel a nord sud est ovest

import turtle 

def GoNorth(victor):
    victor.setheading(270)
    victor.forward(100)

def GoWest(victor):
    victor.setheading()
    victor.forward(100)

def GoEast(victor):
    victor.setheading(90)
    victor.forward(100)

def GoSouth(victor):
    victor.setheading(180)
    victor.forward(100)


def main():




    comandi = {"N": GoNorth, "S": GoSouth, "W": GoWest, "E": GoEast}

    NUM_MAX_OPERAZIONI = 4
    operazioni = []

    for i in range (0, NUM_MAX_OPERAZIONI):
        operazione = input("dimmi delle operazioni tra N S W E separate da spazi che mi permettono di muovere la turtle")
        operazioni.append(operazione)


    #if operazione in comandi:

    window = turtle.Screen()
    victor = turtle.Turtle()

    for operazione in operazioni:
        comandi[operazione](victor)

    window.mainloop()#keep it open

    #else:
        #print ("error")
        #exit()

        #finire

    
    





if __name__ == "__main__":
    main()
