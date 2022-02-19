import pygame

pygame.init()

pantalla = pygame.display.set_mode((600,900))

game_over = False

x = 300
y = 400

while not game_over:
    #Procesar eventos
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            game_over = True
        
    #Modificar los objetos del juego+
    x += -0.1
    y += -0.15
    
    #Refrescar pantalla
    pantalla.fill((255, 0, 0))
    borde_superior = pygame.draw.rect(pantalla,(0,0,0),(10,0,580,10))
    borde_inferior = pygame.draw.rect(pantalla,(0,0,0),(10,890,580,10))
    borde_izquierdo = pygame.draw.rect(pantalla,(0,0,0),(0,0,10,900))
    borde_derecho = pygame.draw.rect(pantalla,(0,0,0),(590,0,10,900))
      
    bola = pygame.draw.rect(pantalla, (255,255,0),(x,y,10,10))

    pygame.display.flip()

pygame.quit()