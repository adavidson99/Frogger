import pygame


class Log(pygame.sprite.Sprite):
    # Log class
    def __init__(self, number, level):
        super().__init__()

        self.number = number
        self.speedup = (level * 20)
        # level 0 = 0% increase
        # level 1 = 20% increase
        # level 2 = 40% increase
        # level 3 = 60% increase...

        # images of the objects
        self.objects = ['small_log.png', 'medium_log.png', 'long_log.png', 'medium_log.png', 'small_log.png']
        self.pos = [70, 105, 140, 175, 210]
        self.speed = [-1.8+(-1.8/100*self.speedup), 1.6+(1.6/100*self.speedup), -1.2+(-1.2/100*self.speedup),
                      1.4+(1.4/100*self.speedup), -1.6+(-1.6/100*self.speedup)]

        # loading image
        self.image = pygame.image.load(self.objects[number])
        self.rect = self.image.get_rect()

        if self.number % 2 == 0:
            self.rect = self.rect.move(550, self.pos[number])
        else:
            self.rect = self.rect.move(-100, self.pos[number])

    def shift(self):
        # update the log to the next location
        self.rect = self.rect.move(self.speed[self.number], 0)
