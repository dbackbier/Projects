import pygame, random, math

pygame.init()

WIDTH = 800
HEIGHT = 800
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zombies")

FPS = 60
clock = pygame.time.Clock()
delta = clock.tick(FPS) // 1000

starting_wave = 1
wave = 1

MAX_BULLETS = 6

background_image = pygame.transform.scale(pygame.image.load("6a68c9aee6a3655.png"),(WIDTH, HEIGHT))

font = pygame.font.Font("doomed.ttf", 24)

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

player_image = pygame.transform.scale(pygame.image.load("Top-Down Player.png"), (64, 64))
player_rect = player_image.get_rect()
player_rect.center = (WIDTH // 2, HEIGHT // 2)

# Set colors
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GREEN = (10, 75, 10)

class Game():
    """A class to control gameplay"""
    def __init__(self, player, zombie_group):
        """Initilize the game object"""
        # Set game values
        self.wave = 1
        self.frame_count = 0
        self.wave_time = 0
        self.player = player
        self.zombie_group = zombie_group
        # self.bullet_group = bullet_group
        self.player_damage = random.uniform(1, 2)
        self.zombie_damage = random.uniform(0.5, 1.5)
        self.player_health = 5
        self.zombie_health = 3
        self.wave_list = []
        self.ran_num_zom = random.randint(5, 15)
        self.zom_multiplier = random.uniform(1, 3)
        self.num_zom = self.ran_num_zom * self.wave * self.zom_multiplier
        self.num_zom = round(self.num_zom)
        self.knockback = 10
        # Set sounds and music

        # Set font
        self.font = pygame.font.Font("doomed.ttf", 24)

        # Set images
        self.zombie_image = pygame.image.load("Top-Down Enemy.png")
        self.zombie_rect = self.zombie_image.get_rect()
        self.zombie_rect.x = random.randint(0, WIDTH)
        self.zombie_rect.y = random.randint(0, HEIGHT)

    def update(self):
        """Update our game object"""
        self.frame_count += 1
        if self.frame_count == FPS // 2:
            self.wave_time += 1
            self.frame_count = 0

        # Check collision
        # self.check_collisions()

        # Text
        title_text = font.render("Zombies", True, DARK_GREEN)
        title_rect = title_text.get_rect()
        title_rect.midtop = (WIDTH // 2, 10)

        self.wave_text = font.render("Wave " + str(wave), True, RED)
        self.wave_rect = self.wave_text.get_rect()
        self.wave_rect.topleft = (10, 10)

        start_text = font.render("START!", True, RED)
        start_rect = start_text.get_rect()
        start_rect.center = (WIDTH // 2, HEIGHT // 2)

        next_wave_text = font.render("Wave " + str(wave), True, RED)
        next_wave_rect = next_wave_text.get_rect()
        next_wave_rect.center = (WIDTH // 2, HEIGHT // 2)

        display_surface.blit(title_text, title_rect)
        display_surface.blit(self.wave_text, self.wave_rect)
        display_surface.blit(heart_1_image, heart_1_rect)
        display_surface.blit(heart_2_image, heart_2_rect)
        display_surface.blit(heart_3_image, heart_3_rect)

        pygame.display.update()

    def check_collisions(self):
        """Check for collisions between player and monsters"""
        bullet_collision = pygame.sprite.spritecollideany(self.bullet_group, self.zombie_group)
        zombie_collision = pygame.sprite.spritecollideany(self.player, self.zombie_group)

        if bullet_collision:
            self.zombie_health -= self.player_damage
            self.bullet_group.reset()
            if self.zombie_health <= 0:
                self.wave_list.remove(self.zombie_group)
                if len(self.wave_list) <= 0:
                    self.start_new_wave()

        if zombie_collision:
            self.player_health -= self.zombie_damage
            if self.player_health > 0:
                if self.zombie_group.rect.x < 400:
                    self.zombie_group.rect.x -= self.knockback
                if self.zombie_group.rect.x > 400:
                    self.zombie_group.rect.x += self.knockback
                if self.zombie_group.rect.y < 400:
                    self.zombie_group.rect.y -= self.knockback
                if self.zombie_group.rect.y > 400:
                    self.zombie_group.rect.y += self.knockback
            if self.player_health <= 0:
                self.main_menu("Zombies", "Press RETURN to restart")
                self.zombie_group.reset()
                self.player.reset()
                self.bullet_group.reset()

    def start_new_wave(self):
        """Start a new wave"""
        #Reset round values
        # for i in range(self.num_zom):
        #     self.zombie_group.add(Zombie)
        #
        # self.wave_text = font.render("Wave " + str(wave), True, RED)
        # self.wave_rect = self.wave_text.get_rect()
        # self.wave_rect.center = (WIDTH // 2, HEIGHT // 2)
        #
        # pygame.time.wait(5000)
        #
        # self.wave_rect.topleft = (10, 10)

    def main_menu(self, main_text, sub_text):
        """Pause the game"""
        global running
        # Set color
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)

        #Create the main pause text
        main_text = self.font.render(main_text, True, WHITE)
        main_rect = main_text.get_rect()
        main_rect.center = (WIDTH//2, HEIGHT//2)
        # Create the sub pause text
        sub_text = self.font.render(sub_text, True, WHITE)
        sub_rect = sub_text.get_rect()
        sub_rect.center = (WIDTH//2, HEIGHT//2 + 64)
        #Display the pause text
        display_surface.fill(BLACK)
        display_surface.blit(main_text, main_rect)
        display_surface.blit(sub_text, sub_rect)
        pygame.display.update()
        #Pause the game
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        is_paused = False
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    def pause_game(self, main_text, sub_text):
        """Pause the game"""
        global running
        # Set color
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)

        #Create the main pause text
        main_text = self.font.render(main_text, True, WHITE)
        main_rect = main_text.get_rect()
        main_rect.center = (WIDTH//2, HEIGHT//2)
        # Create the sub pause text
        sub_text = self.font.render(sub_text, True, WHITE)
        sub_rect = sub_text.get_rect()
        sub_rect.center = (WIDTH//2, HEIGHT//2 + 64)
        #Display the pause text
        display_surface.blit(main_text, main_rect)
        display_surface.blit(sub_text, sub_rect)
        pygame.display.update()
        #Pause the game
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        is_paused = False
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

class Player(pygame.sprite.Sprite):
    """A player class that the user can control"""
    def __init__(self):
        """Initialize the player"""
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("Top-Down Player.png"), (64, 64))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.pos = (WIDTH // 2, HEIGHT // 2)
        # self.bullet_image = pygame.transform.scale(pygame.image.load("New Piskel.png"), (96, 128))
        # self.bullet_rect = self.bullet_image.get_rect()
        # self.bullet_pos = self.rect.center
        self.frame_count = 0
        self.lives = 3

    def update(self):
        """Update the player"""
        # Rotating the player to the mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()
        player_x, player_y = self.pos

        dir_x, dir_y = mouse_x - player_x, mouse_y - player_y

        self.rot = (180 / math.pi) * math.atan2(-dir_x, -dir_y)

        self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("Top-Down Player.png"), (64, 64)), self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        # mouse_x, mouse_y = pygame.mouse.get_pos()
        # bullet_x, bullet_y = self.bullet_pos
        #
        # dir_x, dir_y = mouse_x - bullet_x, mouse_y - bullet_y
        #
        # self.bullet_rot = (180 / math.pi) * math.atan2(-dir_x, -dir_y)
        #
        # self.bullet_image = pygame.transform.rotate(pygame.image.load("New Piskel.png"), self.bullet_rot)

    def reset(self):
        """Resets the players position"""
        self.rect.center = (WIDTH // 2, HEIGHT // 2)

class Bullet:
    def __init__(self, x, y):
        self.image = pygame.transform.scale(pygame.image.load("New Piskel (1).png"), (64, 64))
        self.rect = self.image.get_rect()
        self.pos = (x, y)
        self.bullet_speed = 5

        self.rect.x = WIDTH // 2
        self.rect.y = HEIGHT // 2

        mouse_x, mouse_y = pygame.mouse.get_pos()

        bullet_direction = (mouse_x - self.rect.x, mouse_y - self.rect.y)

        # bullet_direction.normalize_ip()

        self.bullet_velocity = bullet_direction * self.bullet_speed

    def update(self):
        self.pos += self.bullet_velocity * delta


class Zombie(pygame.sprite.Sprite):
    """A class to create enemy monster objects"""
    def __init__(self):
        super(Zombie, self).__init__()
        self.image = pygame.transform.scale(pygame.image.load("Top-Down Enemy.png"), (64, 64))
        self.rect = self.image.get_rect()
        self.zombie_pos = random.choice([(0, 0), (0, 400), (0, 800), (400, 0), (400, 800), (800, 0), (800, 400), (800, 800)])
        self.rect.center = self.zombie_pos
        self.velocity = random.uniform(0.5, 3)
        self.angle = 0
        if self.rect.center == (0, 0):
            self.angle = 225
        if self.rect.center == (0, 400):
            self.angle = 270
        if self.rect.center == (0, 800):
            self.angle = 315
        if self.rect.center == (400, 0):
            self.angle = 180
        if self.rect.center == (400, 800):
            self.angle = 0
        if self.rect.center == (800, 0):
            self.angle = 135
        if self.rect.center == (800, 400):
            self.angle = 90
        if self.rect.center == (800, 800):
            self.angle = 45
        self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("Top-Down Enemy.png"), (64, 64)), self.angle)
        self.vec = pygame.Vector2()
        self.player_pos_x, self.player_pos_y = WIDTH // 2, HEIGHT // 2
        self.player_pos = self.player_pos_x, self.player_pos_y

    def update(self):
        if self.angle == 225:
            self.rect.x += self.velocity
            self.rect.y += self.velocity
        if self.angle == 270:
            self.rect.x += self.velocity
        if self.angle == 315:
            self.rect.x += self.velocity
            self.rect.y -= self.velocity
        if self.angle == 180:
            self.rect.y += self.velocity
        if self.angle == 0:
            self.rect.y -= self.velocity
        if self.angle == 135:
            self.rect.x -= self.velocity
            self.rect.y += self.velocity
        if self.angle == 90:
            self.rect.x -= self.velocity
        if self.angle == 45:
            self.rect.x -= self.velocity
            self.rect.y -= self.velocity

    def reset(self):
        self.image = pygame.transform.scale(pygame.image.load("Top-Down Enemy.png"), (64, 64))
        self.rect = self.image.get_rect()
        self.zombie_pos = random.choice([(0, 0), (0, 400), (0, 800), (400, 0), (400, 800), (800, 0), (800, 400), (800, 800)])
        self.rect.center = self.zombie_pos
        self.velocity = random.uniform(0.5, 3)
        self.angle = 0



#Create a player group and Player object
my_player_group = pygame.sprite.Group()
my_player = Player()
my_player_group.add(my_player)

# my_bullet_group = pygame.sprite.Group()
my_bullet = Bullet(WIDTH // 2, HEIGHT // 2)
# my_bullet_group.add(my_bullet)

#Create a monster group.
my_zombie_group = pygame.sprite.Group()
my_zombies = Zombie()
my_zombie_group.add(my_zombies)

# Create a game object
my_game = Game(my_player, my_zombie_group)
my_game.main_menu("Zombies", "Press RETURN to begin")
my_game.start_new_wave()

bullets = []
pos = (WIDTH // 2, HEIGHT // 2)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                my_game.pause_game("Paused", "Press RETURN to resume")
            if event.type == pygame.K_SPACE and len(bullets) < MAX_BULLETS:
                bullets.append(my_bullet)

    for my_bullet in bullets[:]:
        Bullet.update()
        if not display_surface.get_rect().collidepoint(my_bullet.pos):
            bullets.remove(my_bullet)

    my_player_group.update()
    my_player_group.draw(display_surface)

    display_surface.blit(background_image, (0, 0))

    #Update and draw sprite groups
    my_player_group.update()
    my_player_group.draw(display_surface)

    my_zombie_group.update()
    my_zombie_group.draw(display_surface)

    # for bullet in bullets:
    #     bullet.draw(display_surface)

    #Update and draw the Game
    my_game.update()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()