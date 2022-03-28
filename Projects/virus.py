# prank virus
# download to test it
import time
import pygame
import os

pygame.init()

screen = pygame.display.set_mode((250, 180))
pygame.display.set_caption('NO')
font = pygame.font.SysFont("Smh Console", 20)
label = font.render("TOO BAD", 1, (0,0,0))

while True:
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      pygame.quit()
      time.sleep(0.10)

      screen = pygame.display.set_mode((250, 160))
      pygame.display.set_caption('message from admin')

screen.fill((255, 255, 255))
screen.blit(label, (50, 50))

pygame.display.update()