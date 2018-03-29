#time = input('분을 입력하시오:')
#time = int(time)    

#seconds = time * 60
#print('{0}초입니다'.format(seconds))

#while True:
#    a = int(input('나이를 입력하시오:'))

#    if a >= 8 and a <= 13:
#            print('초등학생입니다.')
#    elif a >= 14 and a <= 16:
#            print('중학생입니다.')
#    elif 17 <= a <= 19:
#            print('고등학생입니다.')
#b = 1

#a = input('숫자를 입력하시오:')
#a = int(a)

#while b <= a:
#    print(b * 2)
#    b = b + 1

#print('After he interrupted me')

#for i in range(2,9,2):
#    print('{0}times'.format(i))
#print('I had to put this out to him.')

#a = ['playing soccer','camping','an ice cream sunday','a subway sandwich','going to Wild Wadi']

#for i in a:
#    print('One of my favorite things is {0}'.format(i))

import random
import pygame
import time
life = 5
t = 70
pygame.init()
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT + 1,1000)
pygame.time.set_timer(pygame.USEREVENT + 2,5)
screen = pygame.display.set_mode((1200, 800))
done = False
is_blue = True
x = 30
y = 30
font = pygame.font.Font(None,24)

obstacles = [
       
        [0,100,1130,100,(255,0,255)],
        [700,300,700,200,(100,20,17)],
        [580,200,50,1000,(100,20,17)],
        [630,570,500,10,(190,20,10)],
        [700,650,500,10,(190,20,10)],
        [630,730,500,10,(190,20,10)],
        [630,740,50,50,(0,255,0)],
        [0,300,350,10,(190,20,10),'M'],
        [70,400,350,10,(190,20,10),'M'],
        [0,500,350,10,(190,20,10),'M'],
        [70,600,350,10,(190,20,10),'M'],
        [0,700,350,10,(190,20,10),'M'],
        [5,740,60,60,(234,59,30)]

        
]

while not done and life > 0:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
                if event.type == (pygame.USEREVENT + 1):
                        t = t - 1
                        if t == -1:
                                print('GAMEOVER')
                                done = True
                                time.sleep(2)
                if event.type == (pygame.USEREVENT + 2):
                        for o in obstacles:
                                if len(o) > 5:
                                        ra= random.randint(1,4)
                                        rb = random.randint(1, 25)
                                        if ra == 1:
                                                o[0] -= rb
                                                if o[0] < 0:
                                                        o[0] = 0
                                        elif ra == 2:
                                                o[0] += rb
                                                if o[0] > 280:
                                                        o[0] = 280


        if is_blue:
                xy = 2
        else:
                xy = 10

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: 
                y -= xy
                if y < 0:
                        y = 0
        if pressed[pygame.K_DOWN]: 
                y += xy
                if (y+60) > 800:
                        y = 800-60
        if pressed[pygame.K_LEFT]: 
                x -= xy
                if x < 0:
                        x = 0
        if pressed[pygame.K_RIGHT]: 
                x += xy
                if (x+60) > 1200:
                        x = 1200-60
        
        screen.fill((255, 255, 255))
        if is_blue: color = (221, 215, 19)
        else: color = (255, 100, 0)
        
        player_rect = pygame.Rect(x,y,60,60)
        pygame.draw.rect(screen, color, player_rect)
       
        for i in obstacles:
                obs_rect = pygame.Rect(i[0],i[1],i[2],i[3])
                pygame.draw.rect(screen, i[4],obs_rect)
               
                if obs_rect.colliderect(player_rect):
                        if i[4] == (0, 255, 0):
                                t = t + 10
                                x = 30
                                y = 210
                        elif i[4] == (234,59,30):
                                print('GAMECLEAR')
                                done = True
                                time.sleep(3)
                        else:
                                x = 30
                                y = 30
                                life -= 1
                                print('life:{0}'.format(life))
        text = font.render('{0} seconds'.format(t), True, (255,0,0),(255,255,255))
        textrect = pygame.Rect(10, 10, 100, 100)
        screen.blit(text, textrect)

        lifetext = font.render('{0} life'.format(life), True, (0,0,255),(255,255,255))
        lifetextrect = pygame.Rect(150, 10, 100, 100)
        screen.blit(lifetext, lifetextrect)
        pygame.display.flip()

        clock.tick(80)