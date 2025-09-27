import pygame, sys, random
pygame.init()

clock = pygame.time.Clock()
S_WIDTH, S_HEIGHT = 400, 900
screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
score = 0

running = True
menu_active = True
game_active = False

class Player():
    def __init__(self, x):
        self.player_obj = pygame.Rect(0, 800, 100, 100)
        self.x = x
        self.player_speed = 6

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.x -= self.player_speed

        if keys[pygame.K_d]:
            self.x += self.player_speed

        self.x = max(0, min(S_WIDTH - self.player_obj.width, self.x))
        self.player_obj.x = self.x

    def draw(self):
        pygame.draw.rect(screen, (0, 255, 0), self.player_obj)

player = Player(0)

class Enemy():
    def __init__(self):
        self.Y = 0
        self.enemy_speed = 7
        self.gravity = 0.5
        self.velocity = 0
        self.enemy_object = pygame.Rect(random.randint(0, S_WIDTH - 50), 0, 50, 50)
    
    def produce_enemy(self):
        self.enemy_object = pygame.Rect(random.randint(0, S_WIDTH - 50), 0, 50, 50)
        self.Y = 0
        self.velocity = 0

    def status_check(self):
        global score, running, menu_active, game_active
        if self.enemy_object.colliderect(player.player_obj):
            score = 0
            game_active = False
            menu_active = True
        
        if self.enemy_object.y > S_HEIGHT:
            score += 1
            self.produce_enemy()

    def update(self):
        self.velocity += self.gravity

        if self.velocity > 12:
            self.velocity = 12

        self.Y += self.velocity
        self.enemy_object.y = int(self.Y)

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), self.enemy_object)

enemy = Enemy()

def game():
    screen.fill((0, 0, 0))
    player.draw()
    enemy.draw()
    enemy.update()
    enemy.status_check()
    player.update()
    pygame.display.update()
    clock.tick(60)
    pygame.display.set_caption(f"Score: {score}")

def menu():
    screen.fill((0, 100, 0))
    pygame.display.set_caption("ENTER to begin")
        
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and menu_active:
                menu_active = False
                game_active = True

    if game_active:
        game()

    elif menu_active:
        menu()


pygame.quit()