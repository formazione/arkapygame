#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys, random

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((1376, 900),0,32)

TILE_SIZE = 20

# [loc, velocity, timer]
particles = []

tile_map = {}
# for i in range(10):
#     tile_map[str(i + 4) + ';14'] = [i + 4, 14, (255, 0, 0)]

# tile_map['15;10'] = [15, 10, (0, 0, 255)]
# tile_map['15;11'] = [15, 11, (0, 0, 255)]
# tile_map['15;12'] = [15, 12, (0, 0, 255)]
# tile_map['15;13'] = [15, 13, (0, 0, 255)]

# tile_map['11;11'] = [11, 11, (0, 255, 255)]
# tile_map['11;12'] = [11, 12, (0, 255, 255)]

clicking = False
pygame.mouse.set_visible(False)
# Loop ------------------------------------------------------- #

def mouse_simulator():
    if random.random() < .05:
        clicking = True
    else:
        clicking = False
    mx = random.randrange(0, 800)
    my = random.randrange(0, 800)
    return clicking, mx, my

while True:
    
    # Background --------------------------------------------- #
    screen.fill((0,0,0))
    clicking, mx, my = mouse_simulator()
    # mx, my = pygame.mouse.get_pos()
    # Particles ---------------------------------------------- #
    if clicking:
        for i in range(10):
            particles.append([[mx, my], [random.randint(0, 42) / 6 - 3.5, random.randint(0, 42) / 6 - 3.5], random.randint(4, 6)])

    for particle in particles:
        particle[0][0] += particle[1][0]
        loc_str = str(int(particle[0][0] / TILE_SIZE)) + ';' + str(int(particle[0][1] / TILE_SIZE))
        # if loc_str in tile_map:
        #     particle[1][0] = -0.7 * particle[1][0]
        #     particle[1][1] *= 0.95
        #     particle[0][0] += particle[1][0] * 2
        particle[0][1] += particle[1][1]
        loc_str = str(int(particle[0][0] / TILE_SIZE)) + ';' + str(int(particle[0][1] / TILE_SIZE))
        # if loc_str in tile_map:
        #     particle[1][1] = -0.7 * particle[1][1]
        #     particle[1][0] *= 0.95
        #     particle[0][1] += particle[1][1] * 2
        particle[2] -= 0.035
        particle[1][1] += 0.15
        pygame.draw.circle(screen, (255, 255, 255), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
        if particle[2] <= 0:
            particles.remove(particle)

    # Render Tiles ------------------------------------------- #
    # for tile in tile_map:
    #     pygame.draw.rect(screen, tile_map[tile][2], pygame.Rect(tile_map[tile][0] * TILE_SIZE, tile_map[tile][1] * TILE_SIZE, TILE_SIZE, TILE_SIZE))
    
    # Buttons ------------------------------------------------ #
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

        # if event.type == MOUSEBUTTONDOWN:
        #     if event.button == 1:
        #         clicking = True

        # if event.type == MOUSEBUTTONUP:
        #     if event.button == 1:
        #         clicking = False                
    # Update ------------------------------------------------- #
    pygame.display.update()
    mainClock.tick(60)