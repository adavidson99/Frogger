import pygame


class Car(pygame.sprite.Sprite):
    # Car class
    def __init__(self, number, level):
        super().__init__()

        self.number = number
        self.speedup = level * 20

        # cars image and location list
        self.cars = ['sprites/car3.gif', 'sprites/car1.gif', 'sprites/truck.gif', 'sprites/car4.gif', 'sprites/car2.gif']
        self.pos = [429, 393, 357, 321, 285]
        self.speed = [-1.5+(-1.5/100*self.speedup), 1.6+(1.6/100*self.speedup), -1.1+(-1.1/100*self.speedup),
                      1.3+(1.3/100*self.speedup), -2+(-2/100*self.speedup)]

        self.image = pygame.image.load(self.cars[number])
        self.rect = self.image.get_rect()

        if self.number % 2 == 0:
            self.rect = self.rect.move(516, self.pos[number])
        else:
            self.rect = self.rect.move(0, self.pos[number])

    def shift(self):
        # update the car to the next location
        self.rect = self.rect.move(self.speed[self.number], 0)
