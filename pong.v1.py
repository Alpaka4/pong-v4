import pygame
import sys
from config import *
from ball import Ball
from bat import Bat
# здесь определяются константы,
# классы и функции

def point_in_rect(px,py,rect_x,rect_y,rect_w,rect_h):
    inx=rect_x<=px<=rect_x+rect_w 
    iny=rect_y<=py<=rect_y+rect_h
    return inx and iny
     
# здесь происходит инициация,
# создание объектов
ball=Ball()
bat=Bat()
clock = pygame.time.Clock()
WHITE = (255, 255, 255)
ORANGE = (255,155,100)
BLACK = (0,0,0)
YELLOW = (255,180,0)
sc = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.font.init()




f2 = pygame.font.SysFont('algerian', 48)

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ball.update()
    bat.update()
    #передвигаем ракетку по экрану
    
    
    #проверяем что мяч попал в ракетку, правая граница
    #вычесляем середины сторон квадрата, описанного вокруг мяча
    mid_leftx=ball.x-ball.r
    mid_lefty=ball.y
     
    mid_rightx=ball.x+ball.r
    mid_righty=ball.y
     
    mid_topx=ball.x
    mid_topy=ball.y-ball.r
     
    mid_bottomx=ball.x
    mid_bottomy=ball.y+ball.r
    #правая граница ракетки №1
    if point_in_rect(mid_leftx,mid_lefty,bat.x,bat.y,BAT_WIDTH,BAT_HEIGHT):
        ball.speed_x=-ball.speed_x
    #верхняя граница ракетки №1
    if point_in_rect(mid_bottomx,mid_bottomy,bat.x,bat.y,BAT_WIDTH,BAT_HEIGHT):
        ball.speed_y=-ball.speed_y 
    #нижняя граница ракетки №1
    if point_in_rect(mid_topx,mid_topy,bat.x,bat.y,BAT_WIDTH,BAT_HEIGHT):
        ball.speed_x=-ball.speed_x
    #левая граница ракетки №2    
    if point_in_rect(mid_rightx,mid_righty,bat.x2,bat.y2,BAT_2_WIDTH,BAT_2_HEIGHT):
        ball.speed_x=-ball.speed_x
    #верхняя граница ракетки №2
    if point_in_rect(mid_bottomx,mid_bottomy,bat.x2,bat.y2,BAT_2_WIDTH,BAT_2_HEIGHT):
        ball.speed_y=-ball.speed_y 
    #нижняя граница ракетки №2
    if point_in_rect(mid_topx,mid_topy,bat.x2,bat.y2,BAT_2_WIDTH,BAT_2_HEIGHT):
        ball.speed_x=-ball.speed_x
    #score
    score_left_text = f2.render(str(ball.left_score), True,(YELLOW))
    score_right_text = f2.render(str(ball.right_score), True,(YELLOW))
    # заливаем фон
    sc.fill(BLACK)
    # счетчик очков
    # рисуем круг
    pygame.draw.circle(sc, ORANGE,(ball.x, ball.y), ball.r)
    pygame.draw.rect(sc, WHITE,(bat.x,bat.y,BAT_WIDTH,BAT_HEIGHT))
    pygame.draw.rect(sc, WHITE,(bat.x2,bat.y2,BAT_2_WIDTH,BAT_2_HEIGHT))

    # обновляем окно
    sc.blit(score_left_text, (SCREEN_WIDTH//2 -100, 10))
    sc.blit(score_right_text, (SCREEN_WIDTH//2 +100, 10))
    pygame.display.update()


    clock.tick(FPS)
