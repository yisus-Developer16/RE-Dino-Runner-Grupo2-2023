import random
from dino_runner.components.obstacles.obstacle import Obstacle
class CactusLarge(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0,2)
        super().__init__(image, self.type)
        self.rect.y = 300
        self.rect.x = 600
        

