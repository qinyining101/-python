import pygame
import random

BLACK = (0,0,0)
WHITE = (255,255,255)
pygame.init()
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption('点破笑脸')
mousedown = False
keep_going = True
clock = pygame.time.Clock()
pic = pygame.image.load('CrazySmile.bmp')
colorkey = pic.get_at((0,0))
pic.set_colorkey(colorkey)
sprite_list = pygame.sprite.Group()
font = pygame.font.SysFont("Arial", 24)
count_smileys = 0
count_popped = 0
hits = 0
misses = 0

class Smiley(pygame.sprite.Sprite):
    def __init__(self, pos, xvel, yvel):
        pygame.sprite.Sprite.__init__(self)
        self.image = pic
        self.scale = random.randrange(10,100)
        self.image = pygame.transform.scale(self.image, (self.scale,self.scale))
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.x = pos[0] - self.scale/2
        self.rect.y = pos[1] - self.scale/2
        self.xvel = xvel
        self.yvel = yvel

    def update(self):
        self.rect.x += self.xvel
        self.rect.y += self.yvel
        if self.rect.x <= 0 or self.rect.x > screen.get_width() - self.scale:
            self.xvel = -self.xvel*0.95
        if self.rect.y <= 0 or self.rect.y > screen.get_height() - self.scale:
            self.yvel = -self.yvel*0.95

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                count_popped += len(sprite_list)
                sprite_list = pygame.sprite.Group() 

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]: 
                mousedown = True
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                clicked_smileys = [s for s in sprite_list if s.rect.collidepoint(pos)]
                sprite_list.remove(clicked_smileys)
                if len(clicked_smileys) > 0:
                    count_popped += len(clicked_smileys)
                    hits += 1       
                else:
                    misses += 1 

        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = True

    screen.fill(BLACK)
    sprite_list.update()
    sprite_list.draw(screen)
    clock.tick(60)

    draw_string = "Bubbles created: " + str(count_smileys)
    draw_string += " - Bubbles popped: " + str(count_popped)
    if count_smileys > 0:
        draw_string += " - Percent: "
        draw_string += str(round(count_popped * 100 / count_smileys, 1)) + "%"

    text = font.render(draw_string, True, WHITE)
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.y = 10
    screen.blit(text, text_rect)

    hit_string = "Total Clicks: " + str(hits + misses)
    hit_string += " - Hits: " + str(hits)
    if hits + misses > 0:
        hit_string += " - Percent: "
        hit_string += str(round(hits * 100 / (hits + misses), 1)) + "%"

    hit_text = font.render(hit_string, True, WHITE)
    hit_text_rect = hit_text.get_rect()
    hit_text_rect.centerx = screen.get_rect().centerx
    hit_text_rect.y = 550
    screen.blit(hit_text, hit_text_rect)

    pygame.display.update()

    if mousedown:
        speedx = 5
        speedy = 5
        newSmiley = Smiley(pygame.mouse.get_pos(), speedx, speedy)
        sprite_list.add(newSmiley)
        count_smileys += 1

pygame.quit()