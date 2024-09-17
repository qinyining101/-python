import pygame  
import random

# 初始化Pygame
pygame.init()

# 设置屏幕尺寸
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("黑客帝国代码雨")

# 设置字体
font = pygame.font.SysFont('monospace', 20)

# 定义字符范围
chars = [chr(i) for i in range(33, 127)]

# 定义代码雨的列
cols = screen_width // 20
drops = [0] * cols

# 定义颜色
green = (0, 255, 0)
black = (0, 0, 0)

# 游戏循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 填充黑色背景
    screen.fill(black)

    for i in range(len(drops)):
        # 随机选择一个字符
        char = random.choice(chars)
        # 渲染字符
        text = font.render(char, True, green)
        # 在当前窗口绘制字符
        screen.blit(text, (i * 20, drops[i] * 20))
        # 更新下落位置
        drops[i] += 1
        # 如果超出屏幕高度，重置到顶部
        if drops[i] * 20 > screen_height or random.random() > 0.95:
            drops[i] = 0

    # 更新屏幕
    pygame.display.flip()
    # 控制帧率 50帧
    pygame.time.delay(50)

# 退出Pygame
pygame.quit()
