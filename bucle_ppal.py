import pygame
pygame.init()

#Parametros juego iniciales
screen_width = 400
screen_height = 900
ancho_bordes = 10
ancho_barra = screen_width/10

xBola = screen_width/2
yBola = screen_height*0.85
xAnterior = screen_width-1
yAnterior = screen_height+1

xBarra = screen_width/2
yBarra = screen_height*0.9

velocidadBolaX = 0.25
velocidadBolaY = 0.2

velocidadBarra = 0.2

pantalla = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Arkanoid")

rojo = (255,0,0)
amarillo = (255, 255, 0)
verde = (0, 255, 0)
azul = (0, 255, 255)
morado = (255, 0, 255)

all_group = pygame.sprite.Group()
test_group = pygame.sprite.Group()

#Bola
bola_juego = pygame.sprite.Sprite()
bola_juego.image = pygame.Surface((20,20))
bola_juego.image.fill(rojo)
bola_juego.rect = pygame.Rect(*pantalla.get_rect().center, 0, 0).inflate(20, 20)
all_group.add(bola_juego)

#Jugador
barra_juego = pygame.sprite.Sprite()
barra_juego.image = pygame.Surface((ancho_barra,10))
barra_juego.image.fill(rojo)
barra_juego.rect = pygame.Rect(*pantalla.get_rect().center,0,0).inflate(ancho_barra,10)
all_group.add(barra_juego)
test_group.add(barra_juego)

#Objetivo hacer funcion crear bloques llenando pantalla
bloque = pygame.sprite.Sprite()
bloque.image = pygame.Surface((40,15))
bloque.image.fill(azul)
bloque.rect = pygame.Rect(*pantalla.get_rect().center,0,0).inflate(40,15)
all_group.add(bloque)
test_group.add(bloque)

#Bordes preguntar como referirme a un miembro del grupo
borde_superior = pygame.sprite.Sprite()
borde_superior.image = pygame.Surface((screen_width, ancho_bordes))
borde_superior.image.fill(amarillo)
borde_superior.rect = pygame.Rect(*pantalla.get_rect(center=((screen_width/2),(screen_height*0.0000001))).center,0,0).inflate(screen_width, ancho_bordes)

borde_inferior = pygame.sprite.Sprite()
borde_inferior.image = pygame.Surface((screen_width, ancho_bordes))
borde_inferior.image.fill(verde)
borde_inferior.rect = pygame.Rect(*pantalla.get_rect(center=((screen_width/2),screen_height)).center,0,0).inflate(screen_width, ancho_bordes)

borde_derecho = pygame.sprite.Sprite()
borde_derecho.image = pygame.Surface((ancho_bordes, screen_height))
borde_derecho.image.fill(azul)
borde_derecho.rect = pygame.Rect(*pantalla.get_rect(center=(screen_width,(screen_height/2))).center,0,0).inflate(ancho_bordes, screen_height)

borde_izquierdo = pygame.sprite.Sprite()
borde_izquierdo.image = pygame.Surface((ancho_bordes, screen_height))
borde_izquierdo.image.fill(morado)
borde_izquierdo.rect = pygame.Rect(*pantalla.get_rect(center=((screen_width*0.0000001),(screen_height/2))).center,0,0).inflate(ancho_bordes, screen_height)

all_group.add(borde_derecho,borde_inferior,borde_izquierdo,borde_superior)
test_group.add(borde_derecho,borde_inferior,borde_izquierdo,borde_superior)

prueba = pygame.sprite.Group()
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
        prueba.add(borde)

vidas = pygame.sprite.Group()
posicion_vidas = [((screen_width*0.9),(screen_height*0.95)),((screen_width*0.8),(screen_height*0.95)),((screen_width*0.7),(screen_height*0.95)),((screen_width*0.6),(screen_height*0.95))]
for i in range(0,4):
    vida = pygame.sprite.Sprite()
    vida.image = pygame.Surface((20,20))
    vida.image.fill(azul)
    vida.rect = pygame.Rect(*pantalla.get_rect(center=(posicion_vidas[i])).center,0,0).inflate(20,20)
    vidas.add(vida)

run = True


movimiento_inicial = True
rebote_derecho = False
rebote_superior = False
rebote_izquierdo = False
rebote_inferior = False
direccion_derecha = False
direccion_izquierda = False
direccion_arriba = False
direccion_abajo = False

#Funciones movimiento y colision
def determinarDireccion():
    global direccion_abajo
    global direccion_arriba
    global direccion_derecha
    global direccion_izquierda

    if yAnterior < yBola:
        direccion_arriba = False
        direccion_abajo = True
        
    if yAnterior > yBola:      
        direccion_arriba = True
        direccion_abajo = False
    if xAnterior < xBola:
        direccion_derecha = True
        direccion_izquierda = False        
    if xAnterior > xBola:
        direccion_derecha = False
        direccion_izquierda = True

def determinarMovimiento():
    global movimiento_inicial
    global rebote_derecho
    global rebote_inferior
    global rebote_izquierdo
    global rebote_superior
    global xBola
    global yBola
    global velocidadBolaX
    global velocidadBolaY
    
    if movimiento_inicial == True:
        xBola -= velocidadBolaX
        yBola -= velocidadBolaY
        
    if rebote_derecho == True:
        xBola -= velocidadBolaX
        if direccion_arriba == True:
            yBola -= velocidadBolaY

        if direccion_abajo == True:
            yBola += velocidadBolaY
        
    if rebote_izquierdo == True:
        xBola += velocidadBolaX
        if direccion_arriba == True:
            yBola -= velocidadBolaY

        if direccion_abajo == True:
            yBola += velocidadBolaY
        
    if rebote_superior == True:
        yBola += velocidadBolaY
        if direccion_derecha == True:
            xBola += velocidadBolaX

        if direccion_izquierda == True:
            xBola -= velocidadBolaX
       
    if rebote_inferior == True:
        yBola -= velocidadBolaY
        if direccion_derecha == True:
            xBola += velocidadBolaX

        if direccion_izquierda == True:
            xBola -= velocidadBolaX

def comprobarColisiones():
    global movimiento_inicial
    global rebote_derecho
    global rebote_inferior
    global rebote_izquierdo
    global rebote_superior
    global xBola
    global yBola
    global direccion_abajo
    global direccion_arriba
    global direccion_derecha
    global direccion_izquierda

    movimiento_inicial = False
    if pygame.sprite.collide_rect(bola_juego,borde_derecho):
        rebote_superior = False
        rebote_inferior = False
        rebote_izquierdo = False
        rebote_derecho = True
    if pygame.sprite.collide_rect(bola_juego,borde_izquierdo):
        rebote_superior = False
        rebote_inferior = False            
        rebote_derecho = False
        rebote_izquierdo = True          
    if pygame.sprite.collide_rect(bola_juego,borde_inferior):
        # Perder vidas, Game Over  
        pygame.sprite.Group.remove(vidas,vida)  
         
        xBola = 300
        yBola = 500
        rebote_inferior = False
        rebote_izquierdo = False
        rebote_derecho = False
        rebote_superior = False
        direccion_derecha = False
        direccion_izquierda = False
        direccion_arriba = False
        direccion_abajo = False
        movimiento_inicial = True       
    if pygame.sprite.collide_rect(bola_juego,borde_superior):            
        rebote_inferior = False
        rebote_izquierdo = False
        rebote_derecho = False
        rebote_superior = True
    if pygame.sprite.collide_rect(bola_juego,barra_juego):            
        rebote_inferior = True
        rebote_izquierdo = False
        rebote_derecho = False
        rebote_superior = False
    if pygame.sprite.collide_rect(bola_juego,bloque):
        bloque.kill()           
        rebote_inferior = False
        rebote_izquierdo = False
        rebote_derecho = False
        rebote_superior = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    KeyPressed = pygame.key.get_pressed() #Movimiento de la Barra
    if KeyPressed[pygame.K_RIGHT]:
        if xBarra > (screen_width - ancho_barra/2):
            pass
        else:
            xBarra = xBarra + velocidadBarra
    if KeyPressed[pygame.K_LEFT]:
        if xBarra <= (0 + ancho_barra/2):
            pass
        else:
            xBarra = xBarra - velocidadBarra

    bola_juego.rect.center = xBola , yBola
    barra_juego.rect.center = xBarra, yBarra
    bloque.rect.center = 50, 40

    determinarDireccion()
            
    xAnterior = xBola
    yAnterior = yBola

    determinarMovimiento()

    colisiones = pygame.sprite.spritecollide(bola_juego, test_group, False)

    pantalla.fill((0,0,0))
    all_group.draw(pantalla)
    vidas.draw(pantalla)
    for s in colisiones:
        comprobarColisiones()
          
    pygame.display.flip()

pygame.quit()
exit()
