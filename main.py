import pygame
import random

pygame.init()
screen = pygame.display.set_mode((900, 500))  
pygame.display.set_caption("Жмакалка!")
pygame.display.set_icon(pygame.image.load("img/Icon_for_first_game.webp"))

# Инициализируем шрифт
pygame.font.init()
font = pygame.font.Font(None, 50) 

# Инициализируем звук
pygame.mixer.init()
click_sound = pygame.mixer.Sound("sound/click.mp3") 

running = True
background_color = (14, 165, 235)  
click_count = 0  

while running:
    screen.fill(background_color)  

    text = font.render(f"Клики: {click_count}", True, (255, 255, 255))  
    screen.blit(text, (20, 20))  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB or pygame.K_SPACE or pygame.K_1:
                background_color = (random.randint(0, 255), 
                                    random.randint(0, 255), 
                                    random.randint(0, 255))
                click_count += 1  
                click_sound.play()  

    pygame.display.update()  

pygame.quit()
