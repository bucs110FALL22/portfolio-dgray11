import pygame

pygame.init()

#gets the display and makes it full screen
#no arguments means full screen
screen = pygame.display.set_mode()

#RGB Scheme
# [R, G, B] => [0-225, 0-225, 0-225]
screen.fill([225, 0, 0])
pygame.display.flip()

pygame.time.wait(500)

screen.fill([0, 225, 0])
pygame.display.flip()

pygame.time.wait(500)

screen.fill([0, 0, 225])
pygame.display.flip()
