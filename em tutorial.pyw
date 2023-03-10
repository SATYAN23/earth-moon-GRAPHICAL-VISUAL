import os
import math as m
import pygame
from datetime import datetime
import time
import pyautogui
width, height = pyautogui.size()
pygame.init()


os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %((73.15*width)/100, (46.67*height)/100)
i_icon = os.getcwd() + '.\p.png'
icon = pygame.image.load(i_icon)
pygame.display.set_icon(icon)
speed =0

def main():
    global speed
    color = (0, 255, 0)

    width = 500
    height = 500
    r = 200
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("earth-moon-relation")
    font = pygame.font.SysFont("Segoe UI", 24)
    clock = pygame.time.Clock()
    cpt = win.get_rect().center


    distance = (2*3.14*r)/(8000/2100)
    distance =  str(distance)
    print("distance of moon to earth : " + distance)
    
        
    run = True
    while run:
        clock.tick(8000/2100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False    
        


        #circle and spline lines
                

        
        for i in range(0, 720):
            win.fill((255, 255, 255))


            S = "distance of moon" +  " : "  + str(distance) + "units"
            draw3 = font.render(str(S), True, color)
            win.blit(draw3,(10,10))

        
            pygame.draw.circle(win, (71, 186,53),[r+50 +r*m.sin(m.radians(i)),r+50+r*m.cos(m.radians(i))],12,12)

            pygame.draw.circle(win, (51, 255,51),[250,250],200,2)
            pygame.draw.circle(win, (71, 186,53),[cpt[0],cpt[1]],25,25)

            pygame.draw.line(win, (0, 255,0), (250,50), (250,450))
            pygame.draw.line(win, (0, 255,0), (50,250), (450,250))

            pygame.draw.line(win,(0, 255,0), (r + 50 + r * m.cos(m.radians(135)),r + 50 +  r * m.sin(m.radians(135))),
                         (r + 50 -r * m.cos(m.radians(135)) ,r +50 - r * m.sin(m.radians(135))))

            pygame.draw.line(win,(0, 255,0), (r + 50 - r * m.cos(m.radians(45)),r +50 - r * m.sin(m.radians(45))),
                         (r + 50+r * m.cos(m.radians(45)) ,r + 50+ r * m.cos(m.radians(45))))
            pygame.display.update()

        pygame.display.update()
        
    pygame.quit()
      
if __name__ == "__main__":
    main() 
















                
