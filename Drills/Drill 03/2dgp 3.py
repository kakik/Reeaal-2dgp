from pico2d import *
import math


open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

isrect = True
rectway=3 
x = 400
y=90
angle=270

while(True):
    clear_canvas_now()
    grass.draw_now(400, 30)
    
    if(isrect==True):
        if(rectway==1):            
             character.draw_now(x, y)
             x = x - 2
             delay(0.01)

             if(x<=50):
                 rectway=4

        elif(rectway==2):
             character.draw_now(x, y)
             y = y + 2
             delay(0.01)

             if(y>=490):
                 rectway=1

        elif(rectway==3):
            if(398<=x&x<400):
                isrect=False
        
            character.draw_now(x, y)
            x = x +2
            delay(0.01)

            if(x>=750):
                rectway=2

        elif(rectway==4):
             character.draw_now(x, y)
             y = y -2
             delay(0.01)

             if(y<=90):
                 rectway=3
                 
    elif(isrect==False):     
        character.draw_now(x, y)
        angle=angle+1
        
        x=400.0+math.cos(angle/180*math.pi)*200.0
        y=290.0+math.sin(angle/180*math.pi)*200.0
        delay(0.01)

        if((angle%360)==269):
            isrect=True
            x=400
            y=90
