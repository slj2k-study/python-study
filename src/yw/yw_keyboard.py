import pygame


def figure_keboard(x,y):
    x_y = []
    for event in pygame.event.get():  # 이벤트 발생 체크
        if event.type == pygame.QUIT:  # 이벤트 발생 체크
            return [999,999];
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = 1
            if event.key == pygame.K_RIGHT:
                x = 2
            if event.key == pygame.K_UP:
                y = 1
            if event.key == pygame.K_DOWN:
                y = 2
        elif event.type == pygame.KEYUP:
            if x == 1 and event.key == pygame.K_LEFT :
                x = 0
            elif x == 2 and event.key == pygame.K_RIGHT:
                x = 0
            if y == 1 and event.key == pygame.K_UP :
                y = 0
            elif y == 2 and event.key == pygame.K_DOWN:
                y = 0

    x_y.append(x)
    x_y.append(y)
    return x_y
