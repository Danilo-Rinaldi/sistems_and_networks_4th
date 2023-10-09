import turtle

print("Inserisci il numero di punte per la tua stella:")
numero_punte = int(input())

print("Inserisci il colore della stella:")
colore = input()

window = turtle.Screen()
victor = turtle.Turtle()

victor.speed(5)

victor.color(colore)
victor.fillcolor(colore)

victor.begin_fill()

for _ in range(numero_punte):
    victor.forward(200)  # Lunghezza delle punte della stella
    victor.right(180 - 180 / numero_punte)

victor.end_fill()

window.mainloop()
