import pygame
import yw_keyboard  as key
import random

## init system value
pygame.init()

v_screen_width = 480
v_screen_height = 640

pygame.display.set_caption(("Quiz 1 Game"))
clock = pygame.time.Clock()

screen = pygame.display.set_mode((v_screen_width, v_screen_height))

## init user data


# 배경이미지 삽입
adress = ['C:\\Users\\YoungWoo\\Desktop\\git\\python-study\\src\\yw\\background.png',
          'C:\\Users\\YoungWoo\\Desktop\\git\\python-study\\src\\yw\\character.png',
          'C:\\Users\\YoungWoo\\Desktop\\git\\python-study\\src\\yw\\enemy.png']

images = list()
for i in adress:
    images.append(pygame.image.load(i))

size = []
for i in images:
    temp_xy = i.get_rect().size
    size.append((temp_xy[0], temp_xy[1]))

position = []
print(size)
position.append([0, 0])
position.append([size[0][0] / 2 - size[1][0] / 2, size[0][1] - size[1][1] - 30] )
position.append([0, 0])

rect = []
for i in images:
    rect.append(i.get_rect())

tick = 60;

speed = 15

start_tick = pygame.time.get_ticks()  # 시작 tick 받기

v_xkeyin = False
v_ykeyin = False

v_flagx = 0
v_flagy = 0

v_accelx = 0
v_accely = 0

running = True

while running:
    dt = clock.tick(tick)  # 초당 프레임
    key_input = key.figure_keboard(v_flagx, v_flagy)

    if key_input == [999,999]:
        running = False

    v_flagx = key_input[0]
    v_flagy = key_input[1]

    if v_flagx == 0:
        v_accelx = 0
    elif v_flagx == 1:
        v_accelx = -1
    elif v_flagx == 2:
        v_accelx = 1

    if v_flagy == 0:
        v_accely = 0
    elif v_flagy == 1:
        v_accely = -1
    elif v_flagy == 2:
        v_accely = 1

    if position[2][1] >= v_screen_height:
        position[2][1] = 0
        position[2][0] = random.randrange(0, v_screen_width - size[2][0])
    else:
        position[2][1] += speed


    if v_accelx * speed > 0 and position[1][0] + size[1][0] + (v_accelx * speed) < v_screen_width:
        position[1][0] += v_accelx * speed
    elif v_accelx * speed < 0 and position[1][0] + (v_accelx * speed) >= 0:
        position[1][0] += v_accelx * speed
#    position[1][1] += v_accely * speed


    screen.blit(images[0], (0, 0))
    screen.blit(images[1], position[1])
    screen.blit(images[2], position[2])

    for i in (1,2):
        rect[i].left = position[i][0]
        rect[i].top = position[i][1]

    if rect[1].colliderect(rect[2]):
        running = False
    pygame.display.update()  # 게임화면 다시 그리기




pygame.time.delay(1000)
pygame.quit()

'''



# 폰트 정의


running = True
while running:
    dt = clock.tick(50) #초당 프레임


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
'''
