import pygame
import random

pygame.init()

# Imposto dimensioni schermata
larghezza, altezza = 1000, 750

# Carico le immagini
testa_img = pygame.image.load("Testa.png")
corpo_img = pygame.image.load("Corpo.png")
coda_img = pygame.image.load("Coda.png")
sfondo_img = pygame.image.load("Background.png")
cibo_img = pygame.image.load("Cibo.png")

# Scalo le immagini per farle combaciare con il blocco del serpente
dimensione_blocco = 25
testa_img = pygame.transform.scale(testa_img, (dimensione_blocco, dimensione_blocco))
corpo_img = pygame.transform.scale(corpo_img, (dimensione_blocco, dimensione_blocco))
coda_img = pygame.transform.scale(coda_img, (dimensione_blocco, dimensione_blocco))
sfondo_img = pygame.transform.scale(sfondo_img, (larghezza, altezza))
cibo_img = pygame.transform.scale(cibo_img, (dimensione_blocco, dimensione_blocco))

# Creo la finestra di gioco
schermo = pygame.display.set_mode((larghezza, altezza))
pygame.display.set_caption("Snake Game")

# Inizializzo il serpente
lunghezza_serpente = 1
serpente = [[larghezza // 2, altezza // 2]]

# Inizializzo il cibo
cibo = [random.randint(0, larghezza // dimensione_blocco - 1) * dimensione_blocco,
        random.randint(0, altezza // dimensione_blocco - 1) * dimensione_blocco]

# Inizializzo la direzione del serpente
direzione = [1, 0]

# Velocità del serpente
velocita_iniziale = 10
velocita = velocita_iniziale
incremento_velocita = 1
tick_per_incremento = 10
tick_counter = 0

# Flag per indicare se chiudere la partita
esci = False

# Punteggio
punteggio = 0
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                pygame.quit()
            elif evento.key == pygame.K_w and direzione != [0, 1]:
                direzione = [0, -1]
            elif evento.key == pygame.K_s and direzione != [0, -1]:
                direzione = [0, 1]
            elif evento.key == pygame.K_a and direzione != [1, 0]:
                direzione = [-1, 0]
            elif evento.key == pygame.K_d and direzione != [-1, 0]:
                direzione = [1, 0]

    if not esci:
        tick_counter += 1
        if tick_counter == tick_per_incremento:
            tick_counter = 0
            # Aggiorno la posizione del serpente ogni tick_per_incremento
            testa_serpente = [serpente[0][0] + direzione[0] * dimensione_blocco,
                              serpente[0][1] + direzione[1] * dimensione_blocco]

            # Controllo se è nel campo da gioco
            if not (0 <= testa_serpente[0] < larghezza and 0 <= testa_serpente[1] < altezza):
                esci = True

            # Controllo se la testa è nel corpo
            if testa_serpente in serpente[1:]:
                esci = True

            # Controllo se il serpente sta mangiando il cibo
            if testa_serpente == cibo:
                punteggio += len(serpente)
                lunghezza_serpente += 1
                cibo = [random.randint(0, larghezza // dimensione_blocco - 1) * dimensione_blocco,
                        random.randint(0, altezza // dimensione_blocco - 1) * dimensione_blocco]
                if punteggio >= 1000:
                    esci = True  # Vittoria
                

            else:
                serpente.pop()

            # Aggiungi la nuova testa del serpente
            serpente.insert(0, testa_serpente)

    # Disegno lo sfondo
    schermo.blit(sfondo_img, (0, 0))

    # Disegno il serpente partendo dalla testa
    for i in range(len(serpente)):
        blocco = serpente[i]

        if i == 0:  # Testa
            # Calcola l'angolo di rotazione in base alla direzione
            if direzione == [1, 0]:
                angolo = 270  # Destra
            elif direzione == [-1, 0]:
                angolo = 90  # Sinistra
            elif direzione == [0, 1]:
                angolo = 360  # Giu
            elif direzione == [0, -1]:
                angolo = 180  # Su
            testa_rotata = pygame.transform.rotate(testa_img, -angolo)
            schermo.blit(testa_rotata, (blocco[0], blocco[1]))

        elif i == len(serpente) - 1:  # Coda
            # Ruota
            if direzione == [1, 0]:
                angolo = 270  # Destra
            elif direzione == [-1, 0]:
                angolo = 90  # Sinistra
            elif direzione == [0, 1]:
                angolo = 180  # Basso
            elif direzione == [0, -1]:
                angolo = 0  # Alto
            coda_rotata = pygame.transform.rotate(coda_img, angolo)
            schermo.blit(coda_rotata, (blocco[0], blocco[1]))

        else:  # Corpo
            schermo.blit(corpo_img, (blocco[0], blocco[1]))

    # Disegno il cibo con l'immagine personalizzata
    schermo.blit(cibo_img, (cibo[0], cibo[1]))

    # Stampo il punteggio
    testo_punteggio = font.render("Punteggio: {}".format(punteggio), True, (0, 0, 0))  # Stampo il punteggio
    schermo.blit(testo_punteggio, (10, 10))

    # Mostra il messaggio "Hai perso" o "Hai vinto" se necessario
    if esci:
        if punteggio >= 1000:
            testo_vinto = font.render("Hai vinto!", True, (0, 0, 0))
            schermo.blit(testo_vinto, (larghezza // 2 - 100, altezza // 2 - 50))
        else:
            testo_hai_perso = font.render("Hai perso!", True, (0, 0, 0))
            schermo.blit(testo_hai_perso, (larghezza // 2 - 100, altezza // 2 - 50))

    # Aggiorno lo schermo
    pygame.display.flip()

    # Imposto il limite di frame per la velocità del serpente
    clock.tick(60)
