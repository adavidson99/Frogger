import pygame
import sys
from pygame.locals import *


class Player(pygame.sprite.Sprite):
    # Frog class for controlling the player and checking collisions
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("frogup1.gif")
        self.rect = self.image.get_rect().move(250, 475)

        # sprite movement dictionaries
        self.image_up = {1: "frogup1.gif", -1: "frogup2.gif"}
        self.image_down = {1: "frogdown1.gif", -1: "frogdown2.gif"}
        self.image_right = {1: "frogright1.gif", -1: "frogright2.gif"}
        self.image_left = {1: "frogleft1.gif", -1: "frogleft2.gif"}

        # sprite movement binary values for alternating the frog image
        self.up_value = 1
        self.down_value = 1
        self.right_value = 1
        self.left_value = 1

    def event(self):
        # checks the keyboard inputs to move the player on the map
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

            if event.type == KEYDOWN:

                if event.key == pygame.K_RIGHT:
                    self.rect = self.rect.move(37, 0)
                    self.image = pygame.image.load(self.image_right[self.right_value])
                    self.right_value *= -1

                if event.key == pygame.K_LEFT:
                    self.rect = self.rect.move(-37, 0)
                    self.image = pygame.image.load(self.image_left[self.left_value])
                    self.left_value *= -1

                if event.key == pygame.K_UP:
                    self.rect = self.rect.move(0, -37)
                    self.image = pygame.image.load(self.image_up[self.up_value])
                    self.up_value *= -1

                if event.key == pygame.K_DOWN:
                    self.rect = self.rect.move(0, 37)
                    self.image = pygame.image.load(self.image_down[self.down_value])
                    self.down_value *= -1

    def check_bounds(self):
        # checks if the player has gone out of bounds
        if -5 > self.rect[0] > 520 or 550 < self.rect[1] < 20:
            self.restart()

    def float(self, obj):
        # checks if the player is floating on the log
        if self.rect.colliderect(obj.rect):
            self.rect = self.rect.move(obj.speed[obj.number], 0)

    def check_drown(self, log_list):
        # checks if the player has fallen into the water
        if 225 >= self.rect[1] > 50 and self.rect.collidelist(log_list) == -1:
            self.restart()

    def check_collision(self, car_list):
        # checks if the player has collided with a car
        if self.rect.collidelist(car_list) != -1:
            self.restart()

    def pause(self):
        return  # keep the player waiting for 5 seconds at the start of the game

    def restart(self):
        # restart the player to the start of the map
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(250, 475)
