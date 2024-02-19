import turtle #example of an importation of a module built-in

#make a program that tells how many perfect squares there are in range 0 to 200

print ("tell me the number of side:\n")
sides = int (input())

print ("tell me the color")
color = input()

window = turtle.Screen()#make a window
victor = turtle.Turtle()#make a window

x = 200

y = 4

victor.color(color)

victor.penup()
victor.goto(-700, 500)



for j in range (0,y):

    victor.goto(-700, -1*(j*x) + 300)

    for k in range (0, y):
  
        victor.pendown()

        for i in range(0, sides):
            victor.forward((x + sides)/sides)
            victor.left(360/sides)

        victor.penup()
        sides = sides + 1
        victor.forward(x)

  


    
window.mainloop()#keep it open