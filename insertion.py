import pygame
import time
import random
pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption('visualization')
run=True
blue=(0,0,150)
lblue=(229,204,255)
h=[]
n=random.randint(20,35)
print(n)
i=0
while(i<n):
    h.append(random.randint(20,400))
    i+=1
#print(h)
i=0
k=0
m=0
p=0
q=0
#draw.rect(a,b,c,d) where a,b=x,y coordinate of top left
#c=width,d=height
while run:
    screen.fill((255,255,255))
    i=0
    while(i<n):

        pygame.draw.rect(screen,blue,(40+24*i,595-h[i],20,h[i]))
        i+=1

    if(p<n):
        q=p+1
        while(q<n):
            if(h[q]<h[p]):
                h[q],h[p]=h[p],h[q]
                pygame.draw.rect(screen,blue,(40+24*p,595-h[p],20,h[p]))
                pygame.draw.rect(screen,blue,(40+24*q,595-h[q],20,h[q]))
                pygame.draw.rect(screen,blue,(40+24*(q-1),595-h[q-1],20,h[q-1]))
                pygame.display.update()
                clock.tick(20)
                q+=1
            else:
                pygame.draw.rect(screen,lblue,(40+24*q,595-h[q],20,h[q]))
                if(q>0):
                    pygame.draw.rect(screen,blue,(40+24*(q-1),595-h[q-1],20,h[q-1]))
                pygame.display.update()
                clock.tick(20)
                q+=1

        p+=1





    #if(k<n):
        #if(k>0):
            #pygame.draw.rect(screen,blue,(40+24*(k-1),595-h[k-1],20,h[k-1]))
        #pygame.draw.rect(screen,lblue,(40+24*k,595-h[k],20,h[k]))
        #k+=1

        #pygame.display.update()
        #clock.tick(5)
        #time.sleep(100)



    mouse=pygame.mouse.get_pos()
    #print(mouse)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.display.update()
