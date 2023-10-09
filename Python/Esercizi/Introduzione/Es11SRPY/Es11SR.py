import turtle #example of an importation of a module built-in

#make a program that tells how many perfect squares there are in range 0 to 200

print ("tell me the number of side:\n")
sides = int (input())

print ("tell me the color")
color = input()

window = turtle.Screen()#make a window
victor = turtle.Turtle()#make a window

victor.speed(sides * 100)

victor.color(color)

victor.fillcolor(color)

victor.begin_fill()

for i in range(0, sides):
    
    victor.forward((350 + sides)/sides)
    victor.left(360/sides)

victor.end_fill()
    






window.mainloop()#keep it open


