import pygame
import random
import sys

pygame.init()

info = pygame.display.Info()
SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)
pygame.display.set_caption("Dindows 10")

try:
    bg_img = pygame.image.load("werty.jpg")
    bg_img = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
except:
    bg_img = None

try:
    android_img = pygame.image.load("market.jpg")
    android_img = pygame.transform.scale(android_img, (100, 100))
except:
    android_img = None

try:
    msg_img = pygame.image.load("cooo.jpg")
except:
    msg_img = None

clock = pygame.time.Clock()
running = True
show_bg = True

android_positions = []
msg_positions = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    screen.fill(random_color)

    if bg_img and show_bg:
        screen.blit(bg_img, (0, 0))
    show_bg = not show_bg

    if android_img and random.random() < 0.2:
        x = random.randint(0, SCREEN_WIDTH - 100)
        y = random.randint(0, SCREEN_HEIGHT - 100)
        android_positions.append((x, y))

    if msg_img and random.random() < 0.1:
        x = random.randint(0, SCREEN_WIDTH - 200)
        y = random.randint(0, SCREEN_HEIGHT - 150)
        msg_positions.append((x, y))

    if android_img:
        for pos in android_positions:
            screen.blit(android_img, pos)

    if msg_img:
        for pos in msg_positions:
            screen.blit(msg_img, pos)

    pygame.display.flip()
    clock.tick(12)

pygame.quit()
sys.exit()
