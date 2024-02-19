import pygame
import sys
import random
import time

# Inizializzazione di Pygame
pygame.init()

# Impostazioni della finestra di gioco
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Movimento nello Spazio")

# Definizione della classe SpaceObject
class SpaceObject:
    def __init__(self, x, y, width, height, image_path):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.speed_x = 5  # Velocità orizzontale
        self.speed_y = 0  # Velocità verticale
        self.gravity = 0.5  # Forza di gravità
        self.is_jumping = False  # Stato del salto
        self.last_jump_time = 0  # Tempo dell'ultimo salto

    def move(self, keys):
        current_time = time.time() * 1000  # Converte il tempo in millisecondi

        if keys[pygame.K_LEFT]:
            self.x -= self.speed_x
        if keys[pygame.K_RIGHT]:
            self.x += self.speed_x

        # Se premuto il tasto di salto e l'oggetto è a terra, applica una forza di salto
        if keys[pygame.K_SPACE] and not self.is_jumping and current_time - self.last_jump_time >= 250 and abs(self.y - (height - self.height)) < 2:
            self.speed_y = -12
            self.is_jumping = True
            self.last_jump_time = current_time

        # Applica la forza di gravità
        self.speed_y += self.gravity
        self.y += self.speed_y

        # Limita la velocità verticale per evitare un aumento infinito
        self.speed_y = min(self.speed_y, 10)

        # Limita il movimento oltre il limite inferiore
        if self.y > height - self.height:
            self.y = height - self.height
            self.speed_y = 0
            self.is_jumping = False  # L'oggetto è a terra dopo il salto

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

# Definizione della classe FloatingBlock
class FloatingBlock:
    def __init__(self, x, y, width, height, speed, color, image_path=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        if image_path:
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (width, height))
        else:
            self.image = None

    def move(self):
        self.x += self.speed

    def draw(self):
        if self.image:
            screen.blit(self.image, (self.x, self.y))
        else:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

# Funzione principale
def main():
    clock = pygame.time.Clock()

    # Specifica il percorso dell'immagine per la skin dell'oggetto
    player_image_path = "bird.png"

    player = SpaceObject(100, 100, 50, 50, player_image_path)

    # Lista delle piattaforme fluttuanti
    floating_blocks = [
        FloatingBlock(random.randint(0, width), height - 50, 100, 20, random.choice([-2, 2]), (0, 255, 0), "Nuvola.png")
        for _ in range(5)
    ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        keys = pygame.key.get_pressed()
        player.move(keys)

        # Muovi il bird
        for block in floating_blocks:
            block.move()

        # Verifica la collisione con le piattaforme fluttuanti
        for block in floating_blocks:
            if (
                player.x < block.x + block.width
                and player.x + player.width > block.x
                and player.y < block.y + block.height
                and player.y + player.height > block.y
            ):
                player.is_jumping = False  # Consenti il salto quando l'oggetto è sulla piattaforma

        # Aggiorna la posizione delle piattaforme fluttuanti
        for block in floating_blocks:
            block.x = (block.x + width) % width  # Garantire che le piattaforme rimangano nell'area di gioco

        # Genera nuovi blocchi quando i blocchi attuali sono lontani dalla visuale del giocatore
        if floating_blocks[-1].y > height // 2:
            new_block = FloatingBlock(
                random.randint(0, width), height - 50, 100, 20, random.choice([-2, 2]), (0, 255, 0), "Nuvola.png"
            )
            floating_blocks.append(new_block)

        screen.fill((0, 0, 0))

        # Disegna il giocatore
        player.draw()

        # Disegna le piattaforme fluttuanti
        for block in floating_blocks:
            block.draw()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
