import sys
import pygame
import random
import time


class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Trash collecting tycoon")
        self.screen = pygame.display.set_mode((900, 900))
        self.clock = pygame.time.Clock()

        self.character_image = pygame.image.load("img/Player.png")
        self.character_image = pygame.transform.scale(self.character_image, (60, 130)) 
        self.char_x = 0
        self.char_y = 0

        self.extra = 1
        self.sped = 0
        self.AC = 0
        self.extracost = 4
        self.spedcost = 5
        self.ACcost = 15


        self.time = 0
        self.ACtimestart = 0
        self.ACtimeend = 0
        self.trash = 0
        self.texttrash = "Trash : " + str(self.trash)

    def Main_menu(self):
        

        self.background_image = pygame.image.load("img/Main-menu.png")
        self.Buttons_image = pygame.image.load("img/Start.png")
        self.Buttons_image = pygame.transform.scale(self.Buttons_image, (326, 132))
        self.Buttons_rect = self.Buttons_image.get_rect (center = (450, 270))
        self.RButtons_image = pygame.image.load("img/Restart.png")
        self.RButtons_image = pygame.transform.scale(self.RButtons_image, (326, 132))
        self.RButtons_rect = self.RButtons_image.get_rect (center = (450, 490))
        
        

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit
                    sys.quit
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.Buttons_rect.collidepoint(event.pos):
                        self.char_x, self.char_y = 375, 600
                        self.Background()
                    

        
            
                        
            self.screen.blit(self.background_image, (0,0 ))
            self.screen.blit(self.Buttons_image, self.Buttons_rect)
            self.screen.blit(self.RButtons_image, self.RButtons_rect)
            
            pygame.display.update()
            self.clock.tick(60)

    def Background(self):
        
        self.list_trash = []
        self.start = time.time()
        self.random_time = random.randint(3, 7)



        self.background_image = pygame.image.load("img/Background.png")
        self.character_image = pygame.image.load("img/Player.png")
        self.character_image = pygame.transform.scale(self.character_image, (60, 130)) 
        self.floor_image = pygame.image.load("img/Terrain.png")
        self.floor_image = pygame.transform.scale(self.floor_image, (900, 225   ))  
        self.Floor_rect = self.floor_image.get_rect(topleft=(0, 820)) 
        self.Trash_image = pygame.image.load("img/Trash.png")
        self.Trash_image = pygame.transform.scale(self.Trash_image, (80, 80))  
        self.Ground_image = pygame.image.load("img/Floor.png")
        self.Ground_image = pygame.transform.scale(self.Ground_image, (900, 300))
        self.HOUSE_image = pygame.image.load("img/House.png")
        self.HOUSE_image = pygame.transform.scale(self.HOUSE_image, (130, 160))
        self.houserect = self.HOUSE_image.get_rect(topleft=(40, 680))
        
        

        # Character properties
        textx,texty = 600, 50
        char_velocity_x = 0
        char_velocity_y = 0
        gravity = 1
        jump_power = -15
        on_floor = False


        self.texttrash = "Trash : " + str(self.trash)
        font = pygame.font.Font('freesansbold.ttf', 32)
        self.text = font.render(self.texttrash, True, "black")
        self.textRect = self.text.get_rect()
        self.textRect.topleft = (textx, texty)
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        char_velocity_x = 5  + self.sped
                    if event.key == pygame.K_LEFT:
                        char_velocity_x = -5  - self.sped
                    if event.key == pygame.K_UP and on_floor:  
                        char_velocity_y = jump_power

                    if event.key == pygame.K_d:
                        char_velocity_x = 5  + self.sped
                    if event.key == pygame.K_a:
                        char_velocity_x = -5  - self.sped
                    if event.key == pygame.K_w and on_floor:  
                        char_velocity_y = jump_power
                    if event.key == pygame.K_e:
                        touched, num = self.touching_trash(self.char_x, self.list_trash)
                        housed = self.touching_house(self.char_x,40)
                        if touched:
                            self.list_trash.remove(self.list_trash[num])
                            self.trash += self.extra
                            print("Trash:", self.trash)
                            self.texttrash = "Trash :" + str(self.trash)
                            self.text = font.render(self.texttrash, True, "black")
                            textRect = self.text.get_rect()
                            textRect.topleft = (textx, texty)

                        elif housed:
                            self.char_x, self.char_y = 700, 600 
                            self.house()

                if event.type == pygame.KEYUP:
                    if event.key in [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_d, pygame.K_a]:
                        char_velocity_x = 0  

            
            char_velocity_y += gravity

            
            self.char_x += char_velocity_x
            self.char_y += char_velocity_y

            
            if self.char_y + 130 > self.Floor_rect.top:  
                if self.Floor_rect.left <= self.char_x <= self.Floor_rect.right or \
                self.Floor_rect.left <= self.char_x + 130 <= self.Floor_rect.right:
                    self.char_y = self.Floor_rect.top - 130 
                    char_velocity_y = 0  
                    on_floor = True
                else:
                    on_floor = False
            else:
                on_floor = False


            if self.time != 0:
                self.ACtimeend = time.time()
                if self.ACtimeend - self.ACtimestart > self.time:
                    self.ACtimestart = time.time()
                    self.trash += 1
                



            self.char_x = max(0, min(self.char_x, 850))  

            # Draw background, floor, and character
            self.screen.blit(self.background_image, (0, 0))
            self.screen.blit(self.floor_image, self.Floor_rect.topleft)  
            self.screen.blit(self.HOUSE_image, self.houserect.topleft)
            self.screen.blit(self.character_image, (self.char_x, self.char_y))
            self.screen.blit(self.text, self.textRect)
            

            self.end = time.time()
            if self.end - self.start > self.random_time:
                self.start = time.time()
                self.random_time = random.randint(3, 7)
                if len(self.list_trash) < 4:
                    self.list_trash.append([random.randint(300, 800), 770])
                    
            

            #Trash appearance randomly
            for item in self.list_trash:
                self.Trash_rect = self.Trash_image.get_rect(topleft=(item[0], item[1])) 
                self.screen.blit(self.Trash_image, self.Trash_rect.topleft)

            pygame.display.update()
            self.clock.tick(60)



    def house(self):
        self.Inside_image = pygame.image.load("img/Inside_house.png")
        self.Ground_rect = self.Ground_image.get_rect(topleft=(0, 820)) 
        self.computer_image = pygame.image.load("img/Computer.png")
        self.computer_image = pygame.transform.scale(self.computer_image, (80,80))  
        self.DOOR_image = pygame.image.load("img/Door.png")
        self.DOOR_image = pygame.transform.scale(self.DOOR_image, (125, 150))
        self.doorrect = self.DOOR_image.get_rect(topleft = (700, 680))
       
        
        
        self.computer_rect = self.computer_image.get_rect(topleft=(160, 720))
        # Character properties
         
        char_velocity_x = 0
        char_velocity_y = 0
        gravity = 1
        jump_power = -15
        on_floor = False

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        char_velocity_x = 5  + self.sped
                    if event.key == pygame.K_LEFT:
                        char_velocity_x = -5  - self.sped
                    if event.key == pygame.K_UP and on_floor:  
                        char_velocity_y = jump_power

                    if event.key == pygame.K_d:
                        char_velocity_x = 5  + self.sped
                    if event.key == pygame.K_a:
                        char_velocity_x = -5  - self.sped
                    if event.key == pygame.K_w and on_floor:  
                        char_velocity_y = jump_power
                    if event.key == pygame.K_e:
                        door_touched = self.touching_door(self.char_x, 700)
                        PCtouched = self.touching_PC(self.char_x, 160)
                        if door_touched:
                            self.char_x, self.char_y = 60, 600
                            self.Background()
                            
                        elif PCtouched:
                            self.PC()

                if event.type == pygame.KEYUP:
                    if event.key in [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_d, pygame.K_a]:
                        char_velocity_x = 0  

            
            char_velocity_y += gravity

            
            self.char_x += char_velocity_x
            self.char_y += char_velocity_y

            
            if self.char_y + 130 > self.Ground_rect.top:  
                if self.Ground_rect.left <= self.char_x <= self.Ground_rect.right or \
                self.Ground_rect.left <= self.char_x + 130 <= self.Ground_rect.right:
                    self.char_y = self.Ground_rect.top - 130 
                    char_velocity_y = 0  
                    on_floor = True
                else:
                    on_floor = False
            else:
                on_floor = False


            self.char_x = max(0, min(self.char_x, 850))  

            # Draw background, floor, and character
            self.screen.blit(self.Inside_image, (0, 0))
            self.screen.blit(self.Ground_image, self.Floor_rect.topleft) 
            self.screen.blit(self.computer_image, self.computer_rect.topleft) 
            self.screen.blit(self.DOOR_image, self.doorrect.topleft)
            self.screen.blit(self.character_image, (self.char_x, self.char_y))
            self.screen.blit(self.text, self.textRect)
            


                    
        
            pygame.display.update()
            self.clock.tick(60)
    
    def PC(self):
        self.bbackground_image = pygame.image.load("img/Menu.png")
        self.yesButtons_image = pygame.image.load("img/Moretrash.png")
        self.yesButtons_image = pygame.transform.scale(self.yesButtons_image, (326, 132))
        self.yesButtons_rect = self.yesButtons_image.get_rect (center = (450, 660))
        self.spedButtons_image = pygame.image.load("img/Sped.png")
        self.spedButtons_image = pygame.transform.scale(self.spedButtons_image, (326, 132))
        self.spedButtons_rect = self.spedButtons_image.get_rect (center = (260, 490))
        self.ACButtons_image = pygame.image.load("img/Autocollect.png")
        self.ACButtons_image = pygame.transform.scale(self.ACButtons_image, (326, 132))
        self.ACButtons_rect = self.ACButtons_image.get_rect (center = (665, 490))
        self.backButtons_image = pygame.image.load("img/Back.png")
        self.backButtons_image = pygame.transform.scale(self.backButtons_image, (326, 132))
        self.backButtons_rect = self.backButtons_image.get_rect (center = (450, 800))


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit
                    sys.quit
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.backButtons_rect.collidepoint(event.pos):
                        self.char_x, self.char_y = 160, 600
                        self.house()
                    if self.yesButtons_rect.collidepoint(event.pos):
                        if self.trash >= self.extracost:
                            self.trash -= self.extracost
                            self.extra += 1
                            self.extracost *= 3
                    if self.spedButtons_rect.collidepoint(event.pos):
                        if self.trash >= self.spedcost:
                            self.trash -= self.spedcost
                            self.sped +=2
                            self.spedcost *= 3
                    if self.ACButtons_rect.collidepoint(event.pos):
                        if self.trash >= self.extracost:
                            self.trash -= self.extracost
                            if self.time == 0:
                                self.time = 60
                            else:
                                self.time -= 5
                
                    
            self.screen.blit(self.bbackground_image, (0,0 ))
            self.screen.blit(self.yesButtons_image, self.yesButtons_rect)
            self.screen.blit(self.spedButtons_image, self.spedButtons_rect)
            self.screen.blit(self.ACButtons_image, self.ACButtons_rect)
            self.screen.blit(self.backButtons_image, self.backButtons_rect)
            self.screen.blit(self.text, self.textRect)
            
            pygame.display.update()
            self.clock.tick(60)

        
    def touching_PC(self, char_x, door_x):
        touched = False
        if door_x <= char_x <= door_x + 80 or \
        door_x + 80 >= char_x + 60 >= door_x:
            touched = True
        return touched

    def touching_trash(self, char_x,  list_trash):
        touched = False
        num = 0
        for item in list_trash:
            if item[0] <= char_x <= item[0] + 80 or \
            item[0] + 80 >= char_x + 60 >= item[0]:
                touched = True
                break
            num += 1
        return touched, num

    def touching_house(self, char_x, house_x):
        touched = False
        if house_x <= char_x <= house_x + 130 or \
        house_x + 130 >= char_x + 60 >= house_x:
            touched = True
          
        return touched
    
    def touching_door(self, char_x, door_x):
        touched = False
        if door_x <= char_x <= door_x + 125 or \
        door_x + 125 >= char_x + 60 >= door_x:
            touched = True
        return touched
            
    
Game().Main_menu()