import pygame
from random import randint
pygame.init()

setting_win = {
    "WIDTH": 1000,
    "HEIGHT": 600,
    "FPS": 60
}
setting_hero = {
    "WIDTH": 200,
    "HEIGHT": 150,
    "HP": 5
}
setting_bot = {
    "WIDTH": 80,
    "HEIGHT": 100
}

setting_boss = {
    "WIDTH": 400,
    "HEIGHT": 200
}

bot_list = list()
bullet_bot_boss_list= list()

hero_image_list = [
    pygame.transform.scale(pygame.image.load("image\\hero_1.png"), (setting_hero["WIDTH"], setting_hero["HEIGHT"])),
    pygame.transform.scale(pygame.image.load("image\\hero_2.png"), (setting_hero["WIDTH"], setting_hero["HEIGHT"]))
]
bot_image_list = [
    pygame.transform.scale(pygame.image.load("image\\bot_1.png"), (setting_bot["WIDTH"], setting_bot["HEIGHT"])),
    pygame.transform.scale(pygame.image.load("image\\bot_2.png"), (setting_bot["WIDTH"], setting_bot["HEIGHT"]))
]
boss_image_list = [
    pygame.transform.scale(pygame.image.load("image\\Boss_bot_1.png"), (setting_boss["WIDTH"], setting_boss["HEIGHT"])),
    pygame.transform.scale(pygame.image.load("image\\Boss_bot_2.png"), (setting_boss["WIDTH"], setting_boss["HEIGHT"]))
]
bg_image = pygame.transform.scale(pygame.image.load("image\\bg.png"), (setting_win["WIDTH"], setting_win["HEIGHT"]))

