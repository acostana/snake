# -*- coding: utf-8 -*-
"""
Created on Fri May 29 23:21:12 2020

Author: Ana Acosta
Date: 05.29.20
Project: CS 112, Final Project, snake.py
"""


import pygame #import pygame 
import random #import random -- to choose locations for food randomly
import math #import math -- to calculate distance

pygame.init()



"""
Cube class - for objects like food and snake segments
"""

class Cube():
    """
    init method takes and sets two values which will represent the x and y coordinates of our cube
    """
    def __init__ (self,x,y): 
        self.x = x 
        self.y = y
  
    """
    draw method will be used to draw cubes that make up the snake
    """
    def draw(self, win): #takes in a window
        
            #for loop checks if the player closes the window and if so it quits
            for event in pygame.event.get():
                if event.type== pygame.QUIT:
                    pygame.quit()
                    
            pygame.draw.rect(win, (255,0,0), (self.x, self.y, 30,30 )) #use pygame draw method to draw cube passing in the coordinates of the cube
            pygame.display.update() #updates window so the cube gets drawn
            
"""
Takes in a window and displays the player's score
"""
def disp_score(window):
    
    
    global score ##make score global so we can use it here
    
    font = pygame.font.Font('freesansbold.ttf', 30) #set the font for the text
    message = font.render("Score: " + str(score), True, (0,255,0)) #construct the message passing in the text, score, and color of text
    messageRect = message.get_rect() #get a rectangle for the text
    messageRect.center = (300,20) #choose location for rectangle
    

        
  
    window.blit(message, messageRect) #display message
    
    pygame.display.update() 
    
    
    #for loop checks and quits window if user closes window
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()


"""
this method takes in a window and siplays a message. This method is called when a crash with the 
boundaries of the window occurs
"""
def crash(window):

    font = pygame.font.Font('freesansbold.ttf', 32) #sets font for message
    message = font.render("You crashed!", True, (0,255,0)) #constructs message and sets location and color
    messageRect = message.get_rect()  
    messageRect.center = (300,300) #the location for the message will be the middle of the window
    

    while(True):

        window.blit(message, messageRect) #displays message
        
        pygame.display.update()

        #for loop checks and sees if user closes window
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
        
            
"""
Takes in  a window. Checks if the snake crashes against itself
"""               
def self_crash(window):
    global fx,fy #makes food coordinates global

    #loop will iterate through the array with the exception of last Cube going backwards
    for i in range(len(body)-2, -1,-1):
        #calculate the distance between the last Cube and the rest of the cubes
        distance = math.hypot(body[len(body)-1].x - body[i].x,body[len(body)-1].y- body[i].y ) 
        #if the distance between the last Cube and the current Cube is less than 30 that means they collided
        if distance < 30:
            crash(window) #calls crash


"""
This method adds a segment to the body of the snake and increments score. This is called when there is a collision 
between head of snake and food
"""
def eat():
    #makes variables global so we can use them
    global score
    global fx,fy #these are the food coordinates
  
    #creates and object Cube using food coordinates. 
    #coodinates fx and fy here don't matter because they will later be adjusted when drawn
    food = Cube(fx,fy)
    body.insert(0,food) #inserts the new object at the beginning of the array(body of snake)
    score += 1 # increments score by 1          

"""
This method takes in a window and next x and y coordinates.
The next_x and y at first are the previous coordinates of the snake head which gets updated after
each element in body is drawn. This way we are moving each Cube to the previous loocation
of the next element so they all follow the head and one another.
"""
def followHead(win, next_x, next_y):
    #the loop will iterate through the body of the snake backwards with the exception of head(last Cube) 
    for i in range(len(body)-2, -1, -1):
        prev_x = body[i].x #this variable stores the current x coordinate of the current Cube
        prev_y = body[i].y 
        body[i].x = next_x #set the x coordinate to be next_x coordinate
        body[i].y = next_y
        next_x = prev_x #update the next_ coordinate to be the x coordinate that we saved previously
        next_y = prev_y
        body[i].draw(win) #draw the Cube using its new coordinates
        pygame.display.update()
    
                

            
"""
This method takes nothing in but returns two values. This is used to select the coordinates of the food 
"""                
def chooseFood():
    w = random.randrange(30,570, 30) #use random to select an x coordinate taht will not go out of boundaries
    z = random.randrange(30,570,30)  #coordinates are multiples of 30 since our snake moves by 30
    return w,z #return the coordinates      

"""
This method will draw the food. Takes in a window and two values(coordinates)
"""
def feed (window, f_x, f_y):
    
        pygame.draw.rect(window, (0,255,0), (f_x, f_y, 30, 30))  #use pygame draw method to draw food using its coordinates
        
        pygame.display.update()
        
        #for loop check and quits game if user closes window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
       
        
        

"""
This method takes in a window. This method is used to move the snake to the left.
User can only move down or up when its going left
"""
def moveLeft(window):
    
    global fx,fy ##makes food coordinates global
    
    #loop runs until user crashed or user presses another key or user closes window
    
    while(True):
        
        pygame.time.delay(80) #delay time 
        
        #check and quit pygame if user closes the window
        for event in pygame.event.get():
                if event.type== pygame.QUIT:
                    pygame.quit()
                    
        keys = pygame.key.get_pressed() #stores the keys the user presses
        


        if(keys[pygame.K_DOWN]): #if the user presses down
            moveDown(window) #call moveDown method
      
            
        elif(keys[pygame.K_UP]): #if user presses up
            moveUp(window) #call move up method
            
        
        #clear the window so that we canredraw things in a different location, making objects move
        window.fill((0,0,0))
        
      
        
        feed(window, fx, fy) #call feed to draw the food
        
        
        head = body[len(body)-1] #set head variable to be the last Cube in the body
        
   
     
        prev_x = head.x #this will dave the current coordinate of the head before changing it
        prev_y = head.y
  
        head.x -= velocity #change coordinate of head subtracting velocity(30) so that it moves to the left by 30
        head.draw(window) #draw the head in its new location
        pygame.display.update()

        distance = math.hypot(head.x - fx,head.y- fy ) #get the distance between head and food 
        
        
        if(distance < 30): #if head collides with food call eat
            eat()
            fx, fy = chooseFood() #call choose food to get new coordinates for food
        disp_score(window) #display the score
        
        followHead(window, prev_x, prev_y) #call followHead and pass to it the previous coordinates of the head
        
        if head.x < 0: #check if the head crashed against the left boundary
            crash(window) #call crash
     
        
        self_crash(window) #check if the snake crashed against itself
      
     
        
    
"""
This method is used to move the snake upwards. Snake can only move left or right when going up
"""   
def moveUp(window):
    
    while(True):  
        
        global fx, fy
        
        pygame.time.delay(80)
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                
        keys = pygame.key.get_pressed()
        
   
                
        if keys[pygame.K_RIGHT]:#if user presses right call moveRight
            moveRight(window)
       
            
        elif(keys[pygame.K_LEFT]): #if user presses left call moveLeft
            moveLeft(window)
        
                
        window.fill((0,0,0)) #clear the window each time

        
        feed(window, fx, fy) #call feed to draw food
        
        head = body[len(body)-1] 
        
    
        #store previous(current) coordinates of the head
        prev_x = head.x
        prev_y = head.y
        
        head.y -= velocity #decrements y coordinate of head by velocity so that it moves down by 30
        head.draw(window) #draw the head in new location
        pygame.display.update()
        
  
        distance = math.hypot(head.x - fx,head.y- fy ) #calculate distance between head and food
        
        if(distance < 30): #if head collides with food call eat and chooseFood
            eat()
            fx, fy = chooseFood()
        disp_score(window) #display the new score
        
        followHead(window,prev_x, prev_y) #call followHead to move the rest of the Cubes. Pass the previous head coordinates
        
        if head.y < 0: #if the head y coordinate is less than zero than it went past the upper window boundary
            crash(window) #call crash
        
        self_crash(window) #check to see if the snake crashed against itself
        
   
    
"""
Moves snake down. Can only go left or right when moving down. Works in similar way as moveUp
"""        
def moveDown(window):
    
    
    while(True): 
        
        global fx,fy
        
        pygame.time.delay(80)
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                
        keys = pygame.key.get_pressed()
        
    
                
        if keys[pygame.K_RIGHT]:
            moveRight(window)
         
  
            
        elif(keys[pygame.K_LEFT]):
            moveLeft(window)
       
                
        window.fill((0,0,0))
        
        feed(window, fx, fy)

        
        head = body[len(body)-1]
        
    
        
        prev_x = head.x
        prev_y = head.y
        
        head.y += velocity #we increment y coordinate by velocity so that it moves down
        head.draw(window)
        pygame.display.update()
        
       
  
        distance = math.hypot(head.x - fx,head.y- fy )
        
        if(distance < 30):
            eat()
            fx, fy = chooseFood()
            
        disp_score(window)
        
        followHead(window, prev_x, prev_y)
        
        if(head.y > 570): #check that it doesn't go past the lower boundary
            crash(window)
        
        self_crash( window)
        
       
        
        
"""
This method moves the snake to the right. Works in a similar way as the moveLeft method
"""
def moveRight(window):

        
    while(True):
        
        global score
        global fx
        global fy
        
        pygame.time.delay(80)
        
        for event in pygame.event.get():
                if event.type== pygame.QUIT:
                    pygame.quit()
                    
        keys = pygame.key.get_pressed()
        

    
     
           
        if(keys[pygame.K_DOWN]):
            moveDown(window)
        
            
        elif(keys[pygame.K_UP]):
            moveUp(window)
           
            

 
                    
        window.fill((0,0,0))
    
        
        feed(window, fx, fy)
        
        head = body[len(body)-1]
        
      
     
        prev_x = head.x
        prev_y = head.y
  
        head.x += velocity #increment x coordinate so that itmoves to the right
        head.draw(window)
        pygame.display.update()
  

        distance = math.hypot(head.x - fx,head.y- fy )
        
        if(distance < 30):
            eat()
            fx, fy = chooseFood()
        disp_score(window)
        
        followHead(window, prev_x, prev_y)
        
        if(head.x > 570): #check that it doesn't go past the right boundary
            crash(window) 
            
        self_crash( window)
        
  
        
        


velocity = 30 #sets velocity to 30

c1 = Cube(30,30) #creates the first Cube 

body = [c1] #initializes the body of the snake with the head

score = 0 #initiates score

fx,fy = chooseFood()  #creates the first food coordinates


"""
This method displays the game instructions and asks the user for input
"""
def instructions(window):
   font = pygame.font.Font('freesansbold.ttf', 20) 
   inst = font.render("Use keys to move snake(red) around ", True, (0,255,0))
   inst2 = font.render("so that it eats its food(green)", True, (0,255,0))
   instRect = inst.get_rect()
   instRect.center = (300, 200)
   inst2Rect = inst2.get_rect()
   inst2Rect.center = (300, 250)
   play = font.render("Press 'right' to play", True, (0,255,0))
   playRect = play.get_rect()
   playRect.center = (300,400)
   while(True):

     
       window.fill((0,0,0))
       window.blit(inst, instRect)
       window.blit(inst2, inst2Rect)
       window.blit(play, playRect)
       
       pygame.display.update()
       
       keys = pygame.key.get_pressed()
       
       if keys[pygame.K_RIGHT]: #if the user presses right to continue then call the moveRight method
           window.fill((0,0,0))
           moveRight(window)
         
    
       #checks to see if user closes window
       for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
    


    
            
                
       
       
"""
This method creates the window for our game and displays an introduction message and prompts
the user for input
"""     
    
def intro():
  
    window = pygame.display.set_mode((600,600))
    print(type(window))
    pygame.display.set_caption("Snake")
    font = pygame.font.Font('freesansbold.ttf', 32) 
    intro = font.render("Welcome to Python's Snake Game", True, (0,255,0))
    introRect = intro.get_rect() 
    introRect.center = (300,300)
    
    
    play = font.render("Press 'space' to continue", True, (0,255,0))
    playRect = play.get_rect()
    playRect.center = (300,400)
    while(True):
        pygame.time.delay(100)
        
        window.fill((0,0,0))
        
     
  
        window.blit(intro, introRect)
        
        
        window.blit(play, playRect)
        
        keys = pygame.key.get_pressed()
        
        pygame.display.update()
        
    
        if keys[pygame.K_SPACE]: #if the user presses space then call the instructions method
            window.fill((0,0,0))
            instructions(window)
           
      
        #checks if user closes window
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                
     
            
intro() #makes the call to intro method