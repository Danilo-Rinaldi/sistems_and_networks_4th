import pygame
import sys

class Grafo():
    def __init__(self):
        self.mat = []

    def getMatriceFromFileCSV(self, path):
        
        self.mat = []

        with open(path, 'r') as file:

            for riga in file:
                elementi = riga.split(",")
                
                riga_interi = [int(elemento) for elemento in elementi]
                
                self.mat.append(riga_interi)

                #self.mat.append([int(elemento) for elemento in riga.split(", ")])

        print(self.mat)

    def calc_path(self, path):  
        """
        with open (path, "r") as f:

            self.mat = [[int(c) for c in riga.split(", ")] for riga in f.readline()]
        """

        pass



    def drawMatrice(self):

        pygame.init()
        lato_x = 100
        lato_y = 100
        pavimento = self.mat
        n_y = len(pavimento)
        n_x = len(pavimento[0])

        screen = pygame.display.set_mode((n_x * lato_x, n_y * lato_y))

        for riga in pavimento:
            for casella in riga:
                surf1 = pygame.Surface((lato_x, lato_y))
                if casella == 1:
                    surf1.fill("red")
                elif casella == 0:
                    surf1.fill("blue")
                elif casella == 3:
                    surf1.fill("yellow")
                rect1 = surf1.get_rect()
                rect1.topleft = (lato_x - 100, lato_y - 100)
                screen.blit(surf1, rect1)

                pygame.display.flip()
                lato_x += 100
            lato_x = 100
            lato_y += 100

        done = False

        while not done:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    done = True
                  
        pygame.quit()








def main():

    """Task: Aprire un file .csv e caricala in una matrice"""

    """Consigliato: creare una finestra in pygame in cui disegnamo tutta la mappa"""

    mappa = Grafo()

    mappa.getMatriceFromFileCSV('File.csv')

    mappa.drawMatrice()

    """Task: fare un dizionario con chiave il numero della cella libera e all'interno le celle libere a addicenti"""
    """Questo dizionario si chiama tabella delle addiacenze"""






if __name__ == "__main__":
    main()