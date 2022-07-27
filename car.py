import pygame


class Car(pygame.sprite.Sprite):
    # Car class
    def __init__(self, number):
        super().__init__()

        self.number = number

        # cars image and location list
        self.cars = ['car3.gif', 'car1.gif', 'truck.gif', 'car4.gif', 'car2.gif']
        self.pos = [429, 393, 357, 321, 285]
        self.speed = [-1.5, 1.6, -1.1, 1.3, -2]

        self.image = pygame.image.load(self.cars[number])
        self.rect = self.image.get_rect()

        if self.number % 2 == 0:
            self.rect = self.rect.move(516, self.pos[number])
        else:
            self.rect = self.rect.move(0, self.pos[number])

    def shift(self):
        # update the car to the next location
        self.rect = self.rect.move(self.speed[self.number], 0)
