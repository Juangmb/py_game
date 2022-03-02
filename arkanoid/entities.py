import pygame as pg
from arkanoid import FPS

class Vigneta(pg.sprite.Sprite):
    def __init__(self, padre):
        super().__init__()
        self.padre = padre
        
    def intersecta(self, otro) -> bool:

        if self.rect.width > otro.rect.width:
            menor_ancho = otro
            mayor_ancho = self
        else:
            menor_ancho = self
            mayor_ancho = otro

        if self.rect.height > otro.rect.height:
            menor_alto = otro
            mayor_alto = self
        else:
            menor_alto = self
            mayor_alto = otro
        return (menor_ancho.rect.left in range(mayor_ancho.rect.left, mayor_ancho.rect.right) or \
                menor_ancho.rect.right in range(mayor_ancho.rect.left, mayor_ancho.rect.right)) and \
               (menor_alto.rect.top in range(mayor_alto.rect.top, mayor_alto.rect.bottom) or \
                menor_alto.rect.bottom in range(mayor_alto.rect.top, mayor_alto.rect.bottom))

class Ladrillo(Vigneta):
    def __init__(self, x, y, ancho, alto, color=(255,255,255)):
        super().__init__(None)
        self.image = pg.Surface((ancho, alto))
        self.rect = self.image.get_rect(x=x, y=y)
        pg.draw.rect(self.image, color, (0, 0, ancho, alto))
        

    def comprobarToque(self, bola):
        if self.intersecta(bola):
            bola.velocidadY *= -1
            return True

class Raqueta(Vigneta):
    def __init__(self, centrox, centroy, padre):
        super().__init__(padre)
        self.images = []
        for i in range(3):
            self.images.append(pg.image.load(f"./resources/images/electric0{i}.png"))
        self.imagen_activa = 0
        self.frecuenciacambio = FPS//10
        self.contador_frames = 0

        self.image = self.images[self.imagen_activa]
        self.rect = self.image.get_rect(centerx = centrox, centery = centroy)
        self.velocidad = 5
        self.x_ini = centrox
        self.y_ini = centroy
    
    def reset(self):
        self.velocidad = 5
        self.rect.centerx = self.x_ini
        self.rect.centery = self.y_ini

    def update(self):
        KeyPressed = pg.key.get_pressed()
        if KeyPressed[pg.K_RIGHT] or KeyPressed[pg.K_d]:
            if self.rect.right >= self.padre.get_width():
                pass
            else:
                self.rect.x += self.velocidad
        if KeyPressed[pg.K_LEFT] or KeyPressed[pg.K_a]:
            if self.rect.left <= 0:
                pass
            else:
                self.rect.x -= self.velocidad

        if self.contador_frames % self.frecuenciacambio == 0:
            self.imagen_activa = (self.imagen_activa + 1) % len(self.images)

        self.contador_frames += 1

class Bola(Vigneta):
    def __init__(self, centrox, centroy, padre, radio=10, color=(255,255,255)):
        super().__init__(padre)
        self.velocidadX = 5
        self.velocidadY = 5
        self.x_ini = centrox
        self.y_ini = centroy
        self.esta_viva = True

        self.image = pg.Surface((radio * 2, radio * 2))
        pg.draw.circle(self.image, color, (radio, radio), radio)
        self.rect = self.image.get_rect(center=(centrox, centroy))
    
    def reset(self):
        self.rect.centerx = self.x_ini
        self.rect.centery = self.y_ini
        self.velocidadX = 5
        self.velocidadY = 5
        self.esta_viva = True

    def update(self):     
        self.rect.x += self.velocidadX
        self.rect.y -= self.velocidadY

        if self.rect.x <= 0 or self.rect.right >= self.padre.get_width():
            self.velocidadX *= -1

        if self.rect.y <= 0:
            self.velocidadY *= -1
            
        if self.rect.bottom >= self.padre.get_height():
            self.esta_viva = False
 
    def comprobarToque(self, otro):
        if self.intersecta(otro):
            self.velocidadY *= -1
            return True