import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import DUCKING, JUMPING, RUNNING

class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310
    JUMP_VEL = 8.5
    DUCK_POS = 340

    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False
        self.jump_vel = self.JUMP_VEL

    def update(self, user_input):
        if self.dino_jump:
            self.jump()
        if self.dino_run:
            self.run()
        if self.dino_duck:
            self.duck()    

        if user_input[pygame.K_LSHIFT] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False

        elif user_input[pygame.K_SPACE] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True

        elif not self.dino_jump:
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False

        if self.step_index >= 10:
            self.step_index = 0

    def draw(self,screen):
        screen.blit(self.image,(self.dino_rect.x, self.dino_rect.y))

    def run(self):
        self.dino_rect.y = self.Y_POS
        self.dino_rect.x = self.X_POS
        if self.step_index< 5:
            self.image = RUNNING[0]
        else:
            self.image = RUNNING[1]
        #Before
        # self.step_index = self.step_index + 1   
        #NOW
        self.step_index += 1        

    def jump(self):
        self.image = JUMPING
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8

        if self.jump_vel <- self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL      

    def duck(self):
        self.image = DUCKING[0]
        self.dino_rect.y = self.DUCK_POS
        if self.step_index< 5:
            self.image = DUCKING[0]
        else:
            self.image = DUCKING[1]
        self.step_index += 1       
        






   