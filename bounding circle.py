#开始必备操作
import pygame
import sys
pygame.init()
#设置窗口
width,height=800,600
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("bounding circle")
#设置颜色
BLACK=(0,0,0)
RED=(255,0,0)
#⚪的属性
circle_r=30
circle_x=width//2
circle_y=height//2
speed_x=3
speed_y=3
