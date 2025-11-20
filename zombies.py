import pygame, random, math

pygame.init()

WIDTH = 800
HEIGHT = 800
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zombies")

FPS = 60
clock = pygame.time.Clock()
delta = clock.tick(FPS) // 1000

STARTING_WAVE = 1
MAX_BULLETS = 6
BULLET_SPEED = 8
STARTING_LIVES = 3
lives = 3
wave = 1

player_damage = random.uniform(1, 2)
zombie_damage = random.uniform(0.5, 1.5)
player_health = 3
zombie_health = 3
wave_list = []
ran_num_zom = random.randint(3, 10)
zom_multiplier = random.uniform(1, 2)
num_zom = ran_num_zom * wave * zom_multiplier
num_zom = round(num_zom)
print(num_zom)
knockback = 75
shot_knockback = 10
player_pos = (WIDTH // 2, HEIGHT // 2)
mouse_x, mouse_y = pygame.mouse.get_pos()
player_x, player_y = player_pos
dead_zombie_pos = 1000, 1000

# Font
font = pygame.font.Font("doomed.ttf", 24)

# Images
background_image = pygame.transform.scale(pygame.image.load("6a68c9aee6a3655.png"),(WIDTH, HEIGHT))

death_image = pygame.transform.scale(pygame.image.load("New Piskel (2).png"), (WIDTH, HEIGHT)).convert_alpha()

player_image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("Top-Down Player.png"), (64, 64)), 90)
player_rect = player_image.get_rect()
player_rect.center = (WIDTH // 2, HEIGHT // 2)

player_hitbox_x, player_hitbox_y = player_x - 26, player_x - 26
player_hitbox = (player_hitbox_x, player_hitbox_y, 52, 52)
player_collision_shape = pygame.draw.rect(display_surface, (0, 0, 0), player_hitbox, 2)

zombie_image = pygame.transform.scale(pygame.image.load("Top-Down Enemy.png"), (64, 64))
zombie_rect = zombie_image.get_rect()
zombie_rect.x = random.randint(0, WIDTH)
zombie_rect.y = random.randint(0, HEIGHT)

zombie = zombie_rect

zombie_pos = random.choice([(0, 0), (0, 400), (0, 800), (400, 0), (400, 800), (800, 0), (800, 400), (800, 800)])
zombie_rect.center = zombie_pos
zombie_velocity = random.uniform(0.5, 2)

zombie_angle = 0
if zombie_rect.center == (0, 0):
    zombie_angle = 225
if zombie_rect.center == (0, 400):
    zombie_angle = 270
if zombie_rect.center == (0, 800):
    zombie_angle = 315
if zombie_rect.center == (400, 0):
    zombie_angle = 180
if zombie_rect.center == (400, 800):
    zombie_angle = 0
if zombie_rect.center == (800, 0):
    zombie_angle = 135
if zombie_rect.center == (800, 400):
    zombie_angle = 90
if zombie_rect.center == (800, 800):
    zombie_angle = 45

zombie_image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("Top-Down Enemy.png"), (64, 64)), zombie_angle)


bullet_image = pygame.transform.scale(pygame.image.load("New Piskel (1).png"), (96, 96))
bullet_rect = bullet_image.get_rect()
bullet_rect.center = player_rect.center

# Heart images
heart_1_image = pygame.transform.scale(pygame.image.load("Heart_corazón.svg.png"), (30, 30))
heart_1_rect = heart_1_image.get_rect()
heart_1_rect.x, heart_1_rect.y = 680, 10
heart_2_image = pygame.transform.scale(pygame.image.load("Heart_corazón.svg.png"), (30, 30))
heart_2_rect = heart_2_image.get_rect()
heart_2_rect.x, heart_2_rect.y = 720, 10
heart_3_image = pygame.transform.scale(pygame.image.load("Heart_corazón.svg.png"), (30, 30))
heart_3_rect = heart_3_image.get_rect()
heart_3_rect.x, heart_3_rect.y = 760, 10

# Set colors
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GREEN = (10, 75, 10)

# Text
title_text = font.render("Zombies", True, DARK_GREEN)
title_rect = title_text.get_rect()
title_rect.midtop = (WIDTH // 2, 10)

wave_text = font.render("Wave " + str(wave), True, RED)
wave_rect = wave_text.get_rect()
wave_rect.topleft = (10, 10)

start_text = font.render("START!", True, RED)
start_rect = start_text.get_rect()
start_rect.center = (WIDTH // 2, HEIGHT // 2)

next_wave_text = font.render("Wave " + str(wave), True, RED)
next_wave_rect = next_wave_text.get_rect()
next_wave_rect.center = (WIDTH // 2, HEIGHT // 2)

# Sounds
player_hit_sound = pygame.mixer.Sound("eating-sound-effect-36186.mp3")
zombie_hit_sound = pygame.mixer.Sound("mixkit-small-hit-in-a-game-2072.wav")
shoot_sound = pygame.mixer.Sound("mixkit-game-gun-shot-1662.mp3")
death_sound = pygame.mixer.Sound("pixel-death-66829.mp3")
pygame.mixer.music.load("mixkit-dark-shadows-64.mp3")



def zombie_reset():
    zombie_rect.center = zombie_pos

def get_new_zombie():
    # zombie_pos = random.choice([(0, 0), (0, 400), (0, 800), (400, 0), (400, 800), (800, 0), (800, 400), (800, 800)])
    # zombie_rect.center = zombie_pos
    # zombie_velocity = random.uniform(0.5, 2)

    if zombie_angle == 225:
        zombie_rect.x += zombie_velocity
        zombie_rect.y += zombie_velocity
    if zombie_angle == 270:
        zombie_rect.x += zombie_velocity
    if zombie_angle == 315:
        zombie_rect.x += zombie_velocity
        zombie_rect.y -= zombie_velocity
    if zombie_angle == 180:
        zombie_rect.y += zombie_velocity
    if zombie_angle == 0:
        zombie_rect.y -= zombie_velocity
    if zombie_angle == 135:
        zombie_rect.x -= zombie_velocity
        zombie_rect.y += zombie_velocity
    if zombie_angle == 90:
        zombie_rect.x -= zombie_velocity
    if zombie_angle == 45:
        zombie_rect.x -= zombie_velocity
        zombie_rect.y -= zombie_velocity

    display_surface.blit(zombie_image, zombie_rect)

def new_wave():
    if len(wave_list) == 0:
        for i in range(num_zom):
            zombie = zombie_rect
            wave_list.append(zombie)
            for zombie in wave_list:
                get_new_zombie()


def pause(main_text, sub_text):
    """Pause the game"""
    global running

    # Create the main pause text
    main_text = font.render(main_text, True, WHITE)
    main_rect = main_text.get_rect()
    main_rect.center = (WIDTH // 2, HEIGHT // 2)
    # Create the sub pause text
    sub_text = font.render(sub_text, True, WHITE)
    sub_rect = sub_text.get_rect()
    sub_rect.center = (WIDTH // 2, HEIGHT // 2 + 64)
    # Display the pause text
    display_surface.blit(main_text, main_rect)
    display_surface.blit(sub_text, sub_rect)
    pygame.display.update()
    # Pause the game
    is_paused = True
    while is_paused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    is_paused = False
            if event.type == pygame.QUIT:
                is_paused = False
                running = False


pygame.mixer.music.play(-1, 0.0)
bullets = []
pos = (WIDTH // 2, HEIGHT // 2)
dead = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pause("Paused", "Press RETURN to resume")
            if event.key == pygame.K_SPACE and len(bullets) < MAX_BULLETS:
                shoot_sound.play()
                bullet = bullet_rect
                bullet_rect.center = player_rect.center
                bullets.append(bullet)

    if dead:
        pygame.mixer.music.stop()
        death_sound.play()
        lives = STARTING_LIVES
        wave = 1
        for zombie in wave_list:
            zombie_health = 3
            wave_list.remove(zombie)
            zombie_reset()

        heart_1_rect.y = 10
        heart_2_rect.y = 10
        heart_3_rect.y = 10

        bullet_rect.center = player_rect.center

        zombie_pos = random.choice([(0, 0), (0, 400), (0, 800), (400, 0), (400, 800), (800, 0), (800, 400), (800, 800)])
        zombie_rect.center = zombie_pos

        get_new_zombie()

        pause("DEAD", "Press RETURN to try again")
        for event in pygame.event.get():
            if event.key == pygame.K_RETURN:
                pygame.mixer.music.play()
                dead = False
                is_paused = False


    display_surface.blit(background_image, (0, 0))
    mouse_pos = pygame.mouse.get_pos()
    angle = 360 - math.atan2(mouse_pos[1] - 400, mouse_pos[0] - 400) * 180 // math.pi
    rotimage = pygame.transform.rotate(player_image, angle)
    bullet_image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("New Piskel (1).png"), (96, 96)), angle)
    rect = rotimage.get_rect(center=(400, 400))
    display_surface.blit(rotimage, rect)
    pygame.draw.rect(display_surface, BLACK, player_hitbox, 2)
    get_new_zombie()
    get_new_zombie()
    get_new_zombie()
    if zombie_health <= 0:
        zombie_rect.center = dead_zombie_pos

    display_surface.blit(title_text, title_rect)
    display_surface.blit(wave_text, wave_rect)
    display_surface.blit(heart_1_image, heart_1_rect)
    display_surface.blit(heart_2_image, heart_2_rect)
    display_surface.blit(heart_3_image, heart_3_rect)

    # for i in range(num_zom):
    #     zombie_pos = random.choice([(0, 0), (0, 400), (0, 800), (400, 0), (400, 800), (800, 0), (800, 400), (800, 800)])
    #     zombie_rect.center = zombie_pos
    #     zombie_velocity = random.uniform(0.5, 2)
    #     get_new_zombie()
    #     wave_list.append(zombie)
    #
    # for zombie in wave_list:
    #     if zombie_health > 0:
    #         display_surface.blit(zombie_image, zombie_rect)

    for bullet in bullets:
        bullet_direction = pygame.Vector2(bullet_rect.x - mouse_pos[0], bullet_rect.y - mouse_pos[1])

        if bullet_direction != pygame.Vector2(0, 0):
            bullet_direction.normalize_ip()

        bullet_velocity = bullet_direction * BULLET_SPEED
        display_surface.blit(bullet_image, bullet_rect)
        bullet_rect.x += bullet_velocity[0]
        bullet_rect.y += bullet_velocity[1]
        if bullet_rect.colliderect(zombie_rect) and (bullet in bullets):
            zombie_hit_sound.play()
            if zombie_angle == 225:
                zombie_rect.x -= shot_knockback
                zombie_rect.y -= shot_knockback
            if zombie_angle == 270:
                zombie_rect.x -= shot_knockback
            if zombie_angle == 315:
                zombie_rect.x -= shot_knockback
                zombie_rect.y += shot_knockback
            if zombie_angle == 180:
                zombie_rect.y -= shot_knockback
            if zombie_angle == 0:
                zombie_rect.y += shot_knockback
            if zombie_angle == 135:
                zombie_rect.x += shot_knockback
                zombie_rect.y -= shot_knockback
            if zombie_angle == 90:
                zombie_rect.x += shot_knockback
            if zombie_angle == 45:
                zombie_rect.x += shot_knockback
                zombie_rect.y += shot_knockback
            zombie_health -= player_damage
            bullets.remove(bullet)
        if bullet_rect.x > WIDTH or bullet_rect.x < 0 or bullet_rect.y > HEIGHT or bullet_rect.y < 0 and (bullet in bullets):
            bullets.remove(bullet)

    if player_collision_shape.colliderect(zombie):
        player_hit_sound.play()
        lives -= 1
        if zombie_angle == 225:
            zombie_rect.x -= knockback
            zombie_rect.y -= knockback
        if zombie_angle == 270:
            zombie_rect.x -= knockback
        if zombie_angle == 315:
            zombie_rect.x -= knockback
            zombie_rect.y += knockback
        if zombie_angle == 180:
            zombie_rect.y -= knockback
        if zombie_angle == 0:
            zombie_rect.y += knockback
        if zombie_angle == 135:
            zombie_rect.x += knockback
            zombie_rect.y -= knockback
        if zombie_angle == 90:
            zombie_rect.x += knockback
        if zombie_angle == 45:
            zombie_rect.x += knockback
            zombie_rect.y += knockback

    if lives <= 2:
        heart_3_rect.y -= 2
    if lives <= 1:
        heart_2_rect.y -= 2
    if lives <= 0:
        heart_1_rect.y -= 2
        dead = True

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
