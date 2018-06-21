#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Filename      : createWindow.py
#
# Author        : Vauke
# Create        : 2018-06-15 18:04:42
# Last Modified : 2018-06-21 10:33:38

import pygame
from pygame.locals import *
import time
import random

class Plane(object):
    def __init__(self, screen, x, y, image):
        self.x = x
        self.y = y
        
        self.bullets = [] # store bullets
        self.screen = screen
        self.image = pygame.image.load(image)

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullets:
            bullet.display()
            # pop bullet out of the screen
            if bullet.y <= -22:
                self.bullets.pop(0)
        
    def fire(self):
        self.bullets.append(HeroBullet(self.screen, self.x, self.y))

class HeroPlane(Plane):
    def __init__(self, screen):
        #Plane.__init__(self, screen, 190, 700, 'feiji/hero1.png')
        super(HeroPlane, self).__init__(screen, 190, 700, 'feiji/hero1.png')

    def move(self, direction):
        if direction == 'LEFT':
            self.x -= 10
        else:
            self.x += 10

    def control(self):
        # listen events
        for event in pygame.event.get():
            # check keyboard
            if event.type == KEYDOWN:
                # check whether key a or LEFT arrow down
                if event.key == K_a or event.key == K_LEFT:
                    # print('left')
                    self.move('LEFT')
                # check whether key d or RIGHT arrow down
                elif event.key == K_d or event.key==K_RIGHT:
                    # print('right')
                    self.move('RIGHT')
                # check space
                elif event.key == K_SPACE:
                    # print('space')
                    self.fire()
            # check quit button
            elif event.type == QUIT:
                # print('quit')
                exit()

class EnemyPlane(Plane):
    def __init__(self, screen):
        #Plane.__init__(self, screen, 0, 0, 'feiji/enemy0.png')
        super(EnemyPlane, self).__init__(screen, 0, 0, 'feiji/enemy0.png')

        self.direction = 'RIGHT'

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

        # let it fly right and left circulation
        if self.direction == 'RIGHT':
            self.x += 3
            if self.x >= 430:
                self.direction = 'LEFT'
        else:
            self.x -= 3
            if self.x <= 0:
                self.direction = 'RIGHT'

        self.fire()

        for bullet in self.bullets:
            if bullet.y <= 821:
                bullet.display()
            else:
                self.bullets.pop(0)

    def fire(self):
        randNum = random.randint(0, 100)
        if randNum == 1 or randNum == 2:
            self.bullets.append(EnemyBullet(self.screen, self.x, self.y))
        
class Bullet(object):
    def __init__(self, screen, x, y, image):
        self.x = x
        self.y = y
        self.screen = screen
        self.image = pygame.image.load(image)
    
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        self.y -= 5

class HeroBullet(Bullet):
    def __init__(self, screen, x, y):
        #Bullet.__init__(self, screen, x + 40, y - 20, 'feiji/bullet.png')
        super(HeroBullet, self).__init__(screen, x + 40, y - 20, 'feiji/bullet.png')

class EnemyBullet(Bullet):
    def __init__(self, screen, x, y):
        #Bullet.__init__(self, screen, x + 25, y + 40, 'feiji/bullet1.png')
        super(EnemyBullet, self).__init__(screen, x + 25, y + 40, 'feiji/bullet1.png')

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        self.y += 5

def main():
    # create a window
    screen = pygame.display.set_mode((480, 852), 0, 32)
    background = pygame.image.load('feiji/background.png')
    plane = HeroPlane(screen)
    enemy = EnemyPlane(screen)

    while True:
        # put backgroud to (0, 0)
        screen.blit(background, (0,0))
        # put plane to (x, y)
        plane.display()
        enemy.display()
        pygame.display.update()
        
        plane.control()
        time.sleep(0.01)

if __name__ == '__main__':
    main()
