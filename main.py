import pygame
from car import Car
from frog import Player
from log import Log
from random import randint


def generate_cars(car_list, level):
    # randomly generate the cars (and trucks) in the game
    if randint(0, 5) == 0:
        car_list.append(Car(0, level))
    if randint(0, 5) == 0:
        car_list.append(Car(1, level))
    if randint(0, 5) == 0:
        car_list.append(Car(2, level))
    if randint(0, 5) == 0:
        car_list.append(Car(3, level))
    if randint(0, 5) == 0:
        car_list.append(Car(4, level))

    return car_list


def generate_small_logs(log_list, level):
    # randomly generate the small logs in the game
    if randint(0, 1) == 0:
        log_list.append(Log(0, level))
    if randint(0, 1) == 0:
        log_list.append(Log(4, level))

    return log_list


def generate_large_logs(log_list, level):
    # randomly generate the medium and large logs in the game
    if randint(0, 1) == 0:
        log_list.append(Log(1, level))
    if randint(0, 1) == 0:
        log_list.append(Log(2, level))
    if randint(0, 1) == 0:
        log_list.append(Log(3, level))

    return log_list


def main():
    # initialize the game
    pygame.init()
    background = pygame.image.load("sprites/frogger_background.gif")
    counter = 0
    level = 0
    car_list = []
    log_list = []
    clock = pygame.time.Clock()
    player = Player()
    screen = pygame.display.set_mode((516, 550))  # screen dimensions

    # start game loop
    while True:
        # handle user inputs
        player.event()
        clock.tick(60)

        if counter % 40 == 0:
            car_list = generate_cars(car_list, level)

        if counter % 100 == 0:
            log_list = generate_small_logs(log_list, level)

        if counter % 180 == 0:
            log_list = generate_large_logs(log_list, level)

        for car in car_list:
            car.shift()
            player.check_collision(car_list)

        for log in log_list:
            log.shift()
            player.float(log)
            player.check_drown(log_list)

        player.check_bounds()  # Checks if player is out of bounds

        if player.check_home():  # Checks if player is at the end of the map
            level += 1
            player.restart()

        counter += 1

        # update display
        screen.fill((0, 0, 0))  # black
        screen.blit(background, (0, 0))

        for car in car_list:
            screen.blit(car.image, car.rect)
        for log in log_list:
            screen.blit(log.image, log.rect)

        screen.blit(player.image, player.rect)
        pygame.display.flip()


if __name__ == '__main__':
    main()
