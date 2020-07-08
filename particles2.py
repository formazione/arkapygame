#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys, random

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((400, 400),0,32)


pygame.mouse.set_visible(False)

particles = []

def spread(mx, my):    
    screen.fill((0,0,0))
    for i in range(1):
        particles.append(
            [
                [mx, my],
                [
                    random.randint(0, 60) / 10 - 3.5,
                    random.randint(0, 60) / 10 - 5],
                random.randint(1, 3)
            ])

    for particle in particles:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.035
        particle[1][1] += 0.15
        pygame.draw.circle(
            screen,
            (128, 128, 255),
            [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
        if particle[2] <= 0:
            particles.remove(particle)


flux = 0
counter = 0


def sprut(mx, my):
    global counter, flux, particles

    spread(mx, my)
    counter += 1
    print(counter)
    if counter > 20:
        flux = 0
        counter = 0
        screen.fill((0, 0, 0))
        particles = []


loop = 1
while loop:
    if flux == 1:
        sprut(mx, my) 

    for event in pygame.event.get():
        if event.type == QUIT:
            loop = 0
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                loop = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mx, my = pygame.mouse.get_pos()
                flux = 1
        # if event.type == pygame.MOUSEBUTTONUP:
        #     if event.button == 1:
        #         flux = 0
    pygame.display.update()
    mainClock.tick(60)

pygame.quit()
sys.exit()