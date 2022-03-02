import pygame as pg
from arkanoid.escenes import Partida, GameOver, Portada

pg.init()

class Game:    
    def __init__(self, ancho=600, alto=800):
        pantalla = pg.display.set_mode((ancho,alto))
        portada = Portada(pantalla)
        partida = Partida(pantalla)
        game_over = GameOver(pantalla)
        self.escenas = [portada, partida, game_over]
        
    def lanzar(self):
        escena_activa = 0
        game_active = True
        while game_active:
            game_active = self.escenas[escena_activa].bucle_ppal()
            escena_activa += 1
            if escena_activa >= len(self.escenas):
                escena_activa = 1
            