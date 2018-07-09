# !/usr/bin/python
# coding:utf-8
##  上面两条注释可以解决 中文注释报错的问题  SyntaxError: Non-ASCII character

import sys

import pygame


def check_event(ship):
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                 ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

def update_screen(ai_settings, screen, ship):
    """更新屏幕上的图像，并切换到主屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(
        ai_settings.bg_color)  # ai_settings.bg_color可以点击进去，真的好神奇，就好像(ai_settings,screen,ship)是Java的(Settings ai_settings,screen,ship)一样

    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()
