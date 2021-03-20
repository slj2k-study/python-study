import pygame

pygame.init()

v_screen_width = 480
v_screen_height = 640

screen = pygame.display.set_mode((v_screen_width, v_screen_height))

pygame.display.set_caption(("Second Game"))

#배경이미지 삽입
background = pygame.image.load('C:\\Users\\YoungWoo\\Desktop\\git\\python-study\\src\\yw\\background.png''')
character = pygame.image.load('C:\\Users\\YoungWoo\\Desktop\\git\\python-study\\src\\yw\\character.png''')
enemy = pygame.image.load('C:\\Users\\YoungWoo\\Desktop\\git\\python-study\\src\\yw\\enemy.png''')

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
speed = 1

enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x = 400
enemy_y = 200

total_time = 10
start_tick = pygame.time.get_ticks() #시작 tick 받기





clock = pygame.time.Clock()

# 폰트 정의
game_font = pygame.font.Font(None, 40)

running = True
while running:
    dt = clock.tick(50) #초당 프레임
    for event in pygame.event.get(): # 이벤트 발생 체크
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed_x -= speed
            elif event.key == pygame.K_RIGHT:
                speed_x += speed
            elif event.key == pygame.K_UP:
                speed_y -= speed
            elif event.key == pygame.K_DOWN:
                speed_y += speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                speed_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                speed_y = 0

    character_x += speed_x * dt
    character_y += speed_y * dt

    if character_x < 0:
        character_x = 0
    if character_y < 0:
        character_y = 0
    if character_x + character_width >= background_width:
        character_x = background_width - character_width
    if character_y + character_height >= background_height:
        character_y = background_height - character_height

    #collision
    character_rect = character.get_rect()
    character_rect.left = character_x
    character_rect.top = character_y

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x
    enemy_rect.top = enemy_y


    if character_rect.colliderect(enemy_rect): ##충돌체크
        print('Collision')
        running = False

    screen.blit(background, (0,0))
    screen.blit(character, (character_x ,character_y))
    screen.blit(enemy, (enemy_x, enemy_y))

    #시간정보 추가 , 초단위(/1000)
    elapsed_time = ( pygame.time.get_ticks() - start_tick) / 1000

    #render 출력값 ,True, 색상
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))

    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False
    screen.blit(timer,(10,10))

    pygame.display.update() # 게임화면 다시 그리기

pygame.time.delay(1000)
pygame.quit()
