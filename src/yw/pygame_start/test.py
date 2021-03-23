import pygame

pygame.init()

v_screen_width = 480
v_screen_height = 640

screen = pygame.display.set_mode((v_screen_width, v_screen_height))

pygame.display.set_caption(("My Game"))

running = True

while running:
    for event in pygame.event.get(): # 이벤트 발생 체크
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생
            running = False
pygame.quit()
