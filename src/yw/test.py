import pygame

pygame.init()

v_screen_width = 480 #가로 크기
v_screen_height = 640 #세로 크기

screen = pygame.display.set_mode((v_screen_width, v_screen_height))

pygame.display.set_caption(("My Game"))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
