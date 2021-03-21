import pygame
import os
import sys
import imgctrl as im

sys.path.append('C:\\Users\\YoungWoo\\Desktop\\git\\python-study\\src\\yw')
import yw_keyboard as key

pygame.init()

current_path = os.path.dirname(__file__)
img_path = os.path.join(current_path, "images")

background = im.ImageControl(os.path.join(img_path, 'background.png'))
stage = im.ImageControl(os.path.join(img_path, 'stage.png'))
character = im.ImageControl(os.path.join(img_path, 'character.png'))

# init position
character.position[1] = background.height - character.height - stage.height
character.rect[1] = background.height - character.height - stage.height
stage.position[1] = background.height - stage.height

weapons = []
balloons = []

origin_ball = im.Balls(0, 0, 0)
balloons.append(origin_ball)

clock = pygame.time.Clock()
tick = 35
character.speed = 20
weapon_speed = 25

screen = pygame.display.set_mode((background.width, background.height))

v_accel = [0, 0]

running = True
input_x = 0
input_y = 0

# Font
game_font = pygame.font.Font(None, 40)
total_time = 30
start_tick = pygame.time.get_ticks()

game_result = 'Game Over'

while running:
    dt = clock.tick(tick)  # 초당 프레임

    key_input = key.figure_keboard(input_x, input_y)

    input_x = key_input[0]
    input_y = key_input[1]
    input_weapon = key_input[2]

    if key_input == [999, 999]:
        running = False

    # 키보드 입력
    if key_input[0] > 0:
        if character.position[0] + character.speed < background.width - character.speed:
            character.movement(key_input[0] * character.speed, 0)
    elif key_input[0] < 0:
        if character.position[0] > 0:
            character.movement(key_input[0] * character.speed, 0)

    # 무기
    if key_input[2] == 1:
        weapon = im.ImageControl(os.path.join(img_path, 'weapon.png'))
        weapon.position[0] = character.position[0] + (character.width - weapon.width) / 2
        weapon.position[1] = character.position[1]
        weapons.append(weapon)

    for i in weapons:
        if i.position[1] < 0:
            weapons.remove(i)
        else:
            i.movement(0, weapon_speed * -1)

    # 공 위치 정의
    for i in balloons:
        i.process()
        i.calc()

    # 출력
    screen.blit(background.image, background.position)

    for i in weapons:
        screen.blit(i.image, i.position)

    for i in balloons:
        screen.blit(i.image, i.position)

    screen.blit(stage.image, stage.position)

    screen.blit(character.image, character.position)

    # 경과시간
    elapsed_time = (pygame.time.get_ticks() - start_tick) / 1000
    timer = game_font.render("Time : {}".format(int(total_time - elapsed_time)), True, (200, 0, 255))
    screen.blit(timer, (10, 10))

    if total_time - elapsed_time <= 0:
        game_result = 'Time Over'
        running = False

    for i in balloons:
        if i.rect.colliderect(character.rect):
            running = False

        for j in weapons:
            if i.rect.colliderect(j.rect):
                return_hits = i.hits()
                if i.size >= 4:
                    balloons.remove(i)
                else:
                    newballoon = im.Balls(i.position[0], i.position[1], i.size, i.speed_x)
                    balloons.append(newballoon)
                    weapons.remove(j)
            else:
                continue
            break

    if len(balloons) == 0:
        game_result = 'Mission Complete'
        running = False

    pygame.display.update()  # 게임화면 다시 그리기

    # 충돌체크

msg = game_font.render(game_result, True, (255, 255, 0))
screen.blit(msg, (300, 150))
pygame.display.update()

pygame.time.delay(1000)

pygame.quit()
