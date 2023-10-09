import turtle #example of an importation of a module built-in

#make a program that tells how many perfect squares there are in range 0 to 200

print ("tell me the number of side:\n")
sides = 5#int (input())

print ("tell me the color")
color = "red" #input()

window = turtle.Screen()#make a window
victor = turtle.Turtle()#make a window

victor.speed(sides * 100)

victor.color(color)

victor.fillcolor(color)

victor.begin_fill()

victor.speed(5)

x = sides

for i in range(0, sides):
    
    victor.left(45
    victor.forward(350+sides)/sides)
    victor.right(-45 * sides)
    victor.forward((350 + sides)/sides)
    
    
    x = x - 1







    






window.mainloop()#keep it open


