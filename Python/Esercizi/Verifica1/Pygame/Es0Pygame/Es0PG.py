import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))

# creiamo una nuova Surface, la coloriamo di bianco e vi disegniamo un cerchio
surf = pygame.Surface((200, 200))
surf.fill("white")
pygame.draw.circle(surf, "red", (50, 50),  20)

# disegniamo surf sulla superficie principale
screen.blit(surf, (500, 500))

# aggiorniamo lo schermo
pygame.display.flip()

# terminiamo correttamente il programma
input("Premi INVIO per terminare il programma")
pygame.quit()