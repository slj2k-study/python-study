import pygame

pygame.init()

v_screen_width = 480
v_screen_height = 640

screen = pygame.display.set_mode((v_screen_width, v_screen_height))

pygame.display.set_caption(("Second Game"))

#배경이미지 삽입
background = pygame.image.load('C:\\Users\\YoungWoo\\Desktop\\git\\python-study\\src\\yw\\background.png''')
character = pygame.image.load('C:\\Users\\YoungWoo\\Desktop\\git\\python-study\\src\\yw\\character.png''')

character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x = 0
character_y = 150

running = True
while running:
    for event in pygame.event.get(): # 이벤트 발생 체크
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생
            running = False
    screen.blit(background, (0,0))
    screen.blit(character, (character_x,character_y))

    pygame.display.update() # 게임화면 다시 그리기
pygame.quit()
