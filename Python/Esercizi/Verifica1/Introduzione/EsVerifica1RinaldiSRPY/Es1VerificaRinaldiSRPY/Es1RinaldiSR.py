import turtle

class Barcode:
    def __init__(self, data):
        self.data = data

    def draw_barcode(self):
        # Configurazione della turtle
        turtle.speed(1)
        turtle.hideturtle()
        turtle.penup()

        # Disegna il codice a barre
        for char in self.data:
            binary_representation = format(ord(char), '08b')  # Converte il carattere in binario a 8 bit
            for bit in binary_representation:
                if bit == '1':
                    self._draw_black_bar()
                else:
                    self._draw_white_bar()

        turtle.done()

    def _draw_black_bar(self):
        turtle.pendown()
        turtle.forward(4)
        turtle.penup()
        turtle.forward(1)  # Spazio di un pixel tra le barre

    def _draw_white_bar(self):
        turtle.pendown()
        turtle.forward(4)
        turtle.penup()
        turtle.forward(1)  # Spazio di un pixel tra le barre

def main():
    data = input("Inserisci una stringa alfanumerica di 8 caratteri: ")
    if len(data) != 8 or any(ord(char) > 255 for char in data):
        print("Errore: La stringa deve essere lunga 8 caratteri e non deve contenere caratteri con codice ASCII maggiore di 255.")
        return

    barcode = Barcode(data)
    barcode.draw_barcode()

if __name__ == "__main__":
    main()
