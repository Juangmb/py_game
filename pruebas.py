import pygame

pygame.init()

pantalla = pygame.display.set_mode((600,900))
rojo = (255,0,0)
amarillo = (255, 255, 0)
verde = (0, 255, 0)
azul = (0, 255, 255)
morado = (255, 0, 255)
game_over = False

all_group = pygame.sprite.Group()

def crearBordes():
    surface = [(580,10),(580,10),(10,890),(10,890)]
    color = [amarillo, verde, azul, morado]
    center = [(300,10),(300,890),(590,450),(10,450)]
    tamaño = [(580,10),(580,10),(10,890),(10,890)]
    for i in range(0,4):
        borde = pygame.sprite.Sprite()
        borde.image = pygame.Surface(surface[i])
        borde.image.fill(color[i])
        borde.rect= pygame.Rect(*pantalla.get_rect(center=center[i]).center,0,0).inflate(tamaño[i])
        all_group.add(borde)

print(all_group)

x = 300
y = 400

while not game_over:
    #Procesar eventos
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            game_over = True
        
    #Modificar los objetos del juego+

    signo = "-"

    izquierda = "(x += -0.1)"
    derecha = "(x += +0.1)"
    arriba = "y += -0.15"
    abajo = "y += +0.15"
    
    #Refrescar pantalla
    pantalla.fill((255, 0, 0))
    crearBordes()
    all_group.draw(pantalla)

    bola = pygame.draw.rect(pantalla, (255,255,0),(x,y,10,10))

    

   
    

    pygame.display.flip()

pygame.quit()