import pygame
import os


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class ImageControl:
    def __init__(self, adrress):
        self.image = pygame.image.load(resource_path(adrress))
        temp = self.image.get_rect().size
        self.width = temp[0]
        self.height = temp[1]
        self.position = [0, 0]
        self.rect = self.image.get_rect()
        self.rect.left = temp[0]
        self.rect.top = temp[1]
        self.v_accelx = 0
        self.v_accely = 0
        self.alive = True
        self.speed = 0

    def movement(self, x, y):
        self.position[0] += x
        self.position[1] += y
        self.rect.left = self.position[0]
        self.rect.top = self.position[1]


class Balls:
    balloon_img = [pygame.image.load(
        resource_path('C:\\Users\\YoungWoo\\Desktop\\git\\python-study\\src\\yw\\pygame_project\\images\\balloon1.png')),
        pygame.image.load(
        resource_path('C:\\Users\\YoungWoo\\Desktop\\git\\python-study\\src\\yw\\pygame_project\\images\\balloon2.png')),
        pygame.image.load(
        resource_path('C:\\Users\\YoungWoo\\Desktop\\git\\python-study\\src\\yw\\pygame_project\\images\\balloon3.png')),
        pygame.image.load(
        resource_path('C:\\Users\\YoungWoo\\Desktop\\git\\python-study\\src\\yw\\pygame_project\\images\\balloon4.png'))]

    def __init__(self, x, y, size, m_speedx=0):
        self.size = size
        self.image = Balls.balloon_img[size]
        temp = self.image.get_rect().size
        self.width = temp[0]
        self.height = temp[1]
        self.position = [x, y]
        self.rect = self.image.get_rect()
        self.rect.left = self.position[0]
        self.rect.top = self.position[1]
        if m_speedx == 0:
            self.speed_x = 10
        else:
            self.speed_x = m_speedx * -1
        self.speed_y = 10

    def hits(self):
        self.size += 1
        if self.size < 4:
            self.image = Balls.balloon_img[self.size]
            temp = self.image.get_rect().size
            self.width = temp[0]
            self.height = temp[1]
            self.rect.left = self.position[0]
            self.rect.top = self.position[1]

    def calc(self, background_width=640, background_height=480 - 50):
        if self.position[0] < 0 or self.position[0] + self.width >= background_width:
            self.speed_x *= -1
        if self.position[1] + self.height > background_height:
            self.speed_y = -10
        else:
            self.speed_y += 0.2

    def process(self):
        self.position[0] += self.speed_x
        self.position[1] += self.speed_y

        self.rect.left = self.position[0]
        self.rect.top = self.position[1]
