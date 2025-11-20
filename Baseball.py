import pygame, random, math

pygame.init()

WIDTH = 800
HEIGHT = 800
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Homerun Derby")

FPS = 60
clock = pygame.time.Clock()

BALL_SPEED = 8
BAT_SPEED = 4
HOMERUN_POS = (WIDTH, HEIGHT)
LUCK = random.uniform(0.3, 1.3)
BONUS = random.uniform(1, 2.5)
BAT_BUFFER_DISTANCE = HEIGHT - 150
BAT_MAX_DISTANCE = BAT_BUFFER_DISTANCE - 75
num_attempts = 10

MAX_BALL = 1
ball_list = []

player_pos = ((WIDTH // 2) + 10, (HEIGHT // 4) + 60)
mouse_x, mouse_y = pygame.mouse.get_pos()
player_x, player_y = player_pos

strikes = 0
balls = 0

batter_points = 0
pitcher_points = 0

batter = "batter"
pitcher = "pitcher"

winner = "None"

# Set colors
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GREEN = (10, 75, 10)
DARK_RED = (75, 10, 10)
ORANGE_RED = (255, 69, 0)

# Background
background = pygame.transform.scale(pygame.image.load("New Piskel (3).png"), (WIDTH, HEIGHT))

# Font
font = pygame.font.Font("m23.TTF", 24)

info_font = pygame.font.Font("m23.TTF", 18)

# Images
# Pitcher
pitcher_frame_1 = pygame.image.load("Pitcher #1.png")
pitcher_frame_1_rect = pitcher_frame_1.get_rect()

current_pitcher_frame_image = pygame.transform.rotate(pygame.transform.scale(pitcher_frame_1, (96, 96)), -90)
current_pitcher_frame_rect = pitcher_frame_1_rect

pitcher_frame_1_rect.center = player_pos

# Baseball
baseball_image = pygame.transform.scale(pygame.image.load("Baseball.png"), (64, 64))
baseball_rect = baseball_image.get_rect()
baseball_rect.center = player_pos

ball = baseball_rect

# Baseball Bat
bat_image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("Baseball Bat.png"), (48, 76)), -90)
bat_rect = bat_image.get_rect()
starting_bat_pos = (1000, 1000)
bat_rect.center = starting_bat_pos

# Sounds
pitch_sound = pygame.mixer.Sound("yt5s.com - Baseball Pitch Sound Effect [HD ] Audio (128 kbps).mp3")
hit_sound = pygame.mixer.Sound("onlymp3.to - The Crack of a Wooden Bat-5VwLqcZ5IHg-256k-1654585163239.mp3")
strike_sound = pygame.mixer.Sound("Umpire Calls 'Strike'.mp3")
ball_sound = pygame.mixer.Sound("Umpire Calls 'Ball'.mp3")
homerun_sound = pygame.mixer.Sound("Y2Mate.is - Outdoor Baseball Stadium Crowd Cheering Loudly  - Sound Effect-YLhVDMmsCO4-160k-1654351656691.mp3")
game_over_sound = pygame.mixer.Sound("Charge - Sound Effects.mp3")
pygame.mixer.music.load("10convert.com_NEW Ballpark Organ Music_PFR3S6jN0Ng.mp3")

# Text
strike_text = font.render("Strike " + str(strikes), True, ORANGE_RED)
strike_rect = strike_text.get_rect()
strike_rect.bottomleft = (10, HEIGHT - 10)

ball_text = font.render("Ball " + str(balls), True, GREEN)
ball_rect = ball_text.get_rect()
ball_rect.bottomright = (WIDTH - 10, HEIGHT - 10)

homerun_text = font.render("HOMERUN", True, BLACK)
homerun_rect = homerun_text.get_rect()
homerun_rect.center = (WIDTH // 2, HEIGHT // 2)

title_text = font.render("Homerun Derby", True, WHITE)
title_rect = title_text.get_rect()
title_rect.midtop = (WIDTH // 2, 25)

batter_points_text = font.render("The batter got " + str(batter_points), True, BLACK)
batter_points_rect = batter_points_text.get_rect()

pitcher_points_text = font.render("The pitcher got " + str(pitcher_points), True, BLACK)
pitcher_points_rect = pitcher_points_text.get_rect()

winner_text = font.render("The winner is " + winner, True, GREEN)
winner_rect = winner_text.get_rect()
winner_rect.center = (WIDTH // 2, HEIGHT // 4)

continue_text = font.render("To retry press RETURN", True, WHITE)
continue_rect = continue_text.get_rect()
continue_rect.center = (WIDTH // 2, HEIGHT - 20)

# Info Texts
info_1_text = info_font.render("Press W to swing and SPACE to pitch and use mouse to control", True, WHITE)
info_1_rect = info_1_text.get_rect()
info_1_rect.center = (WIDTH // 2, HEIGHT // 2)

info_2_text = info_font.render("Each hit is 1 point, and homerun is 3 points", True, WHITE)
info_2_rect = info_2_text.get_rect()
info_2_rect.center = (WIDTH // 2, (HEIGHT // 2) + 40)

info_3_text = info_font.render("Each strike is 2 points, each ball is minus 1 point", True, WHITE)
info_3_rect = info_3_text.get_rect()
info_3_rect.center = (WIDTH // 2, (HEIGHT // 2) + 80)

# Home plate rect
home_plate = pygame.rect.Rect(WIDTH // 2, HEIGHT * 0.75, 25, 50)

bottom_plate = pygame.rect.Rect((WIDTH // 2) - 10, (HEIGHT * 0.75) + 50, 45, 3)

# Number of balls
ball_1 = baseball_image
ball_1_rect = ball_1.get_rect()
ball_1_rect.bottomleft = (155, HEIGHT - 10)

ball_2 = baseball_image
ball_2_rect = ball_2.get_rect()
ball_2_rect.bottomleft = (ball_1_rect.bottomleft[0] + 50, HEIGHT - 10)

ball_3 = baseball_image
ball_3_rect = ball_3.get_rect()
ball_3_rect.bottomleft = (ball_2_rect.bottomleft[0] + 50, HEIGHT - 10)

ball_4 = baseball_image
ball_4_rect = ball_4.get_rect()
ball_4_rect.bottomleft = (ball_3_rect.bottomleft[0] + 50, HEIGHT - 10)

ball_5 = baseball_image
ball_5_rect = ball_5.get_rect()
ball_5_rect.bottomleft = (ball_4_rect.bottomleft[0] + 50, HEIGHT - 10)

ball_6 = baseball_image
ball_6_rect = ball_6.get_rect()
ball_6_rect.bottomleft = (ball_5_rect.bottomleft[0] + 50, HEIGHT - 10)

ball_7 = baseball_image
ball_7_rect = ball_7.get_rect()
ball_7_rect.bottomleft = (ball_6_rect.bottomleft[0] + 50, HEIGHT - 10)

ball_8 = baseball_image
ball_8_rect = ball_8.get_rect()
ball_8_rect.bottomleft = (ball_7_rect.bottomleft[0] + 50, HEIGHT - 10)

ball_9 = baseball_image
ball_9_rect = ball_9.get_rect()
ball_9_rect.bottomleft = (ball_8_rect.bottomleft[0] + 50, HEIGHT - 10)

ball_10 = baseball_image
ball_10_rect = ball_10.get_rect()
ball_10_rect.bottomleft = (ball_9_rect.bottomleft[0] + 50, HEIGHT - 10)

# Conditions
swung = False
threw = False
hit = False
homerun = False
game_over = False

def pause(main_text, sub_text):
    """Pause the game"""
    global running

    # Create the main pause text
    main_text = font.render(main_text, True, BLACK)
    main_rect = main_text.get_rect()
    main_rect.center = (WIDTH // 2, HEIGHT // 2)
    # Create the sub pause text
    sub_text = font.render(sub_text, True, BLACK)
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

mouse_pos = pygame.mouse.get_pos()

ball_direction = pygame.Vector2(baseball_rect.x - mouse_pos[0], baseball_rect.y - mouse_pos[1])

ball_velocity = ball_direction * BALL_SPEED

regular_ball_direction = ball_direction
backwards_ball_direction = ball_direction * -1

# Game Loop
pygame.mixer.music.play(-1, 0.0)
running = True
main_menu = True
while running:
    while main_menu:
        continue_text = font.render("Press RETURN to begin", True, WHITE)

        display_surface.fill(BLACK)
        display_surface.blit(title_text, title_rect)
        display_surface.blit(info_1_text, info_1_rect)
        display_surface.blit(info_2_text, info_2_rect)
        display_surface.blit(info_3_text, info_3_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    continue_text = font.render("To retry press RETURN", True, WHITE)
                    main_menu = False
            if event.type == pygame.QUIT:
                running = False
                quit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pause("Paused", "Press RETURN to resume")
            if event.key == pygame.K_w:
                bat_rect.center = ((WIDTH // 2) - 5, BAT_BUFFER_DISTANCE)
                swung = True
            if event.key == pygame.K_SPACE and len(ball_list) < MAX_BALL and not hit:
                threw = True
                pitch_sound.play()
                ball_direction = regular_ball_direction
                ball = baseball_rect
                baseball_rect.center = current_pitcher_frame_rect.center
                BALL_SPEED = 8
                ball_list.append(ball)

    if baseball_rect.colliderect(bat_rect) and not hit:
        if not hit:
            hit_sound.play()

            # Find End X and Y
            if baseball_rect.x <= (WIDTH // 2) - 25:
                end_x = random.randint(200, 300)
            if baseball_rect.x > (WIDTH // 2) - 25:
                end_x = random.randint(350, 600)
            if baseball_rect.x >= bat_rect.right:
                end_x = random.randint(500, 700)

            LUCK = random.uniform(0.3, 1.3)
            end_y = 2 * (BALL_SPEED / BAT_SPEED) * LUCK * 10
            if baseball_rect.x >= bat_rect.right - 20:
                end_y *= random.randint(5, 8)
            if BAT_SPEED <= 4.4:
                end_y *= random.randint(3, 8)

            if end_y <= 15:
                homerun_sound.play()

            end_pos = (end_x, end_y)

            print(end_pos)

            batter_points += 1

            hit = True

    display_surface.blit(background, (0, 0))

    # Rotate Pitcher
    mouse_pos = pygame.mouse.get_pos()
    angle = 360 - math.atan2(mouse_pos[1] - player_pos[1], mouse_pos[0] - player_pos[0]) * 180 // math.pi
    rotimage = pygame.transform.rotate(current_pitcher_frame_image, angle)
    baseball_image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("Baseball.png"), (64, 64)), angle)
    rect = rotimage.get_rect(center=player_pos)
    display_surface.blit(rotimage, rect)

    display_surface.blit(strike_text, strike_rect)
    display_surface.blit(ball_text, ball_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(ball_1, ball_1_rect)
    display_surface.blit(ball_2, ball_2_rect)
    display_surface.blit(ball_3, ball_3_rect)
    display_surface.blit(ball_4, ball_4_rect)
    display_surface.blit(ball_5, ball_5_rect)
    display_surface.blit(ball_6, ball_6_rect)
    display_surface.blit(ball_7, ball_7_rect)
    display_surface.blit(ball_8, ball_8_rect)
    display_surface.blit(ball_9, ball_9_rect)
    display_surface.blit(ball_10, ball_10_rect)
    pygame.draw.rect(display_surface, BLACK, home_plate, 2)
    pygame.draw.rect(display_surface, RED, bottom_plate, 2)

    if swung:
        if bat_rect.y > BAT_MAX_DISTANCE:
            display_surface.blit(bat_image, bat_rect)
            BAT_SPEED += 0.05

        bat_rect.y -= BAT_SPEED
        if bat_rect.y < BAT_MAX_DISTANCE:
            if threw:
                strike_sound.play()
                strikes += 1
                strike_text = font.render("Strike " + str(strikes), True, ORANGE_RED)
                pitcher_points += 2
                num_attempts -= 1
                ball_list.remove(ball)
                baseball_rect.center = player_pos
                BALL_SPEED = 8
                threw = False
            bat_rect.center = starting_bat_pos
            BAT_SPEED = 4
            swung = False

    if threw:
        if len(ball_list) < MAX_BALL:
            ball_list.append(ball)
        if not hit:
            ball_direction = pygame.Vector2(baseball_rect.x - mouse_pos[0], baseball_rect.y - mouse_pos[1])

        if ball_direction != pygame.Vector2(0, 0):
            ball_direction.normalize_ip()

        ball_velocity = ball_direction * BALL_SPEED
        display_surface.blit(baseball_image, baseball_rect)
        if not hit:
            baseball_rect.x += ball_velocity[0]
            baseball_rect.y += ball_velocity[1]
        if hit:
            baseball_rect.x -= ball_velocity[0]
            baseball_rect.y -= ball_velocity[1]

        if baseball_rect.x > WIDTH or baseball_rect.x < 0 or baseball_rect.y < 0 and (ball in ball_list) and not hit:
            ball_sound.play()
            balls += 1
            ball_text = font.render("Ball " + str(balls), True, GREEN)
            pitcher_points -= 1
            ball_list.remove(ball)
            baseball_rect.center = player_pos
            BALL_SPEED = 8
            threw = False

        if baseball_rect.y > BAT_BUFFER_DISTANCE:
            if WIDTH // 2 <= baseball_rect.centerx <= (WIDTH // 2) + 50 or baseball_rect.colliderect(bottom_plate) and not hit:
                strike_sound.play()
                strikes += 1
                pitcher_points += 2
                strike_text = font.render("Strike " + str(strikes), True, ORANGE_RED)
                num_attempts -= 1
                ball_list.remove(ball)
                baseball_rect.center = player_pos
                BALL_SPEED = 8
                threw = False

            if baseball_rect.centerx < WIDTH // 2 or baseball_rect.centerx > (WIDTH // 2) + 50 and not hit:
                ball_sound.play()
                balls += 1
                pitcher_points -= 1
                ball_text = font.render("Ball " + str(balls), True, GREEN)
                ball_list.remove(ball)
                baseball_rect.center = player_pos
                BALL_SPEED = 8
                threw = False

    if hit:
        threw = False

        ball_direction = pygame.Vector2(baseball_rect.x - end_pos[0], baseball_rect.y - end_pos[1])

        if ball_direction != pygame.Vector2(0, 0):
            ball_direction.normalize_ip()

        ball_velocity = ball_direction * BALL_SPEED
        if baseball_rect.y >= end_y:
            display_surface.blit(baseball_image, baseball_rect)
            baseball_rect.x -= ball_velocity[0]
            baseball_rect.y -= ball_velocity[1]

        if baseball_rect.y <= end_y:
            num_attempts -= 1
            if end_y <= 15:
                homerun = True
            hit = False

        if ball in ball_list:
            ball_list.remove(ball)

    if homerun:
        while homerun:
            display_surface.blit(homerun_text, homerun_rect)
            pygame.display.update()

            pygame.time.wait(5000)

            batter_points += 3
            homerun_sound.stop()
            homerun = False

    if num_attempts <= 9:
        ball_1_rect.y += 3
    if num_attempts <= 8:
        ball_2_rect.y += 3
    if num_attempts <= 7:
        ball_3_rect.y += 3
    if num_attempts <= 6:
        ball_4_rect.y += 3
    if num_attempts <= 5:
        ball_5_rect.y += 3
    if num_attempts <= 4:
        ball_6_rect.y += 3
    if num_attempts <= 3:
        ball_7_rect.y += 3
    if num_attempts <= 2:
        ball_8_rect.y += 3
    if num_attempts <= 1:
        ball_9_rect.y += 3
    if num_attempts < 1:
        ball_10_rect.y += 3
        pygame.mixer.music.stop()
        game_over_sound.play()
        game_over = True

    if game_over:
        strike_sound.stop()
        ball_sound.stop()
        if batter_points > pitcher_points:
            batter_points_text = font.render("The batter got " + str(batter_points), True, GREEN)
            if pitcher_points < 0:
                pitcher_points_text = font.render("The pitcher got minus" + str(pitcher_points), True, ORANGE_RED)
            pitcher_points_text = font.render("The pitcher got " + str(pitcher_points), True, ORANGE_RED)
            batter_points_rect.center = (WIDTH // 2, HEIGHT // 2)
            pitcher_points_rect.center = (WIDTH // 2, HEIGHT // 2 + 40)
            winner = batter
            winner_text = font.render("The winner is " + winner, True, WHITE)
        if pitcher_points > batter_points:
            batter_points_text = font.render("The batter got " + str(batter_points), True, ORANGE_RED)
            pitcher_points_text = font.render("The pitcher got " + str(pitcher_points), True, GREEN)
            pitcher_points_rect.center = (WIDTH // 2, HEIGHT // 2)
            batter_points_rect.center = (WIDTH // 2, HEIGHT // 2 + 40)
            winner = pitcher
            winner_text = font.render("The winner is " + winner, True, WHITE)
        while game_over:
            display_surface.fill(BLACK)
            display_surface.blit(batter_points_text, batter_points_rect)
            display_surface.blit(pitcher_points_text, pitcher_points_rect)
            display_surface.blit(winner_text, winner_rect)
            display_surface.blit(continue_text, continue_rect)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        num_attempts = 10
                        ball_1_rect.bottomleft = (155, HEIGHT - 10)
                        ball_2_rect.bottomleft = (ball_1_rect.bottomleft[0] + 50, HEIGHT - 10)
                        ball_3_rect.bottomleft = (ball_2_rect.bottomleft[0] + 50, HEIGHT - 10)
                        ball_4_rect.bottomleft = (ball_3_rect.bottomleft[0] + 50, HEIGHT - 10)
                        ball_5_rect.bottomleft = (ball_4_rect.bottomleft[0] + 50, HEIGHT - 10)
                        ball_6_rect.bottomleft = (ball_5_rect.bottomleft[0] + 50, HEIGHT - 10)
                        ball_7_rect.bottomleft = (ball_6_rect.bottomleft[0] + 50, HEIGHT - 10)
                        ball_8_rect.bottomleft = (ball_7_rect.bottomleft[0] + 50, HEIGHT - 10)
                        ball_9_rect.bottomleft = (ball_8_rect.bottomleft[0] + 50, HEIGHT - 10)
                        ball_10_rect.bottomleft = (ball_9_rect.bottomleft[0] + 50, HEIGHT - 10)

                        strikes = 0
                        balls = 0
                        batter_points = 0
                        pitcher_points = 0
                        strike_text = font.render("Strike " + str(strikes), True, ORANGE_RED)
                        ball_text = font.render("Ball " + str(balls), True, GREEN)

                        pygame.mixer.music.play()

                        # Reset conditionals
                        swung = False
                        hit = False
                        threw = False
                        homerun = False
                        game_over = False
                if event.type == pygame.QUIT:
                    game_over = False
                    running = False

    pygame.display.update()

pygame.quit()