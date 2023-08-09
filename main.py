import pygame
import time
import random
import math

# game setup
pygame.init()

game_width = 350
game_height = 500

gravity = 9.8

playerStartLocation = (game_width,game_height)
playerImage = pygame.image.load('assets/player.png')

gameDisplay = pygame.display.set_mode((game_width,game_height))
pygame.display.set_caption('Climb!')
clock = pygame.time.Clock()
gameDisplay.fill((135, 206, 235))

# Declaration of world physics in order to initialise the game
gravity = 9.8

# Player physics
playerDrag = 0.9        # no unit, the player velocity is multiplied by 0.9 every second or so
playerLocation = (0,0)
playerSpeed = 0         # speed of the player in m/s
playerDirection = 0     # direction in degrees or radians
playerMass = 20         # Mass in kg's

controlForce = 200      # players Force in Newtons

def updatePlayerVelocity(forces, time): # Apply inputed forces to character
    x = 0
    y = 0
    for i in range(len(forces)):
        

    # player velocities

    

def moveObjects():
    # apply velocity to the time passed
    print('')

def update():
    updateVelocities()  # Apply game forces to update velocities
    moveObjects()       # Apply game velocities
    
gameRunning = True
while gameRunning:      # game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("QUIT")
            pygame.quit()
            gameRunning = False
            quit() 

        controlForces = [[0,0],[0,0],[0,0],[0,0]]

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                controlForces[0] = [controlForce, 0]
            elif event.key == pygame.K_d:
                controlForces[1] = [controlForce, 90]
            elif event.key == pygame.K_s:
                controlForces[2] = [controlForce, 180]
            elif event.key == pygame.K_w:
                controlForces[3] = [controlForce, 270]
            elif event.key == pygame.K_SPACE:
                print("space")
    
    # updatePlayerVelocity(controlForces)
    # update()
    gameDisplay.blit(playerImage, (playerLocation[0],playerLocation[1]))
    # SnakeObject.Update()
    # SnakeObject.Draw()
    pygame.display.update()
    clock.tick(60)
