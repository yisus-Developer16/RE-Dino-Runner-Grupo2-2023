import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.cactus import CactusLarge
from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.utils.constants import LARGE_CACTUS
class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        

    def update (self, game):
        if len(self.obstacles) == 0:
            cact = random.randint(0, 1)
            if cact == 1:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            else:
                self.obstacles.append(CactusLarge(LARGE_CACTUS))   

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)    