import pygame as pg
from arkanoid.entities import Bola, Raqueta, Ladrillo
from arkanoid import niveles, FPS

class Escena:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.reloj = pg.time.Clock()
    
    def bucle_ppal() -> bool:
        return False       

class Partida(Escena):    
    def __init__(self, pantalla):
        super().__init__(pantalla)
        
        self.bola = Bola(self.pantalla.get_width()//2, self.pantalla.get_height() - 90, self.pantalla)
        self.raqueta = Raqueta(self.pantalla.get_width()//2, self.pantalla.get_height() -60 , self.pantalla)
        
       
        self.fondo = pg.image.load("./resources/images/background.jpg")
        self.ladrillos = pg.sprite.Group()
        self.todos = pg.sprite.Group()
        self.reset()
        self.fuente = pg.font.Font("resources/fonts/BebasNeue-Regular.ttf", 30)

    def reset(self):
        self.ladrillos.empty()
        self.todos.empty()
        self.todos.add(self.bola, self.raqueta)
        self.contadorVidas = 3
        self.contadorPuntos = 0

    def creaLadrillos(self, nivel):
        for col, fil in niveles[nivel]:
                l = Ladrillo(5 + 60 * col, 25 + 30 * fil, 50, 20)
                self.ladrillos.add(l)
        
        self.todos.add(self.ladrillos)
                      
    def bucle_ppal(self) -> bool:
        nivel = 0
        self.reset()
        

        while self.contadorVidas > 0 and nivel < len(niveles):
            self.creaLadrillos(nivel)
            
            while self.contadorVidas > 0 and len(self.ladrillos) > 0:
                self.reloj.tick(FPS)
                
                eventos = pg.event.get()
                for evento in eventos:
                    if evento.type == pg.QUIT:
                        return False           
                
                self.pantalla.blit(self.fondo, (0,0))

                self.todos.update()

                self.bola.comprobarToque(self.raqueta)

                if not self.bola.esta_viva:
                    self.contadorVidas -= 1
                    self.bola.reset()
                    self.raqueta.reset()
                    pg.time.wait(500)
                    

                for ladrillo in self.ladrillos:
                    if ladrillo.comprobarToque(self.bola):
                        self.contadorPuntos += 10
                        self.ladrillos.remove(ladrillo)
                        self.todos.remove(ladrillo)
                    
                        
                self.todos.draw(self.pantalla)

                texto = self.fuente.render(f"VIDAS:{self.contadorVidas}", True, (255,255,255))
                texto2 = self.fuente.render(f"PUNTUACION: {self.contadorPuntos}", True, (255,255,255))
                rectexto = texto.get_rect()
                rectexto2 = texto2.get_rect()

                self.pantalla.blit(texto, ((self.pantalla.get_width() - rectexto.width - 10, self.pantalla.get_height() - rectexto.height)))
                self.pantalla.blit(texto2, ((10, self.pantalla.get_height()- rectexto2.height)))

                pg.display.flip()

            nivel += 1
            self.bola.reset()
            pg.time.wait(500)

        return True

class GameOver(Escena):
    def __init__(self, pantalla):
        pg.Rect
        super().__init__(pantalla)
        self.fuente = pg.font.Font("resources/fonts/BebasNeue-Regular.ttf", 30)
        

    def bucle_ppal(self):
        while True:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    return False
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_SPACE:
                        return True

            self.pantalla.fill((0,0,0))
            texto = self.fuente.render("GAME OVER", True, (255,255,255))
            rectexto = texto.get_rect()

            texto2 = self.fuente.render("Pulsa espacio para reiniciar", True, (255,255,255))
            rectexto2 = texto2.get_rect()

            self.pantalla.blit(texto, ((self.pantalla.get_width() - rectexto.width) // 2, (self.pantalla.get_height() - rectexto.height) // 2  - 20))
            self.pantalla.blit(texto2, ((self.pantalla.get_width() - rectexto2.width) // 2, (self.pantalla.get_height() - rectexto2.height) // 2 + 20))

            pg.display.flip()

class Portada(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        self.fuente = pg.font.Font("resources/fonts/BebasNeue-Regular.ttf", 30)
    
    def bucle_ppal(self):
        while True:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    return False
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_SPACE:
                        return True
            
            self.pantalla.fill((0,0,0))
            texto = self.fuente.render("Pulsa espacio para comenzar", True, (255,255,255))
            rectexto = texto.get_rect()

            self.pantalla.blit(texto, ((self.pantalla.get_width() - rectexto.width) // 2, (self.pantalla.get_height() - rectexto.height) // 2))

            pg.display.flip()