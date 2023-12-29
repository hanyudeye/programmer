import pygame
import sys
import random

from pygame.locals import *

# 设置窗口大小
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# 设置颜色

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 蛇的大小
SNAKE_SIZE = 20
SNAKE_SPEED = 20

# 初始化窗口
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("贪食蛇 Snake Game")

# 蛇的初始位置
snake_position = [100, 100]

#蛇的初始长度
snake_body = [[100, 100], [90, 100], [80, 100]]

# 初始食物位置
food_position = [
    random.randrange(1, (WINDOW_WIDTH // SNAKE_SIZE)) * SNAKE_SIZE,
    random.randrange(1, (WINDOW_HEIGHT // SNAKE_SIZE)) * SNAKE_SIZE
]

food_spawn = True

# 设置初始方向
direction = 'RIGHT'
change_to = direction

# 控制速度

clock = pygame.time.Clock()



# 游戏主循环

while True:

    for event in pygame.event.get():

        if event.type == KEYDOWN:

            if event.key == K_UP:
                change_to = 'UP'
            if event.key == K_DOWN:
                change_to = 'DOWN'
            if event.key == K_LEFT:
                change_to = 'LEFT'
            if event.key == K_RIGHT:
                change_to = 'RIGHT' 
                
            # change_to = '正确'


# 确保蛇不能直接掉头
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

# 蛇的移动

        if direction == 'UP':
            snake_position[1] -= SNAKE_SPEED
        if direction == 'DOWN':
            snake_position[1] += SNAKE_SPEED
        if direction == 'LEFT':
            snake_position[0] -= SNAKE_SPEED
        if direction == 'RIGHT':
            snake_position[0] += SNAKE_SPEED

# 蛇身体增长

        snake_body.insert(0, list(snake_position))
        if snake_position == food_position:
            food_spawn = False
        else:
            snake_body.pop()

# 食物生成

        if not food_spawn:
            food_position = [random.randrange(1, (WINDOW_WIDTH // SNAKE_SIZE)) * SNAKE_SIZE, 
            random.randrange(1, (WINDOW_HEIGHT // SNAKE_SIZE)) * SNAKE_SIZE]
            food_spawn = True

# 清屏

        window.fill(BLACK)

# 画蛇
        for position in snake_body:
            pygame.draw.rect(window, GREEN, pygame.Rect(position[0], position[1], SNAKE_SIZE, SNAKE_SIZE))

# 画食物

        pygame.draw.rect(window, RED, pygame.Rect(food_position[0], food_position[1], SNAKE_SIZE, SNAKE_SIZE))
        # pygame.draw.rect(window, RED, pygame.矩形（food_position[0]， food_position[1]， SNAKE_SIZE， SNAKE_SIZE））

# 刷新屏幕
        pygame.display.flip()

# 检查碰撞

        if snake_position[0] < 0 or snake_position[0] > WINDOW_WIDTH - SNAKE_SIZE:
            sys.exit()

        if snake_position[1] < 0 or snake_position[1] > WINDOW_HEIGHT - SNAKE_SIZE:
            sys.exit()

        for block in snake_body[1:]:

            if snake_position == block:
                sys.exit()

# 控制游戏速度

        clock.tick(15)