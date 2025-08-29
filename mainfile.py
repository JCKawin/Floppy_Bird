import pygame
import sys
from settings import *

class FloppyBird():
    def __init__(self):
        self.screen = pygame.display.set_mode(RESOLUTION,vsync=1)
        self.clock = pygame.time.Clock()
    
    def loop(self):
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
        
            self.screen.fill("#ffffff")
            pygame.display.flip()


if __name__ == "__main__":
    player = FloppyBird()
    player.loop()

                

