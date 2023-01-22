import sheetFile
import pygame

pygame.init()


# creates the screen
screen = pygame.display.set_mode(
    (1021, 276), pygame.HWSURFACE | pygame.DOUBLEBUF)

# heading which is displayed next to the icon
pygame.display.set_caption("Dragon Flight")

# adds an icon
icon = pygame.image.load("dragon.png")
pygame.display.set_icon(icon)

# loads an image which we use for a background
bg = pygame.image.load("background2.jpg").convert()

char = pygame.image.load("char_1.png")
charX = 50
charY = 138
charChangeY = 0

fireballImg = pygame.image.load('fire.png')
fireballX = 90
fireballY = 150
fireballX_change = 20
fireballY_change = 0
fireball_state = "ready"
fireballs = []


def character(x, y):
    screen.blit(char, (x, y))


sheet = pygame.image.load("sheet2.png").convert_alpha()

BLACK = (0, 0, 0, 0)
sprite_sheet = sheetFile.Sheets(sheet)
frame_1 = sprite_sheet.getImage(0, 61, 64, BLACK)
frame_2 = sprite_sheet.getImage(1, 61, 64, BLACK)
frame_3 = sprite_sheet.getImage(2, 61, 64, BLACK)

current_frame = 0
clock = pygame.time.Clock()
running = True

moving_up = False
moving_down = False
firing = False

print("hello")
# game loop
while running:
    clock.tick(24)
    screen.blit(bg, (0, 0))
    # for loop through the event queue
    for event in pygame.event.get():
        charY += charChangeY
        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_SPACE:
                fireballY = charY
                fireball = {
                    'img': fireballImg,
                    'x': 90,
                    'y': charY,
                    'x_change': 20,
                    'y_change': 0,
                    'state': 'ready'
                }
                fireballs.append(fireball)
                screen.blit(fireball['img'],
                            (fireball['x'] + 16, fireball['y'] + 10))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            charChangeY = -3
        if keys[pygame.K_s]:
            charChangeY = 3
        if event.type == pygame.KEYUP:
            charChangeY = 0
        if charY >= 211:
            charY = 211
        elif charY <= 0:
            charY = 0
    for i, fireball in enumerate(fireballs):
        screen.blit(fireball['img'], (fireball['x'] + 16, fireball['y'] + 10))
        fireball['x'] += fireball['x_change']
        if fireball['x'] >= 1000:
            fireballs.pop(i)

    

    if fireballX >= 1000:
        fireballX = 90
        fireball_state = "ready"

    if fireball_state == "fire":
        fire_fireball(fireballX, fireballY)
        fireballX += fireballX_change
      # update the current frame
    current_frame += 1
    # check if the current frame is greater than 2 (3 frames)
    if current_frame > 3:
        current_frame = 0
    # display the appropriate frame
    if current_frame == 0:
        current_image = screen.blit(frame_1, (charX, charY))
    elif current_frame == 1:
        current_image = screen.blit(frame_2, (charX, charY))
    elif current_frame == 2:
        current_image = screen.blit(frame_3, (charX, charY))
    elif current_frame == 3:
        current_image = screen.blit(frame_2, (charX, charY))

    current_image

    pygame.display.update()
pygame.quit()
