import pygame
import time
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

def main():
    pygame.init()
    game_size = (775, 230)


    gameDisplay = pygame.display.set_mode(game_size, pygame.RESIZABLE)
    pygame.display.set_caption("GAME")
    wind_size = pygame.Surface.get_size(gameDisplay)

    clock = pygame.time.Clock()

    user_obj_img = pygame.image.load('playeravatar.png')
    user_obj_img.convert_alpha()
    user_size = pygame.Surface.get_size(user_obj_img)


    game_map_img = pygame.image.load('gamemap.png')
    map_size = pygame.Surface.get_size(game_map_img)
    
    obsta_img  = pygame.image.load('obstacle_game.png')
    if wind_size[0]/game_size[0] < wind_size[1]/game_size[1]:
        game_map_img = pygame.transform.rotozoom(game_map_img, 0, int(wind_size[0]/game_size[0]))
        
    elif wind_size[0]/game_size[0] >= wind_size[1]/game_size[1]:
        game_map_img = pygame.transform.rotozoom(game_map_img, 0, int(wind_size[1]/game_size[1]))
        
    x_change_a, x_change_d, y_change_w, y_change_s = 0, 0, 0, 0

    x_user = 20
    y_user = 56
    
    
    ob_x1 = 250
    ob_y1 = 35
    
    ob_x2 = 575
    ob_y2 = 80
    
    ob_x3 = 250
    ob_y3 = 125
    
    ob_x4 = 575
    ob_y4 = 170
    
    ob_x5 = 0
    ob_y5 = 0
    
    
    
    spawn_user = (20, 56)
    refresh_rate = 144
    move_amount = (280/refresh_rate)
    #pygame.Surface.get_sizee() --> (width, height)
    #pygame.transform.scale(IMAGE, (width, height))
    crash = False
    while not crash:
        wind_size = pygame.Surface.get_size(gameDisplay)
        for event in pygame.event.get():
            print(event)
            
            if event.type == pygame.QUIT:
                crash = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    crash = True
                
                if event.key == pygame.K_w:
                    y_change_w = y_change_w -move_amount
                if event.key == pygame.K_a:
                    x_change_a = x_change_a-move_amount
                if event.key == pygame.K_s:
                    y_change_s = y_change_s+move_amount
                if event.key == pygame.K_d:
                    x_change_d = x_change_d + move_amount
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    x_change_a = 0
                elif event.key == pygame.K_w:
                    y_change_w = 0
                elif event.key == pygame.K_d:
                    x_change_d = 0
                elif event.key == pygame.K_s:
                    y_change_s = 0
        
        #BORDER LOGIC CONDITIONS FOR EACH LINE IN MAP IMG
        line1c = (x_user +x_change_a >=18) #ONLY ALLLOW IF RIGHT OF LINE 1
        line2c = (y_user + y_change_s +28 <= 200)
        line3c = (x_user +x_change_d +28 <=600 or x_user +x_change_d >=655) or (y_user+28<=90)
        line4c = (y_user +y_change_s+28<90) or (x_user + 30<=601 or x_user >= 655)
        line5c = (x_user + x_change_a >= 655 or x_user +x_change_a+28<600) or (y_user +28 <= 90)
        line6c = (y_user + y_change_s +28 <= 158) or (x_user <= 654)
        line7c = (x_user + x_change_d +28 <=730)
        line8c = (y_user + y_change_w >= 28)
        line9c = (x_user + x_change_a > 235 or x_user +x_change_a < 110) or (y_user >= 122)
        line10c= (y_user +y_change_w >= 122) or (x_user >235 or x_user +28 <=105)
        line11c= (x_user + x_change_d+28 <104 or x_user +x_change_d > 110) or (y_user >=122)
        line12c= (y_user + y_change_w >= 56) or (x_user >=115)
        #y_user + y_change_s+ 28 < pygame.Surface.get_size(gameDisplay)[1] 
        if line1c and line5c and line9c:
            x_user+=x_change_a
        if line3c and line7c and line11c:
            x_user+=x_change_d
        if line8c and line10c and line12c:
            y_user+=y_change_w
        if line2c and line4c and line6c:
            y_user+=y_change_s
        
        #game_map_img = pygame.transform.scale(game_map_img, (wind_size[0]-20, wind_size[1]-20))
        #MOVE OBSTACLE*************(655, 90)(730, 155)
        if ob_x1 <= 250:
            forward_ob1 = True
            backward_ob1 = False
        elif ob_x1>=575:
            forward_ob1 = False
            backward_ob1 = True
        if forward_ob1:
            ob_x1+=(move_amount*2)
            ob_x2-=(move_amount*2)
            ob_x3+=(move_amount*2)
            ob_x4-=(move_amount*2)
        elif backward_ob1:    
            ob_x1-=(move_amount*1.2)
            ob_x2+=(move_amount*1.2)
            ob_x3-=(move_amount*1.2)
            ob_x4+=(move_amount*1.2)
        #***********************1.2)****
        
        #CHECK IF USER HITS OBSTACLE*************
        check_ob1_col = ((ob_x1+30 >= x_user >= ob_x1) or (ob_x1+30 >= x_user+15 >= ob_x1) or (ob_x1+30 >= x_user+30 >= ob_x1)) and ((ob_y1+30 >=y_user>= ob_y1) or (ob_y1+30 >=y_user + 15>= ob_y1)or (ob_y1+30 >=y_user+30>= ob_y1))
        check_ob2_col = ((ob_x2+30 >= x_user >= ob_x2) or (ob_x2+30 >= x_user+15 >= ob_x2) or (ob_x2+30 >= x_user+30 >= ob_x2)) and ((ob_y2+30 >=y_user>= ob_y2) or (ob_y2+30 >=y_user + 15>= ob_y2)or (ob_y2+30 >=y_user+30>= ob_y2))
        check_ob3_col = ((ob_x3+30 >= x_user >= ob_x3) or (ob_x3+30 >= x_user+15 >= ob_x3) or (ob_x3+30 >= x_user+30 >= ob_x3)) and ((ob_y3+30 >=y_user>= ob_y3) or (ob_y3+30 >=y_user + 15>= ob_y3)or (ob_y3+30 >=y_user+30>= ob_y3))
        check_ob4_col = ((ob_x4+30 >= x_user >= ob_x4) or (ob_x4+30 >= x_user+15 >= ob_x4) or (ob_x4+30 >= x_user+30 >= ob_x4)) and ((ob_y4+30 >=y_user>= ob_y4) or (ob_y4+30 >=y_user + 15>= ob_y4)or (ob_y4+30 >=y_user+30>= ob_y4))
        if check_ob1_col or check_ob2_col or check_ob3_col or check_ob4_col:
            x_user = 20
            y_user = 56#RESETS USER POSITION BACK TO SPAWN
        
        
        #***************************************
        #CHECK IF IN FINISH****************************
        if 730>=x_user+15>=655 and 90<=y_user+15<=155:
            gameDisplay.fill(white)
            message_display("Level Completed", gameDisplay, game_size[0]/2, game_size[1]/2, 50)
            pygame.display.update()
            time.sleep(2)
            x_user = 20 
            y_user = 56
            
        else:
        #********************************************
        #DISPLAY OBJECTS****************
            gameDisplay.fill(white)
            gamemap(gameDisplay,game_map_img,  10, 10)
            user_obj(gameDisplay, user_obj_img, x_user, y_user)
            obsta(gameDisplay, obsta_img, ob_x1, ob_y1)
            obsta(gameDisplay, obsta_img, ob_x2, ob_y2)
            obsta(gameDisplay, obsta_img, ob_x3, ob_y3)
            obsta(gameDisplay, obsta_img, ob_x4, ob_y4)
        #************
        
        pygame.display.update()
        clock.tick(refresh_rate)
        
    pygame.quit()
def user_obj(gameDisplay, user_obj_img, x, y):
    gameDisplay.blit(user_obj_img, (x, y))
def gamemap(gameDisplay, game_map_img, x, y):
    gameDisplay.blit(game_map_img, (x, y))
def obsta(gameDisplay, obsta_img, x, y):
    gameDisplay.blit(obsta_img, (x, y))
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
def message_display(text, gameDisplay, x, y, size_font):
    largeText = pygame.font.Font('freesansbold.ttf',size_font)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x,y)
    gameDisplay.blit(TextSurf, TextRect)
if __name__ == "__main__":
    main()


