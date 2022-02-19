import pygame as pg
pg.init()

class Bola:
    def __init__(self, x, y, color=(255,255,255), radio=10, velocidad=0.2):
        self.x = x
        self.y = y
        self.color = color
        self.radio = radio
        self.velocidadX = velocidad*1.5
        self.velocidadY = velocidad
    def mover(self, limDer, limInf):     
        self.x += self.velocidadX
        self.y -= self.velocidadY

        if self.x <= self.radio or self.x >= limDer - self.radio:
            self.velocidadX *= -1
        if self.y <= self.radio or self.y >= limInf - self.radio:
            self.velocidadY *= -1
    def dibujar(self, superficie):
        pg.draw.circle(superficie, self.color, (self.x, self.y), self.radio)

class Raqueta:
    def __init__(self, x, y, color=(255,0,0), ancho=40, alto=10, velocidad=0.2):
        self.x = x
        self.y = y
        self.color = color
        self.ancho= ancho
        self.alto = alto
        self.velocidad = velocidad
    def mover(self, limDer):
        KeyPressed = pg.key.get_pressed()
        if KeyPressed[pg.K_RIGHT]:
            if self.x >= limDer - self.ancho:
                pass
            else:
                self.x += self.velocidad
        if KeyPressed[pg.K_LEFT]:
            if self.x <= 0:
                pass
            else:
                self.x -= self.velocidad
        pass
    def dibujar(self, superficie, posicionX, posicionY):
        pg.draw.rect(superficie, self.color,(posicionX, posicionY, self.ancho, self.alto))


class Game:
    def __init__(self, ancho=500, alto=900):
        self.pantalla = pg.display.set_mode((ancho,alto))
        self.bola = Bola(ancho//2, alto*0.9, (255,255,0))
        self.raqueta = Raqueta(ancho/2,alto*0.95, (255,0,0), ancho/10)

    def bucle_ppal(self):
        game_over = False

        while not game_over:

            eventos = pg.event.get()
            for evento in eventos:
                if evento.type == pg.QUIT:
                    game_over = True
            
            self.raqueta.mover(self.pantalla.get_width())
            self.bola.mover(self.pantalla.get_width(), self.pantalla.get_height())
            self.pantalla.fill((0,0,0))
            self.bola.dibujar(self.pantalla)
            self.raqueta.dibujar(self.pantalla, self.raqueta.x, self.raqueta.y)

            pg.display.flip()


if __name__ == "__main__":
    pg.init()
    game = Game()
    game.bucle_ppal()
    pg.quit()