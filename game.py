import pygame
import sys
import config # Import the config Module
import random
import shapes


def init_game():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constanst from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events(x1,y1, x2, y2,):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return x1,y1, x2, y2, False
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            x1 -= 1
        if key[pygame.K_RIGHT]:
            x1 += 1
        if key[pygame.K_UP]:
            y1 -= 1
        if key[pygame.K_DOWN]:
            y1 += 1

        if key[pygame.K_a]:
            x2 -= 1
        if key[pygame.K_d]:
            x2 += 1
        if key[pygame.K_w]:
            y2 -= 1
        if key[pygame.K_s]:
            y2 += 1 



        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return x1,y1, x2, y2,True


def draw_rectangle(screen, color, x, y, width, height):
    pygame.draw.rect(screen, color, (x, y, width, height))

def main():
    screen = init_game()

    font = pygame.font.Font(None, 36)


    color1 = config.RED
    x1, y1 = 95, 325
    width1 = 250
    height1 = 125

    color2 = config.BLUE
    x2, y2 = 395, 325
    width2 = 150
    height2 = 225

    text_surface1 = font.render('Hello, Pygame!', True, config.BLUE)

    text_width = text_surface1.get_width()

    text_x = (config.WINDOW_WIDTH - text_width) // 2

    text_y = 50



    text_surface2 = font.render("Cool Text", True, config.RED)

    text_width2 = text_surface2.get_width()
    
    text_x2 = (config.WINDOW_WIDTH - text_width2) // 2

    text_y2 = 90


    running = True

    clock = pygame.time.Clock() # Initialize the clock here
    
    while running:
        running = handle_events(x1,y1,x2,y2)
        value = 1
        
        screen.fill(config.WHITE) # Use color from config
        
        draw_rectangle(screen, color1, x1, y1, width1, height1)

        draw_rectangle(screen,color2, x2, y2, width2, height2)


        screen.blit(text_surface1, (text_x, text_y))
        screen.blit(text_surface2, (text_x2, text_y2))

        pygame.display.flip()

        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(config.FPS) # use the clock to control the frame rate

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()