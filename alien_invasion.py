# !/usr/bin/python
# coding:utf-8
##  上面两条注释可以解决 中文注释报错的问题  SyntaxError: Non-ASCII character



import pygame

from settings import Settings

from ship import Ship

import  game_functions as  gf

# 一个函数
def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien ")

    bg_color = (230, 230, 230)

    # 创建一艘飞船

    ship = Ship(screen)
    # 开始游戏的主循环
    while True:

        # 监视键盘和鼠标事件
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
            gf.check_event(ship)

            # # 每次循环时都重绘屏幕
            # screen.fill(bg_color)
            #
            # ship.blitme()
            #
            # # 让最近绘制的屏幕可见
            # pygame.display.flip()
            gf.update_screen(ai_settings,screen,ship)

# run_game()必须前面没有缩进，否则 pygame.display.flip()后面会报错，看来python虽然没有{}，但是是靠 缩进来比对代码块。
run_game()
