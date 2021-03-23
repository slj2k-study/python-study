import pygame

pygame.init()

v_screen_width = 480
v_screen_height = 640

screen = pygame.display.set_mode((v_screen_width, v_screen_height))

pygame.display.set_caption(("Second Game"))

#배경이미지 삽입
background = pygame.image.load('C:\\Users\\YoungWoo\\Desktop\\git\\python-study\\src\\yw\\background.png''')
character = pygame.image.load('C:\\Users\\YoungWoo\\Desktop\\git\\python-study\\src\\yw\\character.png''')

background_size = background.get_rect().size
background_width = background_size[0]
background_height = background_size[1]



character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x = 0
character_y = 150

speed_x = 0
speed_y = 0

running = True
while running:
    for event in pygame.event.get(): # 이벤트 발생 체크
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed_x -= 0.5
            elif event.key == pygame.K_RIGHT:
                speed_x += 0.5
            elif event.key == pygame.K_UP:
                speed_y -= 0.5
            elif event.key == pygame.K_DOWN:
                speed_y += 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                speed_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                speed_y = 0

    character_x += speed_x
    character_y += speed_y

    if character_x < 0:
        character_x = 0
    if character_y < 0:
        character_y = 0
    if character_x + character_width >= background_width:
        character_x = background_width - character_width
    if character_y + character_height >= background_height:
        character_y = background_height - character_height


    screen.blit(background, (0,0))
    screen.blit(character, (character_x ,character_y))

    print(speed_x, speed_y)
    pygame.display.update() # 게임화면 다시 그리기


pygame.quit()
