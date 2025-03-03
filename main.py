import pygame

pygame.init()
screen = pygame.display.set_mode((900, 500))
pygame.display.set_caption("Pygame || super game!")
pygame.display.set_icon(pygame.image.load("img/Icon_for_first_game.webp"))

background_color = (95, 209, 227)

# Загружаем и масштабируем спрайты
walk = [
    pygame.transform.scale(pygame.image.load("img/slime/slime_1.png"), (80, 80)),
    pygame.transform.scale(pygame.image.load("img/slime/slime_2.png"), (80, 80)),
    pygame.transform.scale(pygame.image.load("img/slime/slime_3.png"), (80, 80)),
]
ghost = pygame.transform.scale(pygame.image.load("img/ghost/ghost.png"), (100, 80))
ghost = pygame.transform.flip(ghost, True, False)
ghost_x = 800
ghost_y = 324



# Загружаем фон
bg = pygame.image.load("img/bg/bg.jpg")
bg = pygame.transform.scale(bg, (900, 500))

# --- clock ---
clock = pygame.time.Clock()
frame = 0  
count = 0  
frame_rate = 5

# --- audio ---
bg_sound = pygame.mixer.Sound("sound/bg.mp3")
bg_sound.play(-1)
bg_sound.set_volume(0.01)
# --- speed ---
speed_player = 6
player_x = 10
player_y = 324

# --- движение ---
facing_right = True  
isJump = False
jumpCount = 10


ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 7000)
ghost_speed = 5

# --- шрифт для текста ---
font = pygame.font.SysFont("Arial", 30) 

running = True
while running:
    screen.blit(bg, (0, 0))  
    screen.blit(ghost, (ghost_x, ghost_y))  
    
    
    speed_text = font.render(f"Speed: {ghost_speed}", True, (255, 255, 255))  
    screen.blit(speed_text, (10, 10))  
    
    player_rect = walk[0].get_rect(topleft=(player_x, player_y))
    ghost_rect = ghost.get_rect(topleft=(ghost_x, ghost_y))
    if player_rect.colliderect(ghost_rect):
        print("Game Over")
        running = False

    if frame % frame_rate == 0:
        count = (count + 1) % len(walk)

    if facing_right:
        screen.blit(walk[count], (player_x, player_y))
    else:
        screen.blit(pygame.transform.flip(walk[count], True, False), (player_x, player_y))

    keys = pygame.key.get_pressed()

    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player_x > 0:
        player_x -= speed_player
        facing_right = False
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            player_x -= speed_player * 1.5

    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player_x < 900 - 80:
        player_x += speed_player
        facing_right = True
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            player_x += speed_player * 1.5

    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1 if jumpCount > 0 else -1
            player_y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    ghost_x -= ghost_speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == ghost_timer:
            ghost_x = 900
            ghost_y = 324
            ghost_speed += 10

    pygame.display.update()
    frame += 1
    clock.tick(30)

pygame.quit()
